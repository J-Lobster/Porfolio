#!/usr/bin/env python3.10

import random

n = random.randrange(1,13)
guess = int(input("Enter any number: "))
while n != guess:
    if guess < n:
        print("too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
        break
print("you guessed it right!!")


