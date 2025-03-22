import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Test node 1", TextType.CODE)
        node2 = TextNode("Test node 2", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("Url test node", TextType.ITALIC, url="https://google.com")
        node2 = TextNode("Url test node", TextType.ITALIC, url="https://google.com")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()