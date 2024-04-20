class Parser:
    def __init__(self, lexer):
        self.lexer = lexer

    def parse(self):
        token = self.lexer.next_token()

        if token[0] == 'LBRACE':
            return self.parse_object()
        elif token[0] == 'LBRACKET':
            return self.parse_array()
        else:
            return False

    def parse_object(self):
        token = self.lexer.next_token()
        if token[0] == "RBRACE":
            return True

        while True:

            if token[0] != "STRING":
                return False
            key = token[1]

            token = self.lexer.next_token()

            if token[0] != 'COLON':
                return False

            if not self.parse_value():
                return False

            token = self.lexer.next_token()
            if token[0] == 'COMMA':
                token = self.lexer.next_token()
            elif token[0] == 'RBRACE':
                return True
            else:
                return False

    def parse_value(self):
        token = self.lexer.next_token()
        if token[0] == 'STRING' or token[0] == 'NUMBER':
            return True
        elif token[0] == 'LBRACE':
            return self.parse_object()
        elif token[0] == 'LBRACKET':
            return self.parse

    def parse_array(self):
        token = self.lexer.next_token()
        if token[0] == 'RBRACKET':
            return True

        while True:
            if not self.parse_value():
                return False

            token = self.lexer.next_token()

            if token[0] =="COMMA":
                token = self.lexer.next_token()
            elif token[0] == "RBRACKET":
                return True
            else:
                return False