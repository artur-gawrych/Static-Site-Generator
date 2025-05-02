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
    code = re.search("^```.*?```$", block, re.DOTALL)
    quote = re.search("^>", block)
    unordered_list = re.search("^-\s", block)
    ordered_list = re.search("^\d+\.\s", block)
    if heading:
        return BlockType.HEADING
    if code:
        return BlockType.CODE
    if quote:
        return BlockType.QUOTE
    if unordered_list:
        return BlockType.UNORDERED_LIST
    if ordered_list:
        splitted = block.splitlines()
        for i, line in enumerate(splitted, start=1):
            match = re.match("^(\d+)\.\s", line)
            if not match or int(match.group(1)) != i:
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    