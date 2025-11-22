#!/usr/bin/env python3
"""
WordPress to Markdown converter for GitHub Pages
Converts HTML files from source-content/ to clean markdown files in site/
"""

import os
import re
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup
from markdownify import markdownify
import yaml


def extract_post_metadata(soup):
    """Extract title, date, author, and categories from WordPress HTML"""
    metadata = {}
    
    # Extract title
    title_elem = soup.find('h1', class_='entry-title')
    if title_elem:
        metadata['title'] = title_elem.get_text().strip()
    
    # Extract date
    date_elem = soup.find('time', class_='entry-date')
    if date_elem:
        date_str = date_elem.get('datetime')
        if date_str:
            # Parse ISO datetime and format for Jekyll
            try:
                dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                metadata['date'] = dt.strftime('%Y-%m-%d')
                metadata['datetime'] = date_str
            except:
                metadata['date'] = date_str.split('T')[0]  # fallback
    
    # Extract author
    author_elem = soup.find('span', class_='author')
    if author_elem:
        author_link = author_elem.find('a')
        if author_link:
            metadata['author'] = author_link.get_text().strip()
    
    # Extract categories
    categories_elem = soup.find('span', class_='cat-links')
    if categories_elem:
        category_links = categories_elem.find_all('a')
        if category_links:
            metadata['categories'] = [link.get_text().strip() for link in category_links]
    
    return metadata


def clean_content_html(content_soup):
    """Clean and prepare HTML content for markdown conversion"""
    if not content_soup:
        return ""
    
    # Remove WordPress-specific elements we don't want
    for elem in content_soup.find_all(['script', 'style']):
        elem.decompose()
    
    # Clean up links - make them absolute if they're internal WordPress links
    for link in content_soup.find_all('a', href=True):
        href = link.get('href')
        if href.startswith('/'):
            # These are internal WordPress links, we might want to update them later
            pass
    
    return str(content_soup)


def html_to_markdown(html_content):
    """Convert HTML content to clean markdown"""
    if not html_content:
        return ""
    
    # Use markdownify with good settings for blog content
    markdown = markdownify(
        html_content,
        heading_style="ATX",  # Use # style headers
        bullets="-",         # Use - for bullet lists
        # strip=['script', 'style'],  # Remove these tags completely - handled in clean_content_html
        convert=['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'br', 'strong', 'em', 'b', 'i', 'ul', 'ol', 'li', 'a', 'blockquote', 'table', 'tr', 'td', 'th']
    )
    
    # Clean up the markdown
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)  # Remove excessive newlines
    markdown = markdown.strip()
    
    return markdown


def generate_astro_frontmatter(metadata, content_preview=""):
    """Generate Astro frontmatter from metadata"""
    frontmatter = {
        'title': metadata.get('title', 'Untitled'),
        'description': metadata.get('description', content_preview[:160] + "..." if content_preview else "A post about " + metadata.get('title', 'Untitled')),
        'pubDate': metadata.get('date', datetime.now().strftime('%Y-%m-%d')),
    }
    
    if 'categories' in metadata:
        frontmatter['tags'] = metadata['categories']  # Map categories to tags
        
    if 'author' in metadata:
        frontmatter['author'] = metadata['author']
    
    return yaml.dump(frontmatter, default_flow_style=False).strip()


def convert_html_file(html_file_path, output_dir, source_dir):
    """Convert a single HTML file to markdown"""
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract metadata
        metadata = extract_post_metadata(soup)
        
        # Extract main content
        entry_content = soup.find('div', class_='entry-content')
        if not entry_content:
            # Try finding content in other common WordPress classes
            entry_content = soup.find('div', class_='post-content') or soup.find('article')
            
            if not entry_content:
                # Skip index pages or pages without content
                return False
        
        # Clean and convert content
        cleaned_html = clean_content_html(entry_content)
        markdown_content = html_to_markdown(cleaned_html)
        
        # Generate preview for description
        # Strip markdown symbols for preview
        content_preview = re.sub(r'[#*`\[\]]', '', markdown_content).replace('\n', ' ').strip()
        
        # Generate filename based on directory structure
        rel_path = html_file_path.parent.relative_to(source_dir)
        
        if str(rel_path) == '.':
            # Root index.html - handle specially or skip
            # For now, let's skip to avoid conflict with index.astro or map to home.md
            print(f"Skipping root file: {html_file_path}")
            return False

        # Determine output path structure
        path_str = str(rel_path)
        if path_str.startswith('recipes') or path_str == 'about':
            # Keep original structure
            output_path = output_dir / f"{rel_path}.md"
        else:
            # Move everything else under 'blog'
            output_path = output_dir / "blog" / f"{rel_path}.md"
        
        # Ensure parent directories exist
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create the full markdown file
        frontmatter = generate_astro_frontmatter(metadata, content_preview)
        full_content = f"---\n{frontmatter}\n---\n\n{markdown_content}\n"
        
        # Write the file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        print(f"Converted: {html_file_path} -> {output_path}")
        return True
        
    except Exception as e:
        print(f"Error converting {html_file_path}: {e}")
        return False


def main():
    """Main conversion function"""
    import sys
    
    # Set up paths
    source_dir = Path('source-content')
    output_dir = Path('site/src/content/blog')
    
    if not source_dir.exists():
        print(f"Error: {source_dir} directory not found")
        return
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all HTML files
    html_files = list(source_dir.rglob('*.html'))
    print(f"Found {len(html_files)} HTML files to convert")
    
    # For testing, let's process just a few files first if --test flag is passed
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        html_files = html_files[:5]  # Just process first 5 files for testing
        print(f"Test mode: processing {len(html_files)} files")
    
    # Convert each file
    success_count = 0
    for html_file in html_files:
        if convert_html_file(html_file, output_dir, source_dir):
            success_count += 1
    
    print(f"\nConversion complete: {success_count}/{len(html_files)} files converted successfully")


if __name__ == "__main__":
    main()
