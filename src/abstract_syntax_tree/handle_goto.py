from src.abstract_syntax_tree.goto_exception import GotoException

def handle_goto(visit_method):
    def wrapper(self, interpreter):
        if not interpreter.goto_mode:
            return visit_method(self, interpreter)
        else:
            try:
                for child in self.children:
                    if child.name == "LabelStatementStandardNode":
                        if interpreter.goto_label == child.get_id_node().get_id_name():
                            interpreter.goto_mode = False
                            interpreter.goto_label = None
                    child.visit(interpreter)
            except GotoException as e:
                interpreter.goto_mode = True
                interpreter.goto_label = e.label
                self.visit(interpreter)
    return wrapper

