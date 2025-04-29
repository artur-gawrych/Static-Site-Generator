
def markdown_to_blocks(markdown):
    blocks = []
    splitted = markdown.split("\n\n")
    for item in splitted:
        item.strip()
        blocks.append(item)
    return blocks