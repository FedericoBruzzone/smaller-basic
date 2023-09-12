class GotoException(Exception):
    def __init__(self, label):
        self.label = label
        super().__init__(f"goto {label}")

    def __str__(self):
        return f"goto {self.label}"
