from textnode import *
from htmlnode import HTMLNode
from inline_markdown import *
from block_markdown import *


def main():

#    test_TextNode = TextNode("This is text", "link", "https://gawrch.ie")
#    test_HTMLNode = HTMLNode("p1", "text", None)
#
#    test_HTMLNode.props = {
#        "href": "https://www.google.com",
#        "target": "_blank",
#    }
#    test_HTMLNode.props_to_html()
#
#    print(f"TEXT NODE TEST: {test_TextNode}")
#    print(f"HTML NODE TEST: {test_HTMLNode}")
#    print(f"{test_HTMLNode.props_to_html()}")
#
#
#    node = TextNode(
#        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
#        TextType.TEXT,
#    )
#
#    new_nodes = split_nodes_image([node])
#
#    node = TextNode(
#    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#    TextType.TEXT,
#    )
#
#    new_nodes_image_links = split_nodes_link([node])
#
#    print(new_nodes)
#
#    print(new_nodes_image_links)
#
#    print("\nTEST TEXT TO TEXTNODES\n**********************\n")
#
#    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
#
#    f_text = text_to_textnodes(text)
#
#    print(f_text)

    print("\nTESTING BLOCK MARKDOWN\n**************************\n\n")

    block_markdown_text = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
    blocks = markdown_to_blocks(block_markdown_text)

    print(blocks)
    
    heading_text = "# This is Heading 1"

    heading = block_to_block_type(heading_text)

    print(heading)

main()
