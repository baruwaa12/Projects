import random

number_guessed = int(input('Enter a number between 0 and 100'))

Minimum = 0
Maximum = 100
not_Found = True


def looper(guess, maximum_number, attempts):
    attempts = attempts + 1
    print(f'Checking {guess} against {maximum_number}')
    if guess == maximum_number:
        print('Found')
        return attempts
    x = int(maximum_number/2)
    if guess > x :
        new_max = int(((maximum_number - x)/2)+ x)
        print(new_max)
        looper(guess, new_max, attempts)
    else:
        if guess == x:
            print('Found')
            return attempts
        new_max = int(((maximum_number - guess)/2)+ x)
        print(new_max)
        looper(guess, new_max, attempts)


result = looper(number_guessed, 100, 0)
print(f'Found in {result} attempt')



# while not_Found: 
#     Answer = number_guessed
#     if 'no' in Answer.lower() and 'higher' in Answer.lower():
#         number -= random.randint(1, 4)
#     elif 'no' in Answer.lower() and 'higher' in Answer.lower():
#         number += random.randint(1, 4)
#     elif Answer.lower() == 'no':
#         print("Higher or lower?")
#         Answer = input()
#         if Answer.lower() == 'higher':
#             number += random.randint(1, 4)
#         elif Answer.lower() == 'lower':
#             number -= random.randint(1, 4)
#     elif Answer.lower() == 'yes':
#         if attempt < 2:
#             print('Yes it only took me %s tries' % str(attempt))
#         elif attempt < 2 and attempt < 10:
#             print("Pretty good for a robot")
#         else:
#             print("That's so bad, % tries")
#         Found = False
#     attempt += 1

# print('Thanks for playing the game')

    



