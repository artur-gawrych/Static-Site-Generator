
def markdown_to_blocks(markdown):
    blocks = []
    splitted = markdown.split("\n\n")
    for item in splitted:
        blocks.append(item.strip())
    return blocks