from textnode import *
from htmlnode import HTMLNode


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

main()
