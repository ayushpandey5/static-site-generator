class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("")
    
    def props_to_html(self):
        html=""
        for key,props in self.props.items():
            html += f' {key}="{props}"'
        return html
    
    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value= {self.value}, childrens = {self.children} props = {self.props})"