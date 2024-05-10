from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None) -> None:
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        prop_string=''
        if self.value == None:
            raise ValueError("No value")
        if self.tag == None:
            return self.value
        if self.props != None:
            prop_string = self.props_to_html()
        return f"<{self.tag}{' '+ prop_string if prop_string else ''}>{self.value}</{self.tag}>"


