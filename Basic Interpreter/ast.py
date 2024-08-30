from lexer import Token


class Statement:
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return str(self.token)


class Expression(Statement):
    def __init__(self, token):
        super().__init__(token)


class BinExpr(Expression):
    def __init__(self, token):
        self.left = Expression(token)
        self.right = Expression(token)
        super().__init__(token)


# An identifier is a token
class Identifier(Expression):
    def __init__(self, identifier, string):
        super().__init__(identifier)
        self.string = string


class NumericLiteral(Expression):
    def __init__(self, literal, value):
        super().__init__(literal)
        self.value = value



