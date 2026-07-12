
class HTMLNode(object):

    def __init__(self, tag : str = None, value : str = None, children : list = None, props : dict = None ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""
        props_str = ""
        for prop in self.props:
            props_str += f" {prop}=\"{self.props[prop]}\""
        return props_str

    def __repr__(self):
        return f"HTMLNode(\n\ttag = {self.tag}\n\tvalue = {self.value}\n\tchildren = {children}\n\tprops = {self.props}\n)"

class LeafNode(HTMLNode):
    def __init__(self, tag : str, value : str, props : dict = None ):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value!")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(\n\ttag = {self.tag}\n\tvalue = {self.value}\n\tprops = {self.props}\n)"

class ParentNode(HTMLNode):
    def __init__(self, tag : str, children : list, props : dict = None ):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("All parent nodes must have a tag!")
        if self.children == None:
            raise ValueError("All parent nodes must have children nodes!")
        html = f"<{self.tag}>"
        for child in self.children:
            html += f"{child.to_html()}"
        html += f"</{self.tag}>"
        return html

