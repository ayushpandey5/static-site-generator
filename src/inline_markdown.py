import re
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextNodeType.TEXT:
            new_nodes.append(node)
        else:
            split_nodes = []
            list_items = node.text.split(delimiter)
            if len(list_items) % 2 == 0:
                raise ValueError("Invalid markdown, formatted section not closed")
            for index,item in enumerate(list_items):
                if item == "":
                    continue
                if index % 2 == 0:
                    split_nodes.append(TextNode(f'{item}', TextNodeType.TEXT))
                else:
                    split_nodes.append(TextNode(f'{item}', text_type))
            new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextNodeType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        images = extract_markdown_images(text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            sections = text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextNodeType.TEXT))
            new_nodes.append(TextNode(image[0], TextNodeType.IMAGE, image[1]))
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextNodeType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextNodeType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        links = extract_markdown_links(text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            sections = text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown syntax, link not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextNodeType.TEXT))
            new_nodes.append(TextNode(link[0], TextNodeType.LINK, link[1]))
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextNodeType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextNodeType.TEXT)]
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextNodeType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextNodeType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextNodeType.CODE)
    return nodes

text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
text_to_textnodes(text)