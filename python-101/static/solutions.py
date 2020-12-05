import re
import random

def check_1(a,b,answer_1):
    try:
        exec(answer_1)
    except:
        raise Exception('Error: Expression does not execute - check syntax')
    expr = re.sub(r'#| |\n|c|=','',answer_1)
    assert 'c' in locals(), 'Error: Do not change "c = " portion.'
    ans = (a**2 + b**2)**0.5
    assert locals()['c'] == ans, 'Error: Expression does not compute to correct answer'
    assert len({'+','*','a','b'} & set(expr))==4, 'Error: Must use mathematical expression, do not hardcode value'
    assert '**' in expr, 'Error: Use in-built expnoentiation'
    print('Answer 1 is correct.')

def check_2(func):
    try:
        func(1,1,1)
    except:
        raise Exception('Error: Function does not run - check syntax')
    calc_area = lambda a,b,c:(a*b + b*c + a*c) * 2
    for i in range(10):
        a, b, c = [random.randint(1,100) for i in range(3)]
        error_message = "Error: Function does not compute correct answer.\n"
        error_message += f"\tExample: {func.__name__}({a}{b}{c}) gives {func(a,b,c)}, correct answer: {calc_area(a,b,c)}"
        assert func(a,b,c) == calc_area(a,b,c), error_message
    print('Answer 2 is correct.')

def check_3(func):
    try:
        func('!',1)
        func('!',2)
    except:
        raise Exception('Error: Function does not run - check syntax')
    def answer(char, l):
        if not isinstance(char, str) or len(char) != 1:
            return "Error 1"
        if not isinstance(l, int) or not (1 <= l <= 100):
            return "Error 2"

        top = char * l
        mid = char + ' ' * (l - 2) + char

        if l == 1:
            square = char
        elif l == 2:
            square = '\n'.join([mid,mid])
        else:
            square = '\n'.join([top,*[mid] * (l-2), top])

        return square
    
    try:
        assert func(5,5).lower() == 'error 1', 'Error: Wrong charactor input argument data type does not return "Error 1"'
    except:
        raise Exception('Error: Wrong charactor input argument data type does not return "Error 1"')
    assert func('@@',5).lower() == 'error 1', 'Error: Did not check single charactor length input argument'
    try:
        assert func('@','@').lower() == 'error 2', 'Error: Did not check intger input argument'
    except:
        raise Exception('Error: Did not check intger input argument')
    try:
        assert func('@',-5).lower() == 'error 2', 'Error: Did not check integer input falls in correct range'
    except:
        'Error: Did not check integer input falls in correct range'
    for i in [1,2,5,50]:
        assert func('@',i) == answer('@',i), "Error: Incorrect output"
    print('Answer 3 is correct.')