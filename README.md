# erikars.com
Source for static erikars.com website.

## Project Structure

- `site/`: The Astro project for the website.
- `source-content/`: The original WordPress content dump.
- `convert_to_markdown.py`: Script to convert content from `source-content` to `site/src/content/blog`.
- `.github/workflows/deploy.yml`: GitHub Actions workflow to deploy the site to GitHub Pages.

## Development

To run the site locally:

```bash
cd site
npm run dev
```

## Deployment

The site is automatically deployed to GitHub Pages when changes are pushed to the `main` branch.

