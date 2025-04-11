from textnode import *
from htmlnode import HTMLNode
from functions import *


def main():

    test_TextNode = TextNode("This is text", "link", "https://gawrch.ie")
    test_HTMLNode = HTMLNode("p1", "text", None)

    test_HTMLNode.props = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    test_HTMLNode.props_to_html()

    print(f"TEXT NODE TEST: {test_TextNode}")
    print(f"HTML NODE TEST: {test_HTMLNode}")
    print(f"{test_HTMLNode.props_to_html()}")


    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )

    new_nodes = split_nodes_image([node])

    print(new_nodes)

main()
