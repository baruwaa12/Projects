import random


charsUsed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!£$%^&*()-=/#"


# Easiest way to create an infinite loop
while 1:
  passwordLen = int(input("How long do you want the password to be?: "))
  passwordCounter = int(input("How many passwords would like to have?: "))
  
  for x in range(0, passwordLen):
    Password = " "

    # After each iteration passwordChars will get a "random" element from charsUsed
    # Then passwordChars is added to the empty password string
    
    for x in range(0, passwordCounter):
      PasswordChars = random.choice(charsUsed)
      Password = PasswordChars + Password
    print("Here is your password: ", Password)
      
      
      