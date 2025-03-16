import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div> <span>child</span> </div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div> <span> <b>grandchild</b> </span> </div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div> <span>child1</span><span>child2</span> </div>",
        )

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props={"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"> <span>child</span> </div>',
        )

    def test_to_html_without_tag(self):
        parent_node = ParentNode(None, [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_without_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()
            
    def test_props_to_html(self):
        parent_node = ParentNode("div", [], props={"class": "container"})
        self.assertEqual(parent_node.props_to_html(), 'class="container"')

if __name__ == '__main__':
    unittest.main()