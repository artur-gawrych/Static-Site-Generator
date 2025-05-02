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

    def test_ordered_list_with_wrong_start_number(self):
        text = "2. Item one\n3. Item two\n4. Item three"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_ordered_list_with_gap(self):
        text = "1. Item one\n3. Item two\n4. Item three"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_ordered_list_with_repeated_number(self):
        text = "1. Item one\n1. Item two\n2. Item three"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_ordered_list_with_ten_items(self):
        text = "\n".join(f"{i}. Item {i}" for i in range(1, 11))
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_ordered_list_with_extra_spaces(self):
        text = "1.  Item one\n2.  Item two"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_code_block_with_newlines(self):
        code = "```\nThis is code\nwith multiple lines\n```"
        block_type = block_to_block_type(code)
        self.assertEqual(block_type, BlockType.CODE)

    def test_mixed_unordered_and_ordered(self):
        text = "1. Ordered item\n- Unordered item"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_quote_with_multiple_lines(self):
        text = "> This is a quote\n> that spans lines"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_heading_with_no_space(self):
        heading = "#Heading without space"
        block_type = block_to_block_type(heading)
        self.assertEqual(block_type, BlockType.PARAGRAPH)