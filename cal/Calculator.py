from sympy import *
from cli.Command_line import Command_line as Cli
class Calculator():

    cli:Cli

    def __init__(self):
        self.cli = Cli()

    def run(self):
        expr = self.cli.argus_parse()
        self.cal(expr)

    def cal(self, expr_str: str):
        expr = sympify(expr_str)
        result = expr.evalf()
        result = round(result, 4)
        print(result)