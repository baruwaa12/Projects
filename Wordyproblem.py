from operator import add, mul, truediv as div


def calculate(operators):
    operators = {
        '+': add,
        '/': div,
        '*': mul,
    }


number1 = int(input("Pick a number"))
number2 = int(input("Pick another number"))
question = str(input("What is") + number1 + operators + number2)





