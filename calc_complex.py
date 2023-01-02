import operator

ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,  # use operator.div for Python 2
    }
def calc_value(num1, num2, oper):
    return ops[oper](num1, num2)
