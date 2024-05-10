from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        if children is None:
            raise ValueError("Not having children is a LeafNode")
        if tag is None:
            raise ValueError("Tag is not provided")
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        childrens = ""
        prop_string= ''
        for child in self.children:
            childrens += child.to_html()
        if self.props != None:
            for key,prop in self.props.items():
                prop_string += f' {key}="{prop}"'
        return f"<{self.tag}{prop_string}> {childrens} </{self.tag}>"
    

node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

print(node.to_html())