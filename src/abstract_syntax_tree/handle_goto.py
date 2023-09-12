def handle_goto(visit_method):
    def wrapper(self, interpreter):
        if not interpreter.goto_mode:
            return visit_method(self, interpreter)
        else:
            if self.name == "GotoStatementStandardNode":
                for child in self.children:
                    child.visit(interpreter)
    return wrapper
