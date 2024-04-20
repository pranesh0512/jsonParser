import sys
from parser.lexicalAnalyser import Lexer
from parser.parser import Parser
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    lexer = Lexer(data)
    parser = Parser(lexer)

    if parser.parse():
        print("Valid JSON file.")
        sys.exit(0)
    else:
        print("Invalid JSON file.")
        sys.exit(1)

if __name__ == "__main__":
    main()