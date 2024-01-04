#!/usr/bin/python3

def fizzbuzz():
    """This Prints numbers from 1 to 100 following FizzBuzz rules."""
    for number in range(1, 101):
        output = ""
        if number % 3 == 0:
            output += "Fizz"
        if number % 5 == 0:
            output += "Buzz"
        print(output if output else number, end=" ")
