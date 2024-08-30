# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from lexer import Lexer

from parser import Parser

def main():
    lexer = Lexer("1 + 4 + (5 + 6) * 8 + 4")
    print(lexer.lex())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
