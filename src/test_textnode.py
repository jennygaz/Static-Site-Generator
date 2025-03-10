import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        self.assertEqual(repr(node), f"TextNode({node.text}, {node.text_type.value}, {node.url})")

    def test_repr_link(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        self.assertEqual(repr(node), f"TextNode({node.text}, {node.text_type.value}, {node.url})")

    def test_repr_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, "https://www.google.com")
        self.assertEqual(repr(node), f"TextNode({node.text}, {node.text_type.value}, {node.url})")

    def test_repr_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), f"TextNode({node.text}, {node.text_type.value}, {node.url})")

    def test_repr_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(repr(node), f"TextNode({node.text}, {node.text_type.value}, {node.url})")

    def test_repr_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(repr(node), f"TextNode({node.text}, {node.text_type.value}, {node.url})")

    def test_repr_normal(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        self.assertEqual(repr(node), f"TextNode({node.text}, {node.text_type.value}, {node.url})")

    def test_repr_invalid(self):
        node = TextNode("This is a text node", "invalid")
        self.assertEqual(type(node.text_type), type(''))

    

if __name__ == '__main__':
    unittest.main()