from htmlnode import *
from textnode import *
from inline_markdown import *
from block_markdown import *

def markdown_to_html_node(markdown):
    nodes = html_nodes(markdown)
    for node in nodes:
        print(node)

def html_nodes(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                html_node = HTMLNode("p", block)
            case BlockType.UNORDERED_LIST:
                html_node = HTMLNode("ul", block)
            case BlockType.ORDERED_LIST:
                html_node = HTMLNode("ol", block)
            case BlockType.HEADING:
                n = check_heading_number(block)
                html_node = HTMLNode(f"h{n}", block)
        html_nodes.append(html_node)
    return html_nodes

def check_heading_number(heading):
    n = 0
    for char in heading:
        if char == "#":
            n += 1
        else:
            break
    return n

def text_to_children(text):
    html_nodes = text_node_to_html_node(text)
    return html_nodes