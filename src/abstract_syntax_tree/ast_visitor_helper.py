from antlr4 import ParserRuleContext

def get_unary_sign(ctx: ParserRuleContext) -> str:
    """
    Get unary sign of the given context.
    
    Returns:
        str: unary sign of the given context.
    """
    if ctx.PLUS():
        return '+'
    elif ctx.MINUS():
        return '-'
    else:
        return ""
