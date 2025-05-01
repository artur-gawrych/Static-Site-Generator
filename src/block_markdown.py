from enum import Enum
import re

def markdown_to_blocks(markdown):
    blocks = []
    stripped = markdown.strip()
    splitted = re.split(r'\n\s*\n', stripped)
    for item in splitted:
        lines = item.strip().split("\n")
        cleaned_lines = [line.strip() for line in lines]
        block = "\n".join(cleaned_lines)
        if block != "":
            blocks.append(block)
    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unondered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    heading = re.search("^#{1,6}\s", block)
    if heading:
        return BlockType.heading