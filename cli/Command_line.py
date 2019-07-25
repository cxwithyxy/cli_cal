import sys
import re

class Command_line():

    def get_expr_from_argus(self) -> str:
        """从命令行参数中构成初步的表达式"""
        argus = sys.argv[1:]
        expr_str = "".join(argus)
        return expr_str

    def fix_left_brackets(self, expr_str: str) -> str:
        """修复表达式中缺少的左括号"""
        count_left_brackets = expr_str.count("(")
        count_right_brackets = expr_str.count(")")
        count_should_add = count_right_brackets - count_left_brackets
        if(count_should_add > 0):
            for i in range(0, count_should_add):
                expr_str = "(" + expr_str
        return expr_str

    def percent_change(self, expr_str: str) -> str:
        """把百分号 % 转成 / 100 的方式"""
        all_match = set(re.findall(r"[0-9]+%", expr_str))
        for i in all_match:
            num_str = re.findall(r"[0-9]+", i)[0]
            to_relpace_str = f"({num_str}/100)"
            expr_str = expr_str.replace(i, to_relpace_str)
        return expr_str.replace("%","*1/100")

    def argus_parse(self) -> str:
        """解析命令行传来的参数
        
        Returns:
            
            解析好的表达式
        """
        expr_str = self.get_expr_from_argus()
        expr_str = self.fix_left_brackets(expr_str)
        expr_str = self.percent_change(expr_str)
        print(expr_str)

        return expr_str