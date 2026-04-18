# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repository is for tracking and analyzing academic conference papers (currently OOPSLA 2026). It stores research data and uses Claude Code skills to automate paper analysis and report generation.

## Generate Skills

Since web pages always change, you need to generate skills or script to handle the variant requests of user and variant kinds of conference pages.

## Skills Goal

These skills listed below may not be available yet. You need to create skills if necessary.

### Academic Paper Analysis

When user provides a conference paper webpage URL, perform the following tasks:

1. **Current Focus Summary** - Use web fetch or web search to extract key information:
   - Paper title, authors, abstract
   - Main contributions and research focus areas
   - Related work context

2. **Paper Content Understanding** - Use PDF reading when PDF is available:
   - Extract methodology, results, and conclusions
   - Identify key technical contributions

3. **Bibliography Generation** - Use MCP tools:
   - Search Google Scholar for paper citations
   - Export ACM format bib entries
   - Generate markdown citations with ACM links

4. **Reference Chain Analysis** - Find important cited papers:
   - Identify foundational/landmark papers in references
   - Search for highly cited related work
   - Trace citation relationships

## Common Commands

No build/test commands needed - this is a research data repository.

## Directory Structure

- `OOPSLA26/` - OOPSLA 2026 conference data
  - `url` - Conference website URL
  - `papers.bib` - Bibliography for all papers
- `conf-analysis/` - Claude Code plugin for paper analysis
  - `.claude-plugin/plugin.json` - Plugin manifest
  - `skills/paper-report/SKILL.md` - Paper analysis skill

## MCP Servers

Configured in `.claude/settings.json`:
- `tavily` - Web search and crawling
- `exa` - Web search

## Usage

To generate a paper report, use the skill:
```
/conf-analysis:paper-report <paper-url>
```

Or directly analyze a URL by calling Tavily/Exa MCP tools to extract paper information and generate a report.