import re
from textnode import TextNode, TextType

def get_text_type_from_delimiter(delimiter):
    match delimiter:
        case "**":
            return TextType.BOLD
        case "_":
            return TextType.ITALIC
        case "`":
            return TextType.CODE
        case "[":
            return TextType.LINK
        case "![":
            return TextType.IMAGE
        case _:
            raise ValueError(f"Invalid delimiter: {delimiter}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    regex = r"\(" + re.escape(delimiter) + r".*?" + re.escape(delimiter) + r"\)"
    matches = re.findall(regex, old_nodes)
    tokens = old_nodes.split(delimiter)
    node_type = get_text_type_from_delimiter(delimiter)
    for token in tokens:
        if token in matches:
            new_nodes.append(TextNode(token, node_type))
        else:
            new_nodes.append(TextNode(token, text_type))
    return new_nodes

def extract_markdown_images(text):
    regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex, text)
    return matches

def extract_markdown_links(text):
    regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex, text)
    return matches

def split_nodes_images(old_nodes):
    new_nodes = []
    matches = extract_markdown_images(old_nodes)
    tokens = re.split(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", old_nodes)
    for token in tokens:
        if token in matches:
            new_nodes.append(TextNode(token, TextType.IMAGE))
        else:
            new_nodes.append(TextNode(token, TextType.TEXT))
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    matches = extract_markdown_links(old_nodes)
    tokens = re.split(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", old_nodes)
    for token in tokens:
        if token in matches:
            new_nodes.append(TextNode(token, TextType.LINK))
        else:
            new_nodes.append(TextNode(token, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_links(nodes)
    return nodes

def markdown_to_blocks(markdown):
    blocks = []
    for line in markdown.split("\n"):
        blocks.append(text_to_textnodes(line))
    return blocks

