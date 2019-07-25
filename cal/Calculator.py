from sympy import *
from cli.Command_line import Command_line as Cli
from ui.Ui import Ui
class Calculator():

    cli:Cli

    def __init__(self):
        self.cli = Cli()

    def run(self):
        expr = self.cli.argus_parse()
        result = self.cal(expr)
        ui = Ui()
        ui.add_text(self.cli.after_fix_left_brackets)
        ui.add_text(result)
        ui.run()

    def cal(self, expr_str: str):
        expr = sympify(expr_str)
        result = expr.evalf()
        result = round(result, 9)
        print(result)
        return result