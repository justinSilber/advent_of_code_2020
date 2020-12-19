#! /usr/bin/python3
#
# Advent of Code 2020
# Day 8, part 1

day8 = open('day8_input')
day8 = day8.readlines()

def print_acc(acc):
    print(f"Accumulator value is {acc}")

def accumulist(acc, cntr, usd):
    accumulator = acc
    counter = cntr
    used = usd
    splins = day8[counter].split()
    if splins[0] == 'acc':
        if counter in used:
            print(f"Accumulator value is {accumulator}")
        else:
            accumulator += int(splins[1])
            used.append(counter)
            counter += 1
            accumulist(accumulator, counter, used)
    elif splins[0] == 'jmp':
        if counter in used:
            print(f"Accumulator value is {acc}")
        else:
            used.append(counter)
            counter += int(splins[1])
            accumulist(accumulator, counter, used)
    elif splins[0] == 'nop':
        if counter in used:
            print(f"Accumulator value is {acc}")
        else:
            used.append(counter)
            counter += 1
            accumulist(accumulator, counter, used)

accumulist(0, 0, [])