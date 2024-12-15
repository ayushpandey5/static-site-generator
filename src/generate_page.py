from block_markdown import markdown_to_html_node
import os

def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line[2:].strip()
    raise ValueError("There is no h1 tag")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as from_file:
        markdown = from_file.read()

    with open(template_path, 'r') as template_file:
        template = template_file.read()

    node = markdown_to_html_node(markdown)
    html = node.to_html()

    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_file = os.path.join(dest_path, "index.html")    
    write = open(dest_file, 'w')
    write.write(template)
    write.close()


def generate_pages_recursive(dir_path, template_path, dest_path):
    files_list = os.listdir(dir_path)
    for file in files_list:
        full_path = os.path.join(dir_path, file)
        if os.path.isfile(full_path):
            print(f"Processing file {file}")
            generate_page(full_path, template_path, dest_path)
        else:
            print(f"Directory found: {file}. Recursively processing.")
            os.makedirs(os.path.join(dest_path, file), exist_ok=True)
            generate_pages_recursive(full_path, template_path, dest_path)