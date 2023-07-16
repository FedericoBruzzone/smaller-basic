from antlr4.error.ErrorListener import ErrorListener

import textwrap

from src.utils.color import set_color_red
from src.utils.color import set_color_yellow
from src.utils.color import set_color_green

class SmallerBasicErrorListener(ErrorListener):
    def __init__(self) -> None:
        super().__init__()
    
    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        #print("reportAmbiguity")
        return super().reportAmbiguity(recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs)
    
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        #print("reportAttemptingFullContext")
        return super().reportAttemptingFullContext(recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs)

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        #print("reportContextSensitivity")
        return super().reportContextSensitivity(recognizer, dfa, startIndex, stopIndex, prediction, configs)
    
    def formatErrorOrWarning(self, title: str, text: str, source_code: str, highlighted: str, color: str) -> str:
        wrapped_title: str = textwrap.fill(title,  
                                              width=80, 
                                              subsequent_indent=color("| "), 
                                              initial_indent=color("| "))
        wrapped_title_with_bar: str = '\n'.join([line_w + " "*(96-len(line_w)) + color(' |') for line_w in wrapped_title.split('\n')])

        wrapped_text: str = textwrap.fill(text,  
                                              width=80, 
                                              subsequent_indent=color("| "), 
                                              initial_indent=color("| "))
        wrapped_text_with_bar: str = '\n'.join([line_w + " "*(87-len(line_w)) + color(' |') for line_w in wrapped_text.split('\n')])

        wrapped_source_code: str = textwrap.fill(source_code,  
                                              width=80, 
                                              subsequent_indent=color("| "), 
                                              initial_indent=color("| "))
        wrapped_source_code_with_bar: str = '\n'.join([line_w + " "*(96-len(line_w)) + color(' |') for line_w in wrapped_source_code.split('\n')])

        wrapped_highlighted: str = textwrap.fill(highlighted,  
                                              width=80, 
                                              subsequent_indent=color("| "), 
                                              initial_indent=color("| "))
        wrapped_highlighted_with_bar: str = '\n'.join([line_w + " "*(96-len(line_w)) + color(' |') for line_w in wrapped_highlighted.split('\n')])
        
        message: str = set_color_green("The parser has automatically corrected the error.")         
        wrapped_message: str = textwrap.fill(message,
                                             width=80,
                                             subsequent_indent=color("| "),
                                             initial_indent=color("| "))
        wrapped_message_with_bar: str = '\n'.join([line_w + " "*(96-len(line_w)) + color(' |') for line_w in wrapped_message.split('\n')])

        if "Syntax Error" in title:
            string_f = f"""{color("+" + "-"*78 + "+")}
{wrapped_title_with_bar}
{wrapped_text_with_bar}
{wrapped_source_code_with_bar}
{wrapped_highlighted_with_bar}
{color("+" + "-"*78 + "+")}"""
        else:
            string_f = f"""{color("+" + "-"*78 + "+")}
{wrapped_title_with_bar}
{wrapped_text_with_bar}
{wrapped_source_code_with_bar}
{wrapped_highlighted_with_bar}
{wrapped_message_with_bar}
{color("+" + "-"*78 + "+")}"""
        return string_f

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        inputList: list = recognizer.getInputStream().tokenSource.inputStream.strdata.split("\n")
        wrongLine: str = inputList[line-1]
        
        if e is None:
            # string_f = f"""
# ================================ {set_color_yellow("Syntax Warning")} ================================
# Syntax warning at line {set_color_yellow(str(line))} column {set_color_yellow(str(column))}: {msg}.
# {wrongLine[:column-1]}{set_color_yellow(wrongLine[column-1:column+len(offendingSymbol.text)])}{wrongLine[column+len(offendingSymbol.text):]}
# {set_color_yellow(" "*(column) + "^"*len(offendingSymbol.text))}
# The parser has automatically corrected the error.
# ===============================================================================
# """
            title: str       = " "*(int((80-len("Syntax Warning"))/2)) + set_color_yellow("Syntax Warning") + " "*(int((80-len("Syntax Warning"))/2))
            text: str        = f"Syntax warning at line {line} column {column}: {msg}."
            source_code: str = f"{wrongLine[:column-1]}{set_color_yellow(wrongLine[column-1:column+len(offendingSymbol.text)])}{wrongLine[column+len(offendingSymbol.text):]}"
            highlighted: str = set_color_yellow(" "*(column) + "^"*len(offendingSymbol.text))
            string_f: str    = self.formatErrorOrWarning(title, text, source_code, highlighted, set_color_yellow)

            print(string_f)
        else:
            # string_f = f"""
# ================================ {set_color_red("Syntax Error")} =================================
# Syntax warning at line {set_color_red(str(line))} column {set_color_red(str(column))}: {msg}.
# {wrongLine[:column-1]}{set_color_red(wrongLine[column-1:column+len(offendingSymbol.text)])}{wrongLine[column+len(offendingSymbol.text):]}
# {set_color_red(" "*(column) + "^"*len(offendingSymbol.text))}
# ===============================================================================
# """
            title: str       = " "*(int((80-len("Syntax Error"))/2)) + set_color_red("Syntax Error") + " "*(int((80-len("Syntax Error"))/2))
            text: str        = f"Syntax error at line {line} column {column}: {msg}."
            source_code: str = f"{wrongLine[:column-1]}{set_color_red(wrongLine[column-1:column+len(offendingSymbol.text)])}{wrongLine[column+len(offendingSymbol.text):]}"
            highlighted: str = set_color_red(" "*(column) + "^"*len(offendingSymbol.text))
            string_f: str    = self.formatErrorOrWarning(title, text, source_code, highlighted, set_color_red)
            print(string_f)
            return
            # raise SyntaxError(f"Syntax error at line {line} column {column}: {msg}.") 

