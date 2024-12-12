block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    blocks = list(map(lambda block: block.strip(),filter(lambda block: block != "", blocks)))
    return blocks

def block_to_block_type(block):
    if heading_block(block):
        return block_type_heading
    elif code_block(block):
        return block_type_code
    elif quote_block(block):
        return block_type_quote
    elif unordered_list_block(block):
        return block_type_unordered_list
    elif ordered_list_block(block):
        return block_type_ordered_list
    else:
        return block_type_paragraph


def heading_block(block):
    return block.startswith(('# ', '## ', '### ', '#### ', '##### ', '###### '))
        
def code_block(block):
    return block.startswith('```') and block.endswith('```')

def quote_block(block):
    return all(line.startswith('>') for line in block.split('\n'))

def unordered_list_block(block):
    return all(line.startswith(('* ', '- ')) for line in block.split('\n'))

def ordered_list_block(block):
    return all(line.startswith(f"{count}. ") for count,line in enumerate(block.split('\n'), 1))
