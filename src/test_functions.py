import unittest
from functions import split_nodes_delimiter, extract_markdown_images, split_nodes_image, split_nodes_link
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

class ExtractMarkdownLinks(unittest.TestCase):
    def test_extraction_https(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        self.assertEqual(
            result,
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        )
    def test_extraction_http(self):
        text = "This is text with a ![rick roll](http://i.imgur.com/aKaOqIh.gif) and ![obi wan](http://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        self.assertEqual(
            result,
            [("rick roll", "http://i.imgur.com/aKaOqIh.gif"), ("obi wan", "http://i.imgur.com/fJRm4Vk.jpeg")]
        )  
    def test_extraction_multiple_items(self):
        text = "This is text with a ![rick roll](http://i.imgur.com/aKaOqIh.gif) and ![obi wan](http://i.imgur.com/fJRm4Vk.jpeg) and some more ![more and more and more](https://google.com/more_more_more)"
        result = extract_markdown_images(text)
        self.assertEqual(
            result,
            [("rick roll", "http://i.imgur.com/aKaOqIh.gif"), ("obi wan", "http://i.imgur.com/fJRm4Vk.jpeg"), ("more and more and more", "https://google.com/more_more_more")]
        )

class ExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

class SplitImageAndLinkNodes(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT
            )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ],
        new_nodes,
        )

        