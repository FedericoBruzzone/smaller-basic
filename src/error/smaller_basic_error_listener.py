from antlr4.error.ErrorListener import ErrorListener

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

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(recognizer, type(recognizer))
        print(offendingSymbol, type(offendingSymbol))
        print(line, type(line))
        print(column, type(column))
        print(msg, type(msg))
        print(e, type(e))
        print()
        print(recognizer.getInputStream().getText())
        print(recognizer.getInputStream())
        print() 
        if e is None:
            print(f"Syntax warning at line {line} column {column}: {msg}.")
            print("The parser has automatically corrected the error.")
        else:
            raise Exception(f"Syntax error at line {line} column {column}: {msg}.")

