#!/usr/bin/env python3

import ipdb

def happy_new_year():
    i = 10
    
    while i > 0:
        print(i)
        i -= 1

    print("Happy New Year!")


def square_integers(int_list):
    squared_integers = [num * num for num in int_list]
    return squared_integers

square_integers([1, 2, 3, 4])

def fizzbuzz():
    i = 1
    while i <= 100:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        
        i += 1
        

fizzbuzz()