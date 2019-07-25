


import sys

class Command_line():

    def argus_parse(self) -> str:
        argus = sys.argv[1:]
        # print(argus)
        expr_str = "".join(argus)
        # print(expr_str)
        return expr_str