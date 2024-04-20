class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def next_token(self):
        while self.pos < len(self.text) and self.text[self.pos] in [' ', '\n', '\t', '\r']:
            self.pos += 1

        if self.pos >= len(self.text):
            return None

        current_char = self.text[self.pos]

        if current_char == '{':
            self.pos += 1
            return('LBRACE', '{')
        elif current_char == '}':
            self.pos += 1
            return('RBRACE', '}')
        elif current_char == '[':
            self.pos += 1
            return('LBRACKET', '[')
        elif current_char == ']':
            self.pos += 1
            return('RBRACKET', ']')
        elif current_char == ':':
            self.pos += 1
            return('COLON', ':')
        elif current_char == ',':
            self.pos += 1
            return('COMMA', ',')
        elif current_char == '"':
            return self.tokenize_string()
        elif re.match(r'-?\d', current_char):
            return self.tokenize_number()
        elif current_char == 't' and self.text[self.pos:self.pos + 4] == 'true':
            self.pos += 4
            return ('TRUE', True)
        elif current_char == 'f' and self.text[self.pos:self.pos + 5] == 'false':
            self.pos += 5
            return ('FALSE', False)
        else:
            return('INVALID', current_char)

    def tokenize_string(self):
        start_pos = self.pos + 1
        end_pos = start_pos
        while end_pos < len(self.text):
            if self.text[end_pos] == '"':
                self.pos = end_pos+1
                return('STRING', self.text[start_pos:end_pos])
            elif self.text[end_pos] == '\\':
                end_pos += 1
            end_pos += 1
        return('INVALID', None)

    def tokenize_number(self):
        start_pos = self.pos
        end_pos = start_pos + 1
        while end_pos <len(self.text) and re.match(r'\d', self.text[end_pos]):
            end_pos += 1
        self.pos = end_pos
        return('NUMBER', int(self.text[start_pos:end_pos]))

