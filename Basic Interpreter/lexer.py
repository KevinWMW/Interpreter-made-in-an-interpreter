import re


def extract_numbers(tok) -> int:
    s = ''
    points = 0
    for char in tok:
        if char == ".":
            points += 1
            s += char

        if char.isdigit():
            s += char

    if points > 0:
        return float(s) if len(s) != 0 else tok
    return int(s) if len(s) != 0 else tok


def reformat_brackets(query) -> str:
    new_query = ''
    for char in query:

        if char == ')':
            new_query += " "

        new_query += char
        if char == '(':
            new_query += " "

    return new_query


class Token:
    FALSE = "False"
    TRUE = "True"
    NUMERIC_LITERAL = "Numeric Literal"

    # Variables and constants are examples of identifiers
    IDENTIFIER = "Identifier"
    BIN_OP = "BinaryOperation"
    LBRACKET = "LBracket"
    RBRACKET = "RBracket"
    EQUAL = "Equal"
    EOF = "EOF"

    def __init__(self, type_, value, index):
        self.type = type_
        self.value = value
        self.index = index

    def __repr__(self):
        return f"({self.type}:{self.value}) at: {self.index}"


class Lexer:
    def __init__(self, query):
        self.query = reformat_brackets(query).replace(" ", "")
        self.index = -1
        self.current_token = None
        self.EOF = False

    def next_token(self):
        if self.index >= len(self.query) - 1:
            self.EOF = True
            self.index = 0
        self.index += 1
        self.current_token = self.query[self.index]

    def lex(self) -> list:
        token_list = []

        for i in range(len(self.query)):
            self.next_token()
            if isinstance(extract_numbers(self.current_token), int):
                token_list.append(Token(Token.NUMERIC_LITERAL, extract_numbers(self.current_token), self.index))
            elif self.current_token in ("+", "-", "*", "/"):
                token_list.append(Token(Token.BIN_OP, None, self.index))
            else:
                match self.current_token:
                    case "(":
                        token_list.append(Token(Token.LBRACKET, None, self.index))
                    case ")":
                        token_list.append(Token(Token.RBRACKET, None, self.index))
                    case "true":
                        token_list.append(Token(Token.TRUE, None, self.index))
                    case "false":
                        token_list.append(Token(Token.FALSE, None, self.index))

        return token_list


class UnaryOperation:
    def __init__(self, operation, operand):
        self.operand = operand
        self.operation = operation


class BinaryOperation:
    FACTOR = "factor"
    TERM = "term"
    EXPR = "expression"

    def __init__(self, operation, pre, ant):
        self.operation = operation
        self.pre = pre
        self.ant = ant

    def add(self):
        return str(f"{self.pre} + {self.ant}")

    def subtract(self):
        return str(f"{self.pre} - {self.ant}")

    def multiply(self):
        return str(f"({self.pre} * {self.ant})")

    def divide(self):
        return str(f"({self.pre} / {self.ant})")

    def __str__(self):
        return f"{self.pre} {self.operation} {self.ant}"
