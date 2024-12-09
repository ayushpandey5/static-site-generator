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
