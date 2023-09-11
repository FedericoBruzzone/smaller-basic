import sys

from src.interpreter.interpreter import Interpreter

if __name__ == "__main__":
    interpreter = Interpreter()
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        interpreter.run(file_path)
    else:
       print("No file path provided.")

