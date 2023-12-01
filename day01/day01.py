#!/usr/bin/env python3
#=======================================================================
#
# day01.py
# --------
# Solutions to Advent of Code 2022, day 01.
#
#=======================================================================

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    l = []
    with open(filename,'r') as f:
        for line in f:
            l.append(line.strip())
    return l


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    my_input = get_input("day01_input.txt")
#    my_input = get_input("day01_example1.txt")

    sum_calibration = 0
    left = 0
    right = 0

    for s in my_input:
        i = 0
        while s[i] not in "0123456789":
            i += 1
        left = int(s[i])

        i = len(s) - 1
        while s[i] not in "0123456789":
            i -= 1
        right = int(s[i])
        sum_calibration += left * 10 + right


    print("Problem 1")
    print("---------")
    print("Calibration values:", sum_calibration)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
#    my_input = get_input("day01_input.txt")
    my_input = get_input("day01_example1.txt")

    numbers = "0123456789"

    num_words = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5,
                 'six':6, 'seven':7, 'eight':8, 'nine':9}

    sum_calibration = 0
    left = 0
    right = 0

    for s in my_input:
        i = 0
        while s[i] not in numbers:
            i += 1
        left = int(s[i])

        i = len(s) - 1
        while s[i] not in numbers:
            i -= 1
        right = int(s[i])
        sum_calibration += left * 10 + right

    print("Problem 2")
    print("---------")
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2023, day 01")
print("===========================")
problem1()
problem2()

#=======================================================================
#=======================================================================
