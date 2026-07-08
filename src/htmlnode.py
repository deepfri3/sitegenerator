

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
            
