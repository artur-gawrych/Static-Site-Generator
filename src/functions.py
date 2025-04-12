import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            first_delimiter = node.text.find(delimiter)
            if first_delimiter == -1:
                new_nodes.append(TextNode(node.text, TextType.TEXT))
                continue

            second_delimiter = node.text.find(delimiter, first_delimiter + len(delimiter))
            if second_delimiter == -1:
                raise Exception(f"Not a valid Markdown, missing second delimiter - {delimiter}")
            
            before = node.text[:first_delimiter]
            inside = node.text[first_delimiter + len(delimiter):second_delimiter]
            after = node.text[second_delimiter + len(delimiter):]

            new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(inside, text_type))

            additional_nodes = split_nodes_delimiter([TextNode(after, TextType.TEXT)], delimiter, text_type)
            new_nodes.extend(additional_nodes)

    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if images == -1:
            return old_nodes
        else:
            for image in images:
                sections = node.text.split(f"![{image[0]}]({image[1]})", 1)
                # new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            print(len(sections))
            for sec in sections:
                print(f"SEC: {sec}")
    return sections