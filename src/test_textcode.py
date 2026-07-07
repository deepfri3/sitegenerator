import unittest
from textnode import TextNode, TextType

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

if __name__ == "__main__":
    unittest.main()
