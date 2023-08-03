def parse_antlr4_tree(tokens: list) -> list:
    """
    Parse a list of tokens into a tree structure.

    Args:
        tokens (list): A list of tokens.
    Returns:
        list: A tree structure.
    """
    stack: list = []
    current_node: list = []
    for token in tokens:
        if token == '(':
            if current_node:
                stack.append(current_node)
            current_node = []
        elif token == ')':
            if stack:
                parent_node = stack.pop()
                parent_node.append(current_node)
                current_node = parent_node
        else:
            current_node.append(token)
    return current_node

def print_antlr4_tree(program: str) -> None:
    """
   Print a tree structure.

    Args:
        program (str): A program generated by ANTLR4.
    """
    tokens: list = program.replace('(', ' ( ').replace(')', ' ) ').split()
    tree: list   = parse_antlr4_tree(tokens)
    def inner(node: str, level: int = 0):
        indent: str = ' ' * (2 * level)
        if isinstance(node, list):
            print(indent + '(')
            for sub_node in node:
                inner(sub_node, level + 1)
            print(indent + ')')
        else:
            print(indent + node)
    inner(tree)
    
def build_antlr4_tree_string(program: str) -> str:
    """
    Build a tree structure string.

    Args:
        program (str): A program generated by ANTLR4.
    Returns:
        str: A tree structure string.
    """
    tokens: list = program.replace('(', ' ( ').replace(')', ' ) ').split()
    tree: list   = parse_antlr4_tree(tokens)
    def inner(node: str, level: int = 0):
        indent: str = ' ' * (2 * level)
        tree_string: str = ''
        if isinstance(node, list):
            tree_string += indent + '(\n'
            for sub_node in node:
                tree_string += inner(sub_node, level + 1)
            tree_string += indent + ')\n'
        else:
            tree_string += indent + str(node) + '\n'
        return tree_string
    return inner(tree)
