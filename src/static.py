from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            nodes.append(node)
        else:
            splits = node.text.split(delimiter)
            if len(splits) % 2 == 0:
                raise Exception("Invalid markdown syntax")
            for index, segment in enumerate(splits):
                if index % 2 == 0:
                    nodes.append(TextNode(segment, TextType.TEXT))
                else:
                    nodes.append(TextNode(segment, text_type))
    return nodes
            
def extract_markdown_images(text):
    images_list = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images_list

def extract_markdown_links(text):
    links_list = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links_list


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            image_list = extract_markdown_images(node.text)
            current_text = node.text
            for image in image_list:
                alt_text, url = image[0],image[1]
                sections = current_text.split(f"![{alt_text}]({url})", 1)
                if sections[0]:
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                current_text = sections[1]
            if current_text:
                new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            link_list = extract_markdown_links(node.text)
            current_text = node.text
            for link in link_list:
                text, url = link[0],link[1]
                sections = current_text.split(f"[{text}]({url})", 1)
                if sections[0]:
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(text, TextType.LINK, url))
                current_text = sections[1]
            if current_text:
                new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)

    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)

    return nodes


def markdown_to_blocks(markdown):
    section = markdown.split('\n\n')
    section = list(filter(lambda line: line != "", map(lambda line: line.strip(), section)))
    return section


def block_to_block_type(markdown_block):
    if re.match(r'^```.*```$', markdown_block, re.DOTALL):
        return "code"
    elif re.match('^#{1,6} .+', markdown_block):
        return "heading"
    elif re.match(r'(?m)^>.*$', markdown_block) and all(line.startswith('>') for line in markdown_block.split('\n')):
        return "quote"
    elif all(line.startswith(('* ', '- ')) for line in markdown_block.split('\n')):
        return "unordered_list"
    elif all(line.startswith(f"{i}. ") for i, line in enumerate(markdown_block.split('\n'), 1)):
        return "ordered_list"
    return "paragraph"
