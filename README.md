# Conf-Abstract: Academic Conference Analysis Tool

An automated framework for crawling, extracting, and analyzing academic conference papers. This tool leverages AI agents to generate comprehensive conference reports.

## 📂 Project Structure

- **[conf-analysis](conf-analysis/)**: Core analysis logic and Skill definitions.
  - **[skills/paper-report](conf-analysis/skills/paper-report/)**: The main skill for generating paper reports. See [SKILL.md](conf-analysis/skills/paper-report/SKILL.md) for detailed workflow.
    - **[scripts/](conf-analysis/skills/paper-report/scripts/)**: Reusable scripts for paper extraction and BibTeX generation.
    - **[template/](conf-analysis/skills/paper-report/template/)**: Output templates for JSON and Markdown reports.
- **[2026](2026/)**: Directory for conference-specific data (e.g., [OOPSLA26](2026/OOPSLA26/), [ASPLOS26](2026/ASPLOS26/)). Each folder contains:
  - `url`: Target conference URL.
  - `papers.json`: Extracted paper metadata.
  - `papers.bib`: Generated BibTeX entries.
  - `summary.md`: Final analysis report.

## 🛠️ Setup

### 1. Prerequisites (uv)
This project uses [uv](https://docs.astral.sh/uv/) for Python package and environment management. Install it via:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Environment Configuration
Copy the `.env.example` to `.env` and fill in your API keys:
```bash
cp .env.example .env
# Edit .env and add your tavilyApiKey
# ...
# export .env to shell environment
export $(grep -v '^#' .env | xargs)
```

### 3. Install Dependencies & MCP Services
Use `uv` to sync dependencies and run the setup script:
```bash
# Sync Python dependencies
uv sync

# Add MCP servers (ensure tavilyApiKey is exported)
./setup.sh
```
The `setup.sh` script also uses `uvx` to run MCP servers without manual installation.

### 4. Running Claude with Plugins
Use the provided wrapper script to start Claude with the `conf-analysis` plugin enabled:
```bash
./run-claude.sh
```

## 🚀 Usage

This project follows a flexible **Meta-Process** described in [SKILL.md](conf-analysis/skills/paper-report/SKILL.md).

### Step 1: Initialize Conference Directory
Create a folder for the specific conference under the `2026/` (or current year) directory.
```bash
mkdir -p 2026/OOPSLA26
echo "https://target-conference-url.com" > 2026/OOPSLA26/url
```

### Step 2: Extract Paper List
1. Retrieve raw content (HTML/Markdown) via `curl`, `Crawl4AI`, or browser "Save as".
2. Use a sub-agent to generate `extract_papers_custom.py` using [extract_papers.py](conf-analysis/skills/paper-report/scripts/extract_papers.py) as a **reference template**.
3. Run the script to generate `papers.json`.

### Step 3: Batch Bibliography Generation
```bash
python3 conf-analysis/skills/paper-report/scripts/batch_bibtex.py 2026/OOPSLA26/papers.json --output 2026/OOPSLA26/papers.bib
```

### Step 4: Generate Summary Report
Generate the final `summary.md` using the provided [template](conf-analysis/skills/paper-report/template/summary.md).

## 🔧 Prerequisites
- Python 3.x
- Dependencies: `crawl4ai`, `bibtexparser`, `tqdm`, `pydantic`
- (Optional) MCP Servers for advanced search (Tavily, Semantic Scholar, etc.)
