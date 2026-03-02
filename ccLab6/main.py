class RecursiveDescentParser:
    def __init__(self, input_string):
        self.input_string = input_string
        self.tokens = self.tokenize(input_string)
        self.position = 0
        self.current_token = None

    def tokenize(self, s):

        tokens = []
        i = 0
        n = len(s)
        while i < n:
            if s[i:i + 2] == 'if':
                tokens.append('if')
                i += 2
            elif s[i:i + 4] == 'then':
                tokens.append('then')
                i += 4
            elif s[i:i + 4] == 'else':
                tokens.append('else')
                i += 4
            elif s[i:i + 3] == 'end':
                tokens.append('end')
                i += 3
            elif s[i] in ['0', 'o']:
                tokens.append('0')
                i += 1
            elif s[i] in ['1', 'i']:
                tokens.append('1')
                i += 1
            elif s[i] == ';':
                tokens.append(';')
                i += 1
            elif s[i].isspace():
                i += 1
            else:
                raise ValueError(f"Lexical Error: Invalid character at index {i}: '{s[i]}'")
        tokens.append('$')
        return tokens

    def advance(self):
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
            self.position += 1

    def match(self, expected_token):
        if self.current_token == expected_token:
            self.advance()
        else:
            raise SyntaxError(f"Expected '{expected_token}', but found '{self.current_token}'")

    def parse(self):
        try:
            self.advance()
            self.Stmtseq()

            if self.current_token == '$':
                print("Parsing Successful: Input Accepted!")
            else:
                print("\nString Rejected")
        except (SyntaxError, ValueError) as e:
            print("\nString Rejected")

    def Stmtseq(self):
        print("Parsing Stmtseq -> Stmt {; Stmt}")
        self.Stmt()
        while self.current_token == ';':
            self.match(';')
            self.Stmt()

    def Stmt(self):
        if self.current_token == 'if':
            print("Parsing Stmt -> if Exp then Stmtseq [else Stmtseq] end")
            self.match('if')
            self.Exp()
            self.match('then')
            self.Stmtseq()

            if self.current_token == 'else':
                print("Found else, parsing else Stmtseq")
                self.match('else')
                self.Stmtseq()

            self.match('end')
            print("End of Stmt")
        else:
            pass

    def Exp(self):
        if self.current_token == '0':
            print("Parsing Exp -> 0")
            self.match('0')
        elif self.current_token == '1':
            print("Parsing Exp -> 1")
            self.match('1')
        else:
            raise SyntaxError("Expected '0' or '1' in Exp")


if __name__ == "__main__":
    user_input = input("Enter input program: ")

    parser = RecursiveDescentParser(user_input)
    parser.parse()