import random

# known_number = input(int('Enter a number between 0 and 100'))

Minimum = 0
Maximum = 100
number = random.randint(0, 100)
Found = False
attempt = 0

while Found:
    print("Is it %s?") str(number)
    Answer = raw_input()
    if 'no' in Answer.lower() and 'higher' in Answer.lower():
        number -= random.randint(1, 4)
    elif 'no' in Answer.lower() and 'higher' in Answer.lower():
        number += random.randint(1, 4)
    elif Answer.lower() == 'no'
        print("Higher or lower?")
        Answer = raw_input()
        if Answer.lower() == 'higher'
            number += random.randint(1, 4)
        elif Answer.lower() == 'lower':
            number -= random.randint(1, 4)
    elif Answer.lower() == 'yes':
        if attempt < 2:
            print('Yes it only took me %s tries') % str(attempt)
        elif attempt < 2 and attempt < 10:
            print("Pretty good for a robot")
        else:
            print("That's so bad, % tries")
        Found = False
    Attempt += 1

print('Thanks for playing the game')

    



