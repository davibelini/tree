class Lexer:
    def __init__(self, data):
        self.data   = data
        self.tokens = []
        self.keywords = [
            "dump",
            "branch",
            "cut",
            "crash"
        ]
        self.tokenize()

    def tokenize(self):
        for line in self.data:
            tmp    = []
            tmp_id = ""

            for c in line:
                if c == '"' and tmp_id == "":
                    tmp_id  = "char"
                    tmp     = []
                elif c == '"' and tmp_id == "char":
                    self.tokens.append({
                        "id": tmp_id,
                        "value": ''.join(tmp)
                    })
                    tmp = []
                    tmp_id = ""
                elif c == "~":
                    self.tokens.append({
                        "id": "branch",
                        "value": "".join(tmp)
                    })
                    tmp = []

                elif ''.join(tmp) in self.keywords:
                    self.tokens.append({
                        "id": "keyword",
                        "value": "".join(tmp)
                    })
                    tmp = []
                elif c in " \n\t" and tmp_id != "char":
                    continue
                else:
                    tmp.append(c)
