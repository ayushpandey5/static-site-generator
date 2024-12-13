from htmlnode import *
from textnode import text_node_to_html_node
from inline_markdown import *

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    blocks = list(map(lambda block: block.strip(),filter(lambda block: block != "", blocks)))
    return blocks

def block_to_block_type(block):
    if heading_block(block):
        return block_type_heading
    elif code_block(block):
        return block_type_code
    elif quote_block(block):
        return block_type_quote
    elif unordered_list_block(block):
        return block_type_unordered_list
    elif ordered_list_block(block):
        return block_type_ordered_list
    else:
        return block_type_paragraph


def heading_block(block):
    return block.startswith(('# ', '## ', '### ', '#### ', '##### ', '###### '))
        
def code_block(block):
    return block.startswith('```') and block.endswith('```')

def quote_block(block):
    return all(line.startswith('>') for line in block.split('\n'))

def unordered_list_block(block):
    return all(line.startswith(('* ', '- ')) for line in block.split('\n'))

def ordered_list_block(block):
    return all(line.startswith(f"{count}. ") for count,line in enumerate(block.split('\n'), 1))

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_heading:
        return heading_to_node(block)
    if block_type == block_type_code:
        return code_to_node(block)
    if block_type == block_type_quote:
        return quote_to_node(block)
    if block_type == block_type_ordered_list:
        return ordered_list_to_node(block)
    if block_type == block_type_unordered_list:
        return unordered_list_to_node(block)
    if block_type == block_type_paragraph:
        return paragraph_to_node(block)
    raise ValueError("Invalid block type")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    childrens = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        childrens.append(html_node)
    return childrens

def heading_to_node(block):
    count=0
    for char in block:
        if char == "#":
            count += 1
        else:
            break
    if count+1 >= len(block):
        raise ValueError(f"Invalid Markdown: {count}")
    text = block[count+1:]
    childrens = text_to_children(text)
    return ParentNode(f'h{count}', childrens)

def code_to_node(block):
    text = block[4:-3]
    childrens = text_to_children(text)
    return ParentNode('pre', [ParentNode('code', childrens)])

def quote_to_node(block):
    lines = " ".join(map(lambda line: line.lstrip(">").strip(), block.split('\n')))
    children = text_to_children(lines)
    return ParentNode("blockquote", children)

def ordered_list_to_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def unordered_list_to_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def paragraph_to_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    childrens = []
    for block in blocks:
        html_node = block_to_html_node(block)
        childrens.append(html_node)
    return ParentNode('div', childrens)
