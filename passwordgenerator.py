import random

useable_characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

password_length = 8

password =  "".join(random.sample(useable_characters,password_length))

print(password)