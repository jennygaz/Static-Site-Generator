from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError('All parent nodes must have a tag')
        if self.children is None or self.children == []:
            raise ValueError('All parent nodes must have children')
        props = f' {self.props_to_html()}' if self.props is not None else ''
        return f'<{self.tag}{props}> {"".join([child.to_html() for child in self.children])} </{self.tag}>'
