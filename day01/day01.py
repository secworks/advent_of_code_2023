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
def contain_num(s):
    my_numbers = '1 one 2 two 3 three 4 four 5 five\
    6 six 7 seven 8 eight 9 nine'.split(' ')

    print(s)
    for x in my_numbers:
        if x in s:
            return True
    return False

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
#    my_input = get_input("day01_input.txt")
    my_input = get_input("day01_example2.txt")

    sum_calibration = 0

    for s in my_input:
        left = 1
        while not contain_num(s[0:left]) and left < len(s):
            print("Looking at", s[0:left])
            left += 1
        print("Left number:", s[0:left])
#
#        right = 1
#        while s[len(s) - right :] not in numbers:
#            right += 1
#        print("Right number:", s[len(s) - right :])


    print("Problem 2")
    print("---------")
    print("Calibration values:", sum_calibration)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2023, day 01")
print("===========================")
#problem1()
problem2()

#=======================================================================
#=======================================================================
