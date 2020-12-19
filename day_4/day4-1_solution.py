#! /usr/bin/python3

# Advent of Code
# Day 4, Problem 1 solution

# Each passport has a blank line
# Create a list splitting along a double newline
day4 = open('day4_input')
day4 = day4.read().split('\n\n')

# Create an empty list to store valid passports
# in case needed later
valid_pp = []

# Cycle through the passports, confirming the needed
# sections are present
for passport in day4:
    byr = 'byr:' in passport
    iyr = 'iyr:' in passport
    eyr = 'eyr:' in passport
    hgt = 'hgt:' in passport
    hcl = 'hcl:' in passport
    ecl = 'ecl:' in passport
    pid = 'pid:' in passport


    # If all the values are True, multiplying them will
    # equal 1. Add valid passports to the valid list.
    if byr * iyr * eyr * hgt * hcl * ecl * pid == 1:
        valid_pp.append(passport)

print(f"The number of valid passports is: {len(valid_pp)}")