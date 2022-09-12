import random 

# These are the characters that will be used to create the password
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789![])("

while 1:
  password_len = int(input("How long do you want your password to be: "))
  password_count = int(input("How many passwords would you like: "))
  for x in range(0, password_len):
    password = " "
    for x in range(0, password_count):

      # The function choice picks a random element from an empty string
      password_char = random.choice(chars)
      password      = password + password_char
    print("Here is your password: ", password)
    
    

                       