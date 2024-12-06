from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "links"
    IMAGE = "images"

class TextNode:
    def __init__(self, text, text_type, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node) -> bool:
        if not isinstance(node, TextNode):
            return False
        return (
            self.text == node.text and
            self.text_type.value == node.text_type.value and
            self.url == node.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    
    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextType.TEXT:
                return LeafNode(text_node.text)
            case TextType.BOLD:
                return LeafNode(text_node.text, "b")
            case TextType.ITALIC:
                return LeafNode(text_node.text, "i")
            case TextType.IMAGE:
                return LeafNode("", "img", {"src": f"{text_node.url}", "alt": f"{text_node.text}"})
            case TextType.CODE:
                return LeafNode(text_node.text, "code")
            case TextType.LINK:
                return LeafNode(text_node.text, "a", {"href": f"{text_node.url}"})
            case _:
               raise Exception("TextType not the right type")