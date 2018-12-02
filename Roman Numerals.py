import math

numerals = ["", "I",  "II",  "III",  "IV",  "V",  "VI",  "VII",  "VIII",  "IX",  "X"]


def one_to_nine(input_number):

    if (input_number <= 10) and input_number > 0:
        return numerals[input_number]
    else:
        return "Romans did not have any negative numbers or zero"


def get_thousands(input_number):
    thousands = math.floor(input_number / 1000)
    if thousands > 0:
        return number_of_thousands[thousands]

# print(one_to_nine(0))
# print(one_to_nine(-1))
# print(one_to_nine(10))


def get_hundreds(input_number):
    # given a number likely in the thousands
    # return the hundreds
    # 2903 -> 903

    thousands = math.floor(input_number / 1000)
    hundreds = input_number - (thousands * 1000)
    return hundreds


def get_roman_nine_hundreds(input_number):
    # given a number not greater than 999
    # return the roman value
    # 900 -> CM if it's greater than 500

    if (input_number <= 999) and input_number >= 900:
        remainder = input_number - 900
        nine_hundred_tens = math.floor(remainder/10)
        nine_hundred_units = remainder - (nine_hundred_tens*10)


        return 'CM' + numerals[nine_hundred_units] + numerals[nine_hundred_tens]


def get_roman_five_hundreds(input_number):

    if (input_number <= 599) and input_number >= 500:
        return 'D'


def get_roman_four_hundreds(input_number):

    if (input_number <= 499) and input_number >= 400:
        return 'CD'


def get_roman_hundreds(input_number):
    if (input_number <= 300) and input_number >= 100:



def get_roman_ninetys(input_number):
    if (input_number <= 99) and input_number >= 90:
        return 'XC'


def get_roman_fifties(input_number):
    if (input_number <= 89) and input_number >= 50:
        return 'L'


numerals1 = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL'}
number_of_thousands = ['', 'M', 'MM', 'MMM']
number_of_hundreds = ['', 'C', 'CC', 'CCC']


# def any_number(input_number):
#     if input_number < 10:
#         return one_to_nine(input_number)
#
#     thousands = math.floor(input_number/1000)
#     if thousands > 0:
#         return number_of_thousands[thousands]
#
#     new_input1 = input_number - (thousands * 1000)
#     five_hundreds = math.floor(new_input1/500)
#     new_input2 = new_input1 - (five_hundreds * 500)
#     hundreds = math.floor(new_input2/100)
#     new_input3 = new_input2 - (hundreds * 100)
#     fifties = math.floor(new_input3/50)
#     new_input4 = new_input3 - (fifties * 50)
#     tens = math.floor(new_input4/10)

#
#     return five_hundreds
# print(get_roman_nine_hundreds(800))
# print(any_number(2000))
# print(get_hundreds(2900))
#


get_roman_nine_hundreds(987)

