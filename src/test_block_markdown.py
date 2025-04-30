import unittest
from block_markdown import markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    def test_extra_blank_lines(self):
        md = """

This is a paragraph with extra space    


Another paragraph after multiple blank lines



- List item 1
- List item 2


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
            "This is a paragraph with extra space",
            "Another paragraph after multiple blank lines",
            "- List item 1\n- List item 2",
            ],
        )

    def test_single_paragraph(self):
        md = "Just a single paragraph with no blank lines"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Just a single paragraph with no blank lines"])

    def test_internal_blank_line_should_split(self):
        md = "Line one\n\nLine two"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Line one", "Line two"])

    def test_blank_lines_with_spaces(self):
        md = "First paragraph\n \nSecond paragraph\n\t\nThird paragraph"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First paragraph", "Second paragraph", "Third paragraph"])

    def test_only_blank_lines(self):
        md = "\n\n \n\t\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

