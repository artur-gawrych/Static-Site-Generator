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