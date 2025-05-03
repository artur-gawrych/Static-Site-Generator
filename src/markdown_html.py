from htmlnode import *
from textnode import *
from inline_markdown import *
from block_markdown import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        

