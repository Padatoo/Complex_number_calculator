import logger

num1 = ''
num2 = ''
sign = ''
mode = ''

def get_complex_num():
    num = ''
    while num == '':
        try:
            num = complex(input('Введите комплексное число в формате a+bj: '))
        except:
            print('Введены неверные символы или лишние пробелы. Попробуйте снова.')
    return num

def get_rational_num():
    num = ''
    while num == '':
        try:
            num = float(input('Введите рациональное число: '))
        except:
            print('Введены неверные символы. Попробуйте снова.')
    return num
def get_sign():
    operator = ''
    while operator not in ["+", "-", "/", "*"]:
        operator = input('Введите операцию (+, -, *, /): ')
        if operator not in ["+", "-", "/", "*"]:
            print('Неверный арифметический оператор. Попробуйте снова.')
    return operator

def get_mode():
    global mode
    print('С какими числами вы планируете работать?')
    mode = input('1. Рациональные\n2. Комплексные\nВведите 1 или 2: ')
    if mode == '1' or mode == '2':
        return int(mode)
    else:
        print('Ошибка! Введите 1 или 2.')

def get_data():
    global num1
    global sign
    global num2
    global mode
    num1 = get_rational_num() if mode == '1' else get_complex_num()
    sign = get_sign()
    num2 = get_rational_num() if mode == '1' else get_complex_num()
    return num1, sign, num2

def view_data(result):
    res_str = f'{num1} {sign} {num2} = {result}'
    logger.add_to_log(res_str)
    print(res_str)