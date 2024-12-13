from enum import Enum
from htmlnode import *

class TextNodeType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node):
        return self.text == text_node.text and self.text_type == text_node.text_type and self.url == text_node.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextNodeType.TEXT:
            return LeafNode(None, text_node.text)
        case TextNodeType.BOLD:
            return LeafNode('b', text_node.text)
        case TextNodeType.ITALIC:
            return LeafNode('i', text_node.text)
        case TextNodeType.CODE:
            return LeafNode('code', text_node.text)
        case TextNodeType.LINK:
            return LeafNode('a', text_node.text, {"href": text_node.url})
        case TextNodeType.IMAGE:
            return LeafNode('img', None, {"src": text_node.url, "alt": text_node.text})        
        case _:
            raise ValueError(f"Invalid type: {text_node.text_type}")