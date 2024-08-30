from token import Token


def extract_numbers(token) -> int:
    s = ''
    points = 0
    for char in token:
        if char == ".":
            points += 1
            s += char

        if char.isdigit():
            s += char

    if points > 0:
        return float(s) if len(s) != 0 else token
    return int(s) if len(s) != 0 else token


def extract_brackets(query) -> str:
    new_query = ''
    for char in query:

        if char == ')':
            new_query += " "

        new_query += char
        if char == '(':
            new_query += " "

    return new_query


class Lexer:
    def __init__(self, query):
        self.query = query
        self.index = 0
        self.current_token = None
        self.token_list = []
        self.EOF = False

    def next_token(self):
        if self.index >= len(self.query):
            self.EOF = True
            self.index = 0
        self.index += 1
        self.current_token = self.query[self.index]

    def lex(self) -> list:

        tokens = extract_brackets(self.query).lower().split(" ")

        while not self.EOF:
            self.next_token()
            if isinstance(extract_numbers(self.current_token), int):
                self.token_list.append(Token(Token.NUMBER, extract_numbers(self.current_token)))
            else:
                match self.current_token:
                    case "+":
                        self.token_list.append(Token(Token.PLUS))
                    case "-":
                        self.token_list.append(Token(Token.MINUS))
                    case "*":
                        self.token_list.append(Token(Token.MULTIPLY))
                    case "/":
                        self.token_list.append(Token(Token.DIVIDE))
                    case "(":
                        self.token_list.append(Token(Token.LBRACKET))
                    case ")":
                        self.token_list.append(Token(Token.RBRACKET))
                    case "true":
                        self.token_list.append(Token(Token.TRUE))
                    case "False":
                        self.token_list.append(Token(Token.FALSE))

        return self.token_list
