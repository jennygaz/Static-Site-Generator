import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph node")
        self.assertEqual(repr(node), "HTMLNode(" + "\n".join([
            f"tag: {node.tag}",
            f"value: {node.value}",
            f"children: {node.children}",
            f"props: {node.props}"
        ]) + "\n)")

    def test_repr_link(self):
        node = HTMLNode("a", "This is a link node", props={"href": "https://www.google.com"})
        self.assertEqual(repr(node), f"HTMLNode(tag: {node.tag}\nvalue: {node.value}\nchildren: {node.children}\nprops: {node.props}\n)")

    def test_repr_image(self):
        node = HTMLNode("img", "This is an image node", props={"src": "https://www.google.com"})
        self.assertEqual(repr(node), f"HTMLNode(tag: {node.tag}\nvalue: {node.value}\nchildren: {node.children}\nprops: {node.props}\n)")

    def test_repr_bold(self):
        node = HTMLNode("b", "This is a bold node")
        self.assertEqual(repr(node), f"HTMLNode(tag: {node.tag}\nvalue: {node.value}\nchildren: {node.children}\nprops: {node.props}\n)")

    def test_repr_italic(self):
        node = HTMLNode("i", "This is an italic node")
        self.assertEqual(repr(node), f"HTMLNode(tag: {node.tag}\nvalue: {node.value}\nchildren: {node.children}\nprops: {node.props}\n)")

    def test_repr_code(self):
        node = HTMLNode("code", "This is a code node")
        self.assertEqual(repr(node), f"HTMLNode(tag: {node.tag}\nvalue: {node.value}\nchildren: {node.children}\nprops: {node.props}\n)")

    def test_props_to_html(self):
        node = HTMLNode("a", "This is a link node", props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com"')

if __name__ == '__main__':
    unittest.main()