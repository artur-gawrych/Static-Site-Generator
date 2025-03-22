import unittest
from htmlnode import HTMLNode

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

    def test_props_str_numb(self):
        self.assertEqual(len(self.node.props), len(self.node.props_to_html().split(" ")))
  
    def test_eq(self):
        self.assertNotEqual(self.node, self.node2)
    
    def test_pass_string_props(self):
        self.assertNotIsInstance(self.node2.props, dict)

        



if __name__ == "__main__":
    unittest.main()