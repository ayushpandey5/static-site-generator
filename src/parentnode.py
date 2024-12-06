from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is needed")
        if not self.children:
            raise ValueError("Cannot be parent node without having children nodes")
        if self.children:
            children_list = []
            for child in self.children:
                children_list.append(child.to_html())
            childrens = "".join(children_list)
            return f"<{self.tag}>{childrens}</{self.tag}>"