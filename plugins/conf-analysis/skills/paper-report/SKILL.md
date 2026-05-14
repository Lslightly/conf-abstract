---
name: paper-report
description: Generate academic paper analysis report from conference webpage URL
invoke: user
---

# Paper Report Skill

This skill processes multiple academic papers from a conference webpage URL to generate comprehensive analysis reports. It extracts key information for each paper, generates citations, and finds important referenced papers.

## Parameters

- **$ARGUMENTS** – The conference webpage URL (required)
- **Conference Folder** – Conference-specific folder path (e.g., `OOPSLA26`), used to store generated scripts and conference data.

## Workflow

### Step 1: Paper List and Metadata Extraction (Meta-process)

Since conference webpage formats vary significantly, this step uses a flexible meta-process rather than a fixed script:

1. **Web Content Retrieval**:
   - Retrieve the conference webpage content using any suitable method (e.g., **curl**, **Crawl4AI**, or browser "Save as").
   - The goal is to obtain the raw HTML or a structured Markdown version to understand the page's structure and identify paper containers.

2. **Custom Extraction Script Generation**:
   - Based on the retrieved content and its structure, use a sub-agent (or Claude's coding capabilities) to generate a Python extraction script (e.g., `extract_papers_custom.py`) within the specified **Conference Folder**.

3. **Batch Processing and Generation**:
   - Run the generated custom script to extract paper metadata in batch.
   - The script should generate a `papers.json` following the template [./template/papers.json](./template/papers.json).
   - Extract and verify for each paper: Title, authors, affiliations, abstract, and publication details.

**Tools**: `curl`, `Crawl4AI`, `Sub-agent (Script Generation)`, `python3`

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

Identify foundational content and seminal papers to help readers build a solid understanding of the research topics. **When generating this section of the report, you are required to include as many relevant links as possible (e.g., links to DBLP, Google Scholar, Semantic Scholar, official paper PDFs, and author profiles).**

1. **Foundational Knowledge Extraction**:
   - Use search engines (Tavily/Exa) to find "survey", "tutorial", or "introduction" papers related to the conference themes.
   - Summarize the core concepts and historical development of the main research directions, providing links to key survey papers.

2. **Classic Paper Identification**:
   - Search for papers with exceptionally high citation counts (seminal works) in the relevant fields.
   - List 3-5 classic papers that are essential for beginners to understand the current research context, ensuring each paper has a direct link to its source or metadata page.

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

Generate a markdown report using template [template/summary.md](template/summary.md). **Crucially, the report should be rich in external links, providing direct access to papers, bibliographies, author profiles, and relevant academic databases for every piece of information presented.**

## Tips for Varied Conference Pages

- ACM/IEEE pages have consistent structure - parse DOI and metadata
- ResearchR (PL and systems conferences) have organized paper listings
- ArXiv papers have different format - check for arXiv ID
- Some conference pages only list abstracts, not full papers
- Always look for PDF links, supplementary material, and code repositories