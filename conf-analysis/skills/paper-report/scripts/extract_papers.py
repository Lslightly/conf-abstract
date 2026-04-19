import asyncio
import json
import argparse
import sys
import os
from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
from pydantic import BaseModel, Field
from typing import List, Optional

class PaperMetadata(BaseModel):
    title: str = Field(..., description="The title of the academic paper.")
    authors: Optional[str] = Field(None, description="The authors of the paper.")
    affiliations: Optional[str] = Field(None, description="The affiliations of the authors.")
    abstract: Optional[str] = Field(None, description="The abstract or a short summary of the paper.")
    publication_details: Optional[str] = Field(None, description="Publication details like venue, date, etc.")
    pdf_url: Optional[str] = Field(None, description="Link to the PDF version of the paper.")

class PaperList(BaseModel):
    papers: List[PaperMetadata]

async def extract_papers(url, output_file):
    """
    Extract paper metadata from a conference URL using Crawl4AI with a structured schema.
    """
    print(f"Crawling {url} using Crawl4AI...")

    # Define the extraction schema and mapping
    # JsonCssExtractionStrategy requires a schema that maps CSS selectors to fields.
    schema = {
        "name": "Paper List",
        "baseSelector": ".paper, .publication, li, tr, .paper-item", # Common paper containers
        "fields": [
            {"name": "title", "selector": "h3, .title, strong, .paper-title", "type": "text"},
            {"name": "authors", "selector": ".authors, .author, .paper-authors", "type": "text"},
            {"name": "affiliations", "selector": ".affiliations, .affiliation, .paper-affiliations", "type": "text"},
            {"name": "abstract", "selector": ".abstract, .paper-abstract", "type": "text"},
            {"name": "publication_details", "selector": ".venue, .publication, .paper-venue", "type": "text"},
            {"name": "pdf_url", "selector": "a[href$='.pdf']", "type": "attribute", "attribute": "href"}
        ]
    }
    
    extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)

    async with AsyncWebCrawler(verbose=True) as crawler:
        # Retry logic for network instability
        max_retries = 3
        for attempt in range(max_retries):
            try:
                result = await crawler.arun(
                    url=url,
                    extraction_strategy=extraction_strategy,
                    bypass_cache=True,
                    # Add browser-like headers to bypass simple bot detection
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    wait_for="body"
                )
                if result.success:
                    break
                print(f"Attempt {attempt + 1} failed: {result.error_message}")
                if attempt < max_retries - 1:
                    await asyncio.sleep(2) # Wait before retry
            except Exception as e:
                print(f"Attempt {attempt + 1} crashed: {e}")
                if attempt < max_retries - 1:
                    await asyncio.sleep(2)
        
        if not result.success:
            print(f"Failed to crawl {url} after {max_retries} attempts.")
            return
        
        # Get the extracted structured data
        try:
            extracted_content = result.extracted_content
            if isinstance(extracted_content, str):
                papers_data = json.loads(extracted_content)
            else:
                papers_data = extracted_content
            
            # Extract the actual list of papers
            # The structure might vary slightly depending on the strategy's output
            if isinstance(papers_data, dict) and "papers" in papers_data:
                final_papers = papers_data["papers"]
            elif isinstance(papers_data, list):
                final_papers = papers_data
            else:
                final_papers = [papers_data]

            # Save structured JSON
            with open(output_file, 'w') as f:
                json.dump(final_papers, f, indent=4)
            print(f"Successfully extracted {len(final_papers)} papers to {output_file}.")

            # Also save raw markdown for reference/manual refinement
            md_file = output_file.replace('.json', '.md')
            with open(md_file, 'w') as f:
                f.write(result.markdown)
            print(f"Saved raw markdown to {md_file} for reference.")

        except Exception as e:
            print(f"Error processing extracted content: {e}")
            # Fallback: Save whatever we have
            with open(output_file.replace('.json', '_raw.txt'), 'w') as f:
                f.write(str(result.extracted_content))
            print(f"Saved raw extracted content to {output_file.replace('.json', '_raw.txt')} due to error.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract paper metadata using Crawl4AI.")
    parser.add_argument("url", help="Conference webpage URL")
    parser.add_argument("--output", default="papers.json", help="Output JSON file path")
    
    args = parser.parse_args()
    
    asyncio.run(extract_papers(args.url, args.output))
