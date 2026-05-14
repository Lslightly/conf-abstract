#!/usr/bin/env python3
"""Extract papers from PLDI 2026 conference HTML page."""
import re
import json
import sys

def extract_papers(html_path, output_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract title + event-modal-id pairs
    pattern = r'data-event-modal="([^"]*)">([^<]*)</a></strong>'
    matches = re.findall(pattern, html)

    papers = []
    for event_id, title in matches:
        title = title.strip()
        if title == "Title TBD":
            continue  # skip keynote placeholder

        # Find authors for this paper by looking at surrounding content
        # The authors are in the next .performers div after this paper entry
        papers.append({
            "title": title,
            "event_id": event_id
        })

    print(f"Found {len(papers)} papers")

    # Now extract authors for each paper
    # Each paper entry in the HTML is a <tr> with data-slot-id
    # Followed by performers div containing author info
    # We need to iterate through the slot rows and match them

    # Extract all slot rows with their data-slot-id
    slot_pattern = r'<tr data-slot-id="([^"]*)" class="hidable">(.*?)</tr>'
    slot_matches = re.findall(slot_pattern, html, re.DOTALL)

    result = []
    for paper in papers:
        # Find the event by its modal ID in the HTML
        title_escaped = re.escape(paper['title'])
        # Find the containing tr with the relevant info
        # Use a more targeted approach
        pass

    # Alternative simpler approach: parse by sections
    # Each paper entry structure:
    # <tr data-slot-id="..." class="hidable">
    #   <td>...</td>
    #   <td>...</td>
    #   <td><strong><a href="#" data-event-modal="ID">Title</a></strong>
    #       <div class="prog-track">...</div>
    #       <div class="performers">authors</div>
    #   </td>
    # </tr>

    # Find all tr entries with data-slot-id
    tr_pattern = r'<tr data-slot-id="([^"]*)" class="hidable">(.*?)</tr>'
    tr_matches = re.findall(tr_pattern, html, re.DOTALL)

    for slot_id, content in tr_matches:
        # Extract title
        title_match = re.search(r'data-event-modal="[^"]*">([^<]*)</a></strong>', content)
        if not title_match:
            continue
        title = title_match.group(1).strip()
        if title == "Title TBD":
            continue

        # Extract authors from performers div
        performers_match = re.search(r'class="performers">(.*?)</div>', content, re.DOTALL)
        authors = []
        if performers_match:
            performers_html = performers_match.group(1)
            # Extract author names from <a> tags
            author_matches = re.findall(r'class="navigate">([^<]*)</a>', performers_html)
            authors = [a.strip() for a in author_matches if a.strip()]

        # Extract affiliations
        aff_matches = re.findall(r'class="prog-aff">([^<]*)</span>', performers_html) if performers_match else []
        affiliations = [a.strip() for a in aff_matches if a.strip()]

        result.append({
            "title": title,
            "authors": authors,
            "affiliations": affiliations
        })

    print(f"Extracted {len(result)} papers with authors")

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Saved to {output_path}")

    # Also print a summary
    for i, p in enumerate(result):
        author_str = ", ".join(p['authors'][:3])
        if len(p['authors']) > 3:
            author_str += f" et al. ({len(p['authors'])} authors)"
        print(f"  {i+1}. {p['title']}")
        print(f"     Authors: {author_str}")

if __name__ == '__main__':
    html_path = sys.argv[1] if len(sys.argv) > 1 else '/tmp/pldi26.html'
    output_path = sys.argv[2] if len(sys.argv) > 2 else '/home/lqw/mygit/conf-abstract/2026/PLDI26/papers.json'
    extract_papers(html_path, output_path)
