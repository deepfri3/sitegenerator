from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    if old_nodes is None:
        raise Exception("Missing old_nodes")
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
        else:
            num_delimiters = node.text.count(delimiter)
            if num_delimiters % 2 != 0:
                raise Exception(f"Not enough matching delimiters ({num_delimiters})")
            split_text = node.text.split(delimiter)
            delimiter_found = False
            while len(split_text) > 0:
                segment = split_text.pop(0)
                if segment == '' and len(split_text) != 0: # this was a leading delimiter
                    segment = split_text.pop(0)
                    new_nodes.append(TextNode(segment, text_type))
                elif delimiter_found:
                    new_nodes.append(TextNode(segment, text_type))
                    delimiter_found = False
                else:
                    new_nodes.append(TextNode(segment, TextType.PLAIN_TEXT))
                    delimiter_found = True
    return new_nodes

def extract_markdown_images(text : str) -> list[tuple]:
    alt_text_reggie = r"\!\[(.*?)\]\((.*?)\)"
    return re.findall(alt_text_reggie, text)

def extract_markdown_links(text : str) -> list[tuple]:
    link_text_reggie = r"\[(.*?)\]\((.*?)\)"
    return re.findall(link_text_reggie, text)

