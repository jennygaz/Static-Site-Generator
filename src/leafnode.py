from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError('All leaf nodes must have a value')
        if self.tag is None:
            return self.value
        props = f' {self.props_to_html()}' if self.props is not None else ''
        return f'<{self.tag}{props}>{self.value}</{self.tag}>'
    
    def props_to_html(self):
        return super().props_to_html()
        