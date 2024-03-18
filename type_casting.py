class type_casting:

    # Float to Int
    def float2int(self, x: float) -> int: return int(x)
    # Int to Float
    def int2flost(self, x: int) -> float: return float(x)
    # Str to Int
    def srt2int(self, x: str) -> int: return int("".join([y for y in [X for X in x] if y.isdigit()]))
    # Int to Str
    def int2str(self, x: int) -> str: return str(x)
    # Str to List
    def str2list(self, x: str) -> list: return [y for y in x]
    # List to Str
    def list2str(self, x: list) -> str: return "".join(x)
    # Int to List
    def int2list(self, x: int) -> str: return [int(y) for y in str(x)]
    # List to Int
    def list2int(self, x: list) -> int: return [int(y) for y in [str(y) for y in x] if y.isdigit()]



tc = type_casting()






