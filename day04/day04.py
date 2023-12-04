#!/usr/bin/env python3
#=======================================================================
#
# day01.py
# --------
# Solutions to Advent of Code 2022, day 04.
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
def get_num_array(s):
    w = []
    for x in s.split(' '):
        if len(x) > 0:
            w.append(int(x))
    return w


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_cards(lines):
    cards = []
    for line in lines:
        (h, tick1) = line.split('|')
        (head1, win) = h.split(':')
        ticket = get_num_array(tick1)
        winners = get_num_array(win)
        head = head1.split(' ')
        cards.append((int(head[-1]), ticket, winners))
    return cards


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def check_card(card):
    (i, ticket, winners) = card
    wins = 0
    for n in ticket:
        if n in winners:
            if wins == 0:
                wins = 1
            else:
                wins *=2
    return wins


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
#    my_input = get_input("day04_example1.txt")
    my_input = get_input("day04_input.txt")

    my_cards = get_cards(my_input)
    total_wins = 0
    for card in my_cards:
        total_wins += check_card(card)

    print("Problem 1")
    print("---------")
    print("Total wins:", total_wins)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
#    my_input = get_input("day04_input.txt")
    my_input = get_input("day04_example1.txt")


    print("Problem 2")
    print("---------")
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2023, day 04")
print("===========================")
problem1()
problem2()

#=======================================================================
#=======================================================================
