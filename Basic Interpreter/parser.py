from lexer import Token
from ast import Statement, Expression, BinExpr, NumericLiteral


class Parser:
    def __init__(self, token_list: list):
        self.token_list = token_list
        self.index = 0
        self.current_token = token_list[0]
        self.EOF = False

    def lookahead(self):
        if self.index >= len(self.token_list) - 1:
            self.EOF = True
            self.index = 0
        self.index += 1
        self.current_token = self.token_list[self.index]

    def eat(self):
        first = self.current_token.pop(0)
        return first

    # Use "Recursive Descent for Parsing"
    # Doing the expression lower on the tree gives it more of a precedence counter-intuitively.
    # Make it a priority to do the expressions higher up on the tree first

    # Order of Precedence as a tree:
    # Logical Expression
    # Comparison Expression
    # Factor Expression
    # Unary Expression
    # Primary Expression

    def parse_primary_expression(self) -> Expression:
        token = self.current_token

        if token.type is Token.NUMERIC_LITERAL:
            return NumericLiteral(token.NUMERIC_LITERAL, token.value)
        elif token.type is Token.LBRACKET:
            self.eat()
            value = self.parse_expression()


    def parse_statement(self) -> Statement:
        return self.parse_expression()

    def parse_expression(self) -> Expression:
        return self.parse_additive_expression()

    # def parse_additive_expression(self) -> Expression:
    #     left = self.parse_multiplicative_expr();
    #
    #     if self.current_token.value in ("+", "-"):
    #
    #
    #     return left
    #
    # def parse_multiplicative_expr(self) -> Expression:
    #     left = self.parse_primary_expression()
    #     right
    #
    # def parse(self):
    #     return 0

    # def produce_ast(self):
    #     while not self.EOF:
    #
    # def parse_statement(self):


class Error:
    def __init__(self, line, message):
        self.line = line
        self.message = message

    def report(self):
        print(f"{self.message} at line {self.line}")
