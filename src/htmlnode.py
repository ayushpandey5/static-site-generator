class HTMLNode():
    def __init__(self, tag, value, children, props):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        prop_string = ""
        for key, val in self.props.items():
            prop_string += (f' {key}: "{val}"')
        return prop_string



class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, value, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return f"{self.value}"
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    