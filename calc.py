import re

prev = 0
run = True


def calc():
    global run
    global prev
    if (prev == 0):
	    print('\n Enter equation: ')
    equation = str(input())
    if (prev != 0):
        equation = str(prev) + equation
    if (equation == 'quit'):
        print('Exiting now.')
        run = False
        return None
    equation = re.sub('[A-Za-z.,:!@#$%()]', '', equation)
    prev = eval(equation)
    print(prev, end='')


while run:
    calc()
