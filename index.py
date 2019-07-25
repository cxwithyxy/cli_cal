from sympy import *
# y = Symbol('y')
# print(solve("(10%-0)-y",["y"]))

expr = sympify("2+2/100")
result = expr.evalf()
print(result)