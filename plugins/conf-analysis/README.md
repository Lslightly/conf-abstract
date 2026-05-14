# Conference Analysis Plugin

This plugin provides academic paper analysis capabilities for conferences.

## Paper Report Skill Workflow

The following flowchart describes the automated process of generating a paper analysis report from a conference URL:

```mermaid
graph TD
    A[Start: Conference Webpage URL] --> B[Step 1: Paper List & Metadata Extraction]
    B --> C{For Each Paper}
    
    subgraph "Per-Paper Processing"
    C --> D[Step 2: PDF Retrieval & Content Understanding]
    D --> E[Step 3: Citation Search & Metadata Collection]
    end
    
    E --> F{More Papers?}
    F -- Yes --> C
    F -- No --> G[Step 3: Batch BibTeX Generation & Export]
    
    G --> H[Step 4: Subject Background & Classic Papers - Optional]
    H --> J[Step 5: Advanced Reference Chain Analysis - Optional]
    J --> I[End: Generate Final Markdown Reports]

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style I fill:#ccf,stroke:#333,stroke-width:2px
    style B fill:#fff,stroke:#333,stroke-width:1px
    style D fill:#fff,stroke:#333,stroke-width:1px
    style G fill:#fff,stroke:#333,stroke-width:1px
    style H fill:#fff,stroke:#e67e22,stroke-width:1px,stroke-dasharray: 5 5
    style J fill:#fff,stroke:#e67e22,stroke-width:1px,stroke-dasharray: 5 5
```

## Key Components

- **Metadata Extraction**: Primarily uses the [extract_papers.py](skills/paper-report/scripts/extract_papers.py) script with **Crawl4AI** to convert conference pages into structured content and generate `papers.json`.
- **PDF Retrieval**: Integrates `paper-search-mcp` and `academic-mcp` to find and download full-text PDFs.
- **Batch BibTeX**: Optimized process using the [batch_bibtex.py](skills/paper-report/scripts/batch_bibtex.py) script to search DBLP and export a unified `.bib` file, replacing multiple manual MCP calls.
- **Reference Analysis**: (In development) Specialized tools for citation graph exploration.
