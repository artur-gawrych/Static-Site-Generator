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
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        remaining_text = node.text

        images = extract_markdown_images(remaining_text)

        if not images:
            new_nodes.append(node)
            continue
        
        for alt_text, image_url in images:
            splitted = remaining_text.split(f"![{alt_text}]({image_url})", 1)

            if splitted[0]:
                new_nodes.append(TextNode(splitted[0], TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))

            if len(splitted) > 1:
                remaining_text = splitted[1]
            else:
                remaining_text = ""

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        remaining_text = node.text

        links = extract_markdown_links(remaining_text)

        if not links:
            new_nodes.append(node)
            continue

        for alt_text, link_url in links:
            splitted = remaining_text.split(f"[{alt_text}]({link_url})", 1)
            if splitted[0]:
                new_nodes.append(TextNode(splitted[0], TextType.TEXT))
            
            new_nodes.append(TextNode(alt_text, TextType.LINK, link_url))

            if len(splitted) > 1:
                remaining_text = splitted[1]
            else:
                remaining_text = ""

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    new_nodes = []
    text_node = TextNode(text, TextType.TEXT)
    image_node = split_nodes_image([text_node])
    link_node = split_nodes_link(image_node)
    bold = split_nodes_delimiter(link_node,"**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    new_nodes.append(code)
    return new_nodes