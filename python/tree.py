from pprint import pprint

from lexer import Lexer

def main():
    file_name = "tree_source/hello.tre"
    f = open(file_name, "r")
    lexer = Lexer(f.readlines())

    print("TOKENS:")
    pprint(lexer.tokens)

if __name__ == "__main__":
    main()