def calc_value(real, real1, znak):
    if znak == '+':
        result = complex(real.replace(' ', '')) + complex(real1.replace(' ', ''))
    elif znak == '-':
        result = complex(real.replace(' ', '')) - complex(real1.replace(' ', ''))
    elif znak == '*':
        result = complex(real.replace(' ', '')) * complex(real1.replace(' ', ''))
    else:
        result = complex(real.replace(' ', '')) / complex(real1.replace(' ', ''))
    return result