from block_markdown import markdown_to_html_node

def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line[2:].strip()
    raise ValueError("There is no h1 tag")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    from_file = open(from_path, 'r')
    markdown = from_file.read()
    from_file.close()

    template_file = open(template_path, 'r')
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown)
    html = node.to_html()
    print(html)

generate_page('./content/index.md', './template.html', './public')
    