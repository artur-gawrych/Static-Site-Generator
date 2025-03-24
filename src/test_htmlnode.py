import unittest
from htmlnode import HTMLNode, LeafNode

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


if __name__ == "__main__":
    unittest.main()