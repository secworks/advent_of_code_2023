#!/usr/bin/env python3
#=======================================================================
#
# day01.py
# --------
# Solutions to Advent of Code 2022, day 02.
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
def get_games(lines):
    games = []
    for line in lines:
        (game_id, play) = line.split(':')
        gid = int(game_id.split(' ')[1])
        sets = play.split(';')
        for s in sets:
            tmp = s.split(',')
            for t in tmp:
                x, n, c = t.split(' ')
                print("color:", c, "num:", int(n))
        games.append((gid, sets))
    return games


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
#    my_input = get_input("day02_input.txt")
    my_input = get_input("day02_example1.txt")
#    print(my_input)

    my_games = get_games(my_input)
    print(my_games)

    for game in my_games:
        (gid, sets) = game
        for s in sets:
            balls = s.split(',')
            print("Game", gid, "pulls", balls)


    print("Problem 1")
    print("---------")
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    my_input = get_input("day02_input.txt")
    my_input = get_input("day02_example1.txt")

    print("Problem 2")
    print("---------")
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2023, day 02")
print("===========================")
problem1()
problem2()

#=======================================================================
#=======================================================================
