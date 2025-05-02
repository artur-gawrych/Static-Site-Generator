import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):
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


class TestBlockToBlockTypes(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        heading_1 = "# This is Heading 1"
        block_type = block_to_block_type(heading_1)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_code(self):
        code = "```This is code```"
        block_type = block_to_block_type(code)
        self.assertEqual(block_type, BlockType.CODE)
    
    def test_block_to_block_type_quote(self):
        quote = "> This is a quote"
        block_type = block_to_block_type(quote)
        self.assertEqual(block_type, BlockType.QUOTE)
    
    def test_block_to_block_type_unorederd_list(self):
        unordered_list = "- List item 1\n- List item 2"
        block_type = block_to_block_type(unordered_list)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_orederd_list(self):
        orederd_list = "1. List item 1\n2. List item 2\n3. List item 3"
        block_type = block_to_block_type(orederd_list)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_block_to_block_type_paragraph(self):
        paragraph = "This is just a paragraph"
        block_type = block_to_block_type(paragraph)
        self.assertEqual(block_type, BlockType.PARAGRAPH)