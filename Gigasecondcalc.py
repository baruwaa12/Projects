
age = int(input("What is your age?"))
secondsinday = (24 * 60 * 60)
daysinyear = 365
secondsinyear = secondsinday * daysinyear
secondslivedfor = secondsinyear * age


def secondslived():
    if secondslivedfor < 10**9:
        print("You have not lived for a gigasecond.")



