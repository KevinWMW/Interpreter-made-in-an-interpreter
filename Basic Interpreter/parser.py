from token import Token


class Parser:
    def __init__(self, token_list: list):
        self.token_list = token_list
        self.index = 0
        self.current_token = token_list[0]

    def next_token(self):
        self.index += 1
        self.current_token = self.token_list[self.index]
        if self.index >= len(self.token_list):
            self.index = 0
            print("End of token list")

    # Use "Recursive Descent for Parsing"
    def parse(self):
        return


class Number:
    def __init__(self, value):
        self.token = Token(Token.NUMBER, value)
        self.value = value

    def __str__(self):
        return f"{self.token}: {self.value}"


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


class Error:
    def __init__(self, line, message):
        self.line = line
        self.message = message

    def report(self):
        print(f"{self.message} at line {self.line}")
