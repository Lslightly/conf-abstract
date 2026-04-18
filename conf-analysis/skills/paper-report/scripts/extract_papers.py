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
    authors: List[str] = Field(default_factory=list, description="List of authors of the paper.")
    abstract: Optional[str] = Field(None, description="The abstract or a short summary of the paper.")
    venue: Optional[str] = Field(None, description="The conference or journal where the paper was published.")
    year: Optional[int] = Field(None, description="The publication year.")
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
        "baseSelector": ".paper, .publication, li, tr", # Common paper containers
        "fields": [
            {"name": "title", "selector": "h3, .title, strong", "type": "text"},
            {"name": "authors", "selector": ".authors, .author", "type": "text"},
            {"name": "abstract", "selector": ".abstract", "type": "text"},
            {"name": "pdf_url", "selector": "a[href$='.pdf']", "type": "attribute", "attribute": "href"}
        ]
    }
    
    extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)

    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url=url,
            extraction_strategy=extraction_strategy,
            bypass_cache=True
        )
        
        if not result.success:
            print(f"Failed to crawl {url}: {result.error_message}")
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
