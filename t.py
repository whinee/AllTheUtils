import re

def slugify(text: str) -> str:
    """Convert a heading into a URL-safe slug."""
    text = text.lower().strip()  # Convert to lowercase and trim spaces
    text = re.sub(r"[^\w\s-]", "", text)  # Remove special characters
    return re.sub(r"\s+", "-", text)

def generate_html_heading(level: int, text: str) -> str:
    """Generate an HTML heading with a clickable link."""
    slug = slugify(text)
    return f'<h{level} id="{slug}"><a href="#{slug}">{text}</a></h{level}>'

# Example usage
heading_html = generate_html_heading(2, "Hello, World! This is a test heading.")
print(heading_html)
