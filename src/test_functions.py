import unittest
from functions import split_nodes_delimiter
from textnode import TextNode, TextType


class SplitNodesDelimiterTest(unittest.TestCase):
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    def test_code(self):
        self.assertEqual(
            self.new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        ) 

    def test_no_delimiters(self):
        """Test when there are no delimiters in the text"""
        old_nodes = [TextNode("No special formatting here", TextType.TEXT)]
        result = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        self.assertEqual(
            result,
            [TextNode("No special formatting here", TextType.TEXT)]
        )
    def test_one_delimited_text(self):
        """Test a single delimited block"""
        old_nodes = [TextNode("Text with `code` block", TextType.TEXT)]
        result = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        self.assertEqual(
            result,
            [
                TextNode("Text with ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" block", TextType.TEXT)
            ]
        )
    def test_multiple_delimiters(self):
        """Test handling multiple delimited blocks in one node"""
        old_nodes = [TextNode("`code1` and `code2`", TextType.TEXT)]
        result = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        self.assertEqual(
            result,
            [
                TextNode("", TextType.TEXT),
                TextNode("code1", TextType.CODE),
                TextNode(" and ", TextType.TEXT),
                TextNode("code2", TextType.CODE),
                TextNode("", TextType.TEXT)
            ]
        )
    def test_mixed_types(self):
        """Test nodes containing mixed types (non-text should remain unchanged)"""
        old_nodes = [
            TextNode("Text with **bold** text", TextType.TEXT),
            TextNode("Non-text node", TextType.BOLD)
        ]
        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(
            result,
            [
                TextNode("Text with ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
                TextNode("Non-text node", TextType.BOLD)
            ]
        )