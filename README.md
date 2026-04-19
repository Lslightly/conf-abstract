# Conf-Abstract: Academic Conference Analysis Tool

An automated framework for crawling, extracting, and analyzing academic conference papers. This tool leverages AI agents and specialized scripts to generate comprehensive conference reports, including metadata, bibliographies, and paper summaries.

## 📂 Project Structure

- **[conf-analysis](conf-analysis/)**: Core analysis logic and Skill definitions.
  - **[skills/paper-report](conf-analysis/skills/paper-report/)**: The main skill for generating paper reports.
    - **[scripts/](conf-analysis/skills/paper-report/scripts/)**: Reusable scripts for paper extraction and BibTeX generation.
    - **[template/](conf-analysis/skills/paper-report/template/)**: Output templates for JSON and Markdown reports.
- **[2026](2026/)**: Directory for conference-specific data (e.g., [OOPSLA26](2026/OOPSLA26/), [ASPLOS26](2026/ASPLOS26/)). Each folder contains:
  - `url`: Target conference URL.
  - `papers.json`: Extracted paper metadata.
  - `papers.bib`: Generated BibTeX entries.
  - `summary.md`: Final analysis report.

## 🚀 Usage (The Meta-Process)

This project follows a flexible **Meta-Process** to handle various conference webpage formats.

### Step 1: Initialize Conference Directory
Create a folder for the specific conference under the `2026/` (or current year) directory.
```bash
mkdir -p 2026/OOPSLA26
echo "https://target-conference-url.com" > 2026/OOPSLA26/url
```

### Step 2: Extract Paper List
Since webpage formats vary, use the most effective tool (`curl`, `Crawl4AI`, or browser "Save as") to get the content, then generate a custom extraction script.
1. Retrieve raw content (HTML/Markdown).
2. Use a sub-agent to generate `extract_papers_custom.py` based on [extract_papers.py](conf-analysis/skills/paper-report/scripts/extract_papers.py).
3. Run the script to generate `papers.json`.

### Step 3: Batch Bibliography Generation
Use the provided script to fetch BibTeX from DBLP.
```bash
python3 conf-analysis/skills/paper-report/scripts/batch_bibtex.py 2026/OOPSLA26/papers.json --output 2026/OOPSLA26/papers.bib
```

### Step 4: Generate Summary Report
Combine paper metadata, PDF content (if available), and reference analysis to generate the final `summary.md` using the provided [template](conf-analysis/skills/paper-report/template/summary.md).

## 🛠️ Key Components

- **[extract_papers.py](conf-analysis/skills/paper-report/scripts/extract_papers.py)**: Template for Crawl4AI-based extraction with browser spoofing and retry logic.
- **[batch_bibtex.py](conf-analysis/skills/paper-report/scripts/batch_bibtex.py)**: Automated DBLP search and BibTeX customization (handles SSL verification and custom keys).
- **[SKILL.md](conf-analysis/skills/paper-report/SKILL.md)**: Detailed workflow and tool requirements for AI agents.

## 🔧 Prerequisites
- Python 3.x
- Dependencies: `crawl4ai`, `bibtexparser`, `tqdm`, `pydantic`
- (Optional) MCP Servers for advanced search (Tavily, Semantic Scholar, etc.)
