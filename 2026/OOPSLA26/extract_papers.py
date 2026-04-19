#!/usr/bin/env python3
"""Extract paper metadata from OOPSLA 2026 HTML page."""

import re
import json

with open('papers.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to match each paper entry
pattern = r'<a href="#" data-event-modal="[^"]+">([^<]+)</a>.*?<div class="prog-track">OOPSLA</div>.*?<div class="performers">(.*?)</div>'

matches = re.findall(pattern, html, re.DOTALL)

papers = []
for title_match, authors_match in matches:
    title = title_match.strip()
    # Extract author names from <a> tags
    author_pattern = r'<a href="[^"]+" class="navigate">([^<]+)</a>'
    authors = re.findall(author_pattern, authors_match)
    papers.append({
        'title': title,
        'authors': authors
    })

print(f"Found {len(papers)} papers")

with open('papers.json', 'w', encoding='utf-8') as f:
    json.dump(papers, f, indent=2, ensure_ascii=False)

print("Saved to papers.json")