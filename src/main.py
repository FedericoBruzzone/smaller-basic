from src.interpreter.Interpreter import Interpreter 
import sys

if __name__ == "__main__":
    interpreter: Interpreter = Interpreter()
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        interpreter.load_file(file_path)
    else:
        print("No file path provided.")
