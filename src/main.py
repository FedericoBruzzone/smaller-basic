import sys

from src.interpreter.Interpreter import Interpreter 

if __name__ == "__main__":
    interpreter: Interpreter = Interpreter()
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        interpreter.run(file_path)
    else:
        print("No file path provided.")
