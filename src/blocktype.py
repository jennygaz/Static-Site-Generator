from enum import Enum
from htmlnode import HTMLNode

class BlockType(Enum):
    PARAGRAPH      = "paragraph"
    HEADING        = "heading"
    CODE           = "code"
    QUOTE          = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST   = "ordered_list"

def block_to_block_type(markdown_block):
    if markdown_block.startswith("#"):
        return BlockType.HEADING
    elif markdown_block.startswith("```"):
        return BlockType.CODE
    elif markdown_block.startswith(">"):
        return BlockType.QUOTE
    elif markdown_block.startswith("- "):
        return BlockType.UNORDERED_LIST
    elif markdown_block[0].isdigit() and markdown_block[1] == ".":
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    
def markdown_to_html_node(markdown):
    block_type = block_to_block_type(markdown)
    match block_type:
        case BlockType.PARAGRAPH:
            return HTMLNode("p", markdown)
        case BlockType.HEADING:
            level = 0
            while markdown[level] == "#":
                level += 1
            return HTMLNode(f"h{level}", markdown[level + 1:])
        case BlockType.CODE:
            return HTMLNode("code", markdown[3:])
        case BlockType.QUOTE:
            return HTMLNode("blockquote", markdown[2:])
        case BlockType.UNORDERED_LIST:
            return HTMLNode("ul", markdown[2:])
        case BlockType.ORDERED_LIST:
            return HTMLNode("ol", markdown[3:])
        case _:
            raise ValueError(f"Invalid BlockType: {block_type}")