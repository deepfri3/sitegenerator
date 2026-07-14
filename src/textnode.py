from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    PLAIN_TEXT = 1
    BOLD_TEXT = 2
    ITALIC_TEXT = 3
    CODE_TEXT = 4
    LINKS_ANCHOR_TEXT = 5
    IMAGE_ALT_TEXT = 6

TextTypeString = {
    TextType.PLAIN_TEXT: 'PLAIN_TEXT',
    TextType.BOLD_TEXT: 'BOLD_TEXT',
    TextType.ITALIC_TEXT: 'ITALIC_TEXT',
    TextType.CODE_TEXT: 'CODE_TEXT',
    TextType.LINKS_ANCHOR_TEXT: 'link',
    TextType.IMAGE_ALT_TEXT: 'IMAGE_ALT_TEXT'}

class TextNode(object):
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def text_node_to_html_node(self) -> LeafNode:
        match self.text_type:
            case TextType.PLAIN_TEXT:
                return LeafNode(None, self.text)
            case TextType.BOLD_TEXT:
                return LeafNode("b", self.text)
            case TextType.ITALIC_TEXT:
                return LeafNode("i", self.text)
            case TextType.CODE_TEXT:
                return LeafNode("code", self.text)
            case TextType.LINKS_ANCHOR_TEXT:
                return LeafNode("a", self.text, { "href" : "https://www.google.com"})
            case TextType.IMAGE_ALT_TEXT:
                return LeafNode("img", "", { "src" : self.url, "alt" : self.text })
            case _:
                raise Exception("Invalid TextType")

    def __eq__(self, other: object):
        if not isinstance(other, TextNode):
            return NotImplemented
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {TextTypeString[self.text_type]}, {self.url})"
