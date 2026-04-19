import json
import argparse
import sys
import urllib.request
import urllib.parse
import ssl
import time
import re
import bibtexparser
from tqdm import tqdm
from bibtexparser.bparser import BibTexParser
from bibtexparser.bibdatabase import BibDatabase

def search_dblp(title):
    """
    Search DBLP for a paper title and return the best match's BibTeX URL.
    """
    encoded_title = urllib.parse.quote(title)
    url = f"https://dblp.org/search/publ/api?q={encoded_title}&format=json&h=1"
    
    # Bypass SSL verification if it fails locally
    context = ssl._create_unverified_context()
    
    try:
        with urllib.request.urlopen(url, context=context) as response:
            data = json.loads(response.read().decode())
            hits = data.get("result", {}).get("hits", {}).get("hit", [])
            if not hits:
                return None
            
            # Get the first hit's info
            info = hits[0].get("info", {})
            url = info.get("url")
            if url and url.startswith("https://dblp.org/rec/"):
                # DBLP BibTeX URL pattern: https://dblp.org/rec/[key].bib
                return url + ".bib"
    except Exception as e:
        print(f"  Error searching DBLP for '{title}': {e}")
    return None

def fetch_bibtex(bib_url):
    """
    Fetch the BibTeX content from a DBLP .bib URL.
    """
    context = ssl._create_unverified_context()
    try:
        with urllib.request.urlopen(bib_url, context=context) as response:
            return response.read().decode()
    except Exception as e:
        print(f"  Error fetching BibTeX from {bib_url}: {e}")
    return None

def generate_custom_key(bib_content):
    """
    Generate a custom BibTeX key in the format: <FirstAuthorSurname><Year><TitleKeyword>
    Using bibtexparser for robust parsing.
    """
    try:
        parser = BibTexParser(common_strings=True)
        bib_db = bibtexparser.loads(bib_content, parser=parser)
        if not bib_db.entries:
            return None
        
        entry = bib_db.entries[0]
        author_text = entry.get('author', '')
        year = entry.get('year', '')
        title_text = entry.get('title', '')

        if not (author_text and year and title_text):
            return None

        # Get first author's surname
        authors = author_text.split(' and ')
        first_author = authors[0].strip()
        # Handle "Lastname, Firstname" or "Firstname Lastname"
        if ',' in first_author:
            surname = first_author.split(',')[0].strip()
        else:
            surname = first_author.split(' ')[-1].strip()
        
        # Remove braces and special LaTeX chars from surname
        surname = re.sub(r'[\{\}\\\'\`\"^]', '', surname).lower()
        
        # First significant word from title
        clean_title = re.sub(r'[\{\}\:\,\.\?\!\(\)\[\]\-\/\/\\\'\`\"^]', ' ', title_text)
        words = clean_title.split()
        keyword = ""
        stopwords = {'the', 'and', 'for', 'with', 'from', 'using', 'based', 'towards', 'multi', 'fusion', 'distance'}
        for word in words:
            if len(word) > 3 and word.lower() not in stopwords:
                keyword = word.capitalize()
                break
        if not keyword and words:
            keyword = words[0].capitalize()

        # Construct new key
        new_key = f"{surname}{year}{keyword}"
        new_key = re.sub(r'[^a-zA-Z0-9]', '', new_key)
        
        # Update the entry ID
        entry['ID'] = new_key
        
        # Return as BibTeX string
        return bibtexparser.dumps(bib_db)
    except Exception as e:
        print(f"  Error customizing key with bibtexparser: {e}")
        return None

def batch_process_bibtex(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            papers = json.load(f)
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)

    print(f"Starting batch process for {len(papers)} papers...")
    bib_entries = []

    for paper in tqdm(papers):
        title = paper.get('title')
        if not title:
            continue
        
        print(f"Processing: {title}")
        
        # 1. Search for the paper on DBLP
        bib_url = search_dblp(title)
        
        if bib_url:
            print(f"  Found: {bib_url}")
            # 2. Fetch BibTeX content
            bib_content = fetch_bibtex(bib_url)
            if bib_content:
                # 3. Generate custom key
                custom_bib = generate_custom_key(bib_content)
                if custom_bib:
                    bib_entries.append(custom_bib)
                    print(f"  Successfully retrieved and customized BibTeX.")
                else:
                    bib_entries.append(bib_content)
                    print(f"  Retrieved BibTeX but failed to customize key.")
            else:
                print(f"  Failed to retrieve BibTeX content.")
        else:
            print(f"  No match found on DBLP.")
        
        # Be nice to DBLP API
        time.sleep(1)

    if bib_entries:
        try:
            with open(output_file, 'w') as f:
                f.write("\n\n".join(bib_entries))
            print(f"\nBatch processing complete. Saved {len(bib_entries)} entries to {output_file}")
        except Exception as e:
            print(f"Error writing to output file: {e}")
    else:
        print("\nNo BibTeX entries were collected.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch process paper titles for BibTeX generation via DBLP API.")
    parser.add_argument("input", help="Path to JSON file containing paper titles (list of objects with 'title' key)")
    parser.add_argument("--output", default="papers.bib", help="Path to output .bib file (default: papers.bib)")
    args = parser.parse_args()
    
    batch_process_bibtex(args.input, args.output)
