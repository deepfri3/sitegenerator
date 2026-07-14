import unittest
from textnode import TextNode, TextType
from helpers import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node.url, None)

    def test_texttype_invalid(self):
        with self.assertRaises(AttributeError) as context:
            node = TextNode("This is a text node", TextType.INVALID)

        self.assertEqual(str(context.exception), "type object 'TextType' has no attribute 'INVALID'")

    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_split_nodes_delimite(self):
        old_nodes = [
            TextNode("This is text with a `code block` word", TextType.PLAIN_TEXT ),
            TextNode("`code_block` is at the beginning of text", TextType.PLAIN_TEXT ),
            TextNode("This `code block` leads to another `code block`", TextType.PLAIN_TEXT ),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE_TEXT)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE_TEXT)
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[2].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(new_nodes[3].text, "code_block")
        self.assertEqual(new_nodes[3].text_type, TextType.CODE_TEXT)
        self.assertEqual(new_nodes[4].text, " is at the beginning of text")
        self.assertEqual(new_nodes[4].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(new_nodes[5].text, "This ")
        self.assertEqual(new_nodes[5].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(new_nodes[8].text, "code block")
        self.assertEqual(new_nodes[8].text_type, TextType.CODE_TEXT)

if __name__ == "__main__":
    unittest.main()
