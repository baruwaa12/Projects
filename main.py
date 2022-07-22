# # Programming Exercises

# # Python program to check whether the given number is even or not.

# # Get a user to enter a number.
# number = input("Please enter a number")

# # Check if number is even
# isEven = int(number) % 2
# if isEven == 0:
#   print("The number " + number + " is even.")
# else:
#   print("The " + number + " is not even")

# # Convert celsius to Fahrenheit
# number1 = input("Enter a number to change it into Fahrenheit")
# numInF = (int(number1) * 1.8) + 32
# print(numInF)

# # Find the average of 10 numbers using a while loop
# count = 0
# sum = 0.0
# while(count<10):
#     number = float(input("Enter a real number: "))
#     count=count+1
#     sum = sum+number
# avg = sum/10;
# print("Average is :",avg)

# Python program to display the given integer in a reverse manner.

# NumberEntered = int(input("Enter a number to reverse"))
# reversedNumber = 0
# while (NumberEntered != 0):
#   tens = NumberEntered % 10
#   reversedNumber = (reversedNumber * 10) + tens
#   numberPrint = NumberEntered // 10
# print(reversedNumber)

# Python program to check if an integer is a prime number.

# number = int(input("Enter an integer greater than 1: "))
# isPrime = 1
# for i in range(2, number// 2):
#   if (number %i ==0):
#     isPrime = 0
#     break
#   if (isPrime==1):
#     print(number, "is a prime number")
#   else:
#     print(number, "is not a prime number")

# Python program to display all integers within the range 100-200 whose sum of digits is an even number

# for i in range(100, 200):
#   number = i
#   sum = 0
#   while( number != 0):
#     digit = number % 10
#     sum = sum + digit
#     number = number // 10
#   if (sum % 2 == 0):
#     print(i)

# Python program to check whether the given integer is a prime number or not

# number = int(input("Enter an integer greater than 1: "))
# isPrime = 1  # assuming that the number is prime
# for i in range(2, number // 2):
#     if (number % i == 0):
#         isPrime = 0
#         break
#     if (isPrime == 1):
#         print(number, "is a prime number")
#     else:
#         print(number, "is not a prime number")
