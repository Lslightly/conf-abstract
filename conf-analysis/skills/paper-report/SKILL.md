---
name: paper-report
description: Generate academic paper analysis report from conference webpage URL
invoke: user
---

# Paper Report Skill

This skill processes multiple academic papers from a conference webpage URL to generate comprehensive analysis reports. It extracts key information for each paper, generates citations, and finds important referenced papers.

## Parameters

- **$ARGUMENTS** – The conference webpage URL (required)

## Workflow

### Step 1: Paper List and Metadata Extraction

Use the [extract_papers.py](scripts/extract_papers.py) script to crawl the conference page and generate a structured paper list:

1. **Automated Crawling**:
   - Run `python3 scripts/extract_papers.py [URL]` to crawl the conference page.
   - The script uses **Crawl4AI** to convert the page into structured Markdown and an initial `papers.json`.

2. **Metadata Refinement**:
   - Review the generated `papers.json` and the accompanying `.md` file.
   - Extract and verify for each paper: Title, authors, affiliations, abstract, and publication details.
   - Ensure `papers.json` follows the template [./template/papers.json](./template/papers.json).

**Tools to use**: [extract_papers.py](scripts/extract_papers.py), `python3`

### Step 2: Paper Content Understanding and PDF Retrieval

For each paper identified in Step 1, retrieve the full content (ideally PDF):

1. **PDF Link Search**:
   - Use Tavily's web search to find direct PDF URLs.
   - If a PDF link is not directly available on the conference page, use [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp) or [LinXueyuanStdio/academic-mcp](https://github.com/LinXueyuanStdio/academic-mcp) to search for and download the PDF.
   - Search dblp to get PDF links if other sources fail.

2. **Content Extraction**:
   - Extract key sections from the PDF:
     - Introduction motivation (In current situation X, we want to get Y, but the key problem is Z. Simply say how Z is done)
     - Results and evaluation
     - Limitations and future work

**Tools to use**: `mcp__tavily__tavily_search`, `mcp-paper-search__search_papers`, `mcp-academic__search_papers`, `Read` (for downloaded PDF)

### Step 3: Batch Bibliography Generation

To save tokens and improve efficiency when processing multiple papers:
1. **Batch Preparation**:
   - Save the list of paper titles and metadata extracted in Step 1 to a structured file (e.g., `papers.json`). The example is [./template/papers.json](./template/papers.json)

2. **Automated Search and Collection**:
   - Run the Python script [batch_bibtex.py](scripts/batch_bibtex.py) to iterate through the paper list.
   - The script automatically searches DBLP via its API, retrieves the correct BibTeX entries, and aggregates them.

3. **Final Output**:
   - The script generates a single, unified `.bib` file (e.g., `papers.bib`) containing all collected entries.

**Tools to use**: [batch_bibtex.py](scripts/batch_bibtex.py), `python3`

### Step 4: Subject Background and Classic Papers (Optional)

Identify foundational content and seminal papers to help readers build a solid understanding of the research topics:

1. **Foundational Knowledge Extraction**:
   - Use search engines (Tavily/Exa) to find "survey", "tutorial", or "introduction" papers related to the conference themes.
   - Summarize the core concepts and historical development of the main research directions.

2. **Classic Paper Identification**:
   - Search for papers with exceptionally high citation counts (seminal works) in the relevant fields.
   - List 3-5 classic papers that are essential for beginners to understand the current research context.

**Tools to use**: `mcp__tavily__tavily_search`, `mcp__exa__web_search_exa`, `mcp-academic__search_papers`

### Step 5: Advanced Reference Chain Analysis (Optional)

Analyze the broader impact and connections between papers to uncover research trends:

1. **Citation Graph Exploration**:
   - Instead of simple web search, use specialized services like [LinXueyuanStdio/academic-mcp](https://github.com/LinXueyuanStdio/academic-mcp) or [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp).
   - Identify how the conference papers build upon foundational works and connect with recent trends.

2. **Specialized Analysis Tools**:
   - Consider using Python libraries like `scholarly` or `crossrefapi` for programmatic access to citation data.
   - Look for MCP services that provide semantic analysis of reference lists.

**Tools to use**: `mcp-academic__get_references`, `mcp-paper-search__get_citations`, `Python scholarly/crossref`

## Output Report Structure

Generate a markdown report using template [template/summary.md](template/summary.md)

## Tips for Varied Conference Pages

- ACM/IEEE pages have consistent structure - parse DOI and metadata
- ResearchR (PL and systems conferences) have organized paper listings
- ArXiv papers have different format - check for arXiv ID
- Some conference pages only list abstracts, not full papers
- Always look for PDF links, supplementary material, and code repositories