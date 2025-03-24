import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    node = HTMLNode()
    node.tag = "p1"
    node.value = "paragraph text"
    node.children = None
    node.props = {
    "href": "https://www.google.com",
    "target": "_blank",
    }
    
    node2 = HTMLNode()
    node2.tag = "h1"
    node2.value = "Title"
    node2.children = node
    node2.props = "string"

    def test_props_dict(self):
        self.assertIsInstance(self.node.props, dict)

    def test_eq(self):
        self.assertNotEqual(self.node, self.node2)
    
    def test_pass_string_props(self):
        self.assertNotIsInstance(self.node2.props, dict)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_h(self):
        node = LeafNode("h1", "Heading 1")
        self.assertEqual(node.to_html(), "<h1>Heading 1</h1>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_props_none(self):
        node = LeafNode("div", "Simple div")
        self.assertTrue(node.props == None)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_no_grandchildren(self):
        parent_node = ParentNode("div", None)
        self.assertRaises(ValueError)

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()