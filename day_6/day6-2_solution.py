#! /usr/bin/python3
#
# Advent of Code 2020
# Day 6, Part 2

# Open input file and divide groups with blank lines between them
with open('day6_input') as day6_input:
    day6 = day6_input.read().split('\n\n')

# Counter for 'Yes' answers
yes = 0

for group in day6:

    # Empty list to hold all collective 'yes' answers
    group_yes = []
    # Get the number of people in the group
    group_split = group.split('\n')
    for n in range(len(group_split)):
        if group_split[n] == '' or group_split == '\n':
            del group_split[n]
    group_size = len(group_split)
    # Cycle through the answers in the group;
    # If they occur as many times as there are
    # people in the group, add them to the list
    for answer in group.replace('\n', ''):
        if group.count(answer) == group_size and answer not in group_yes:
            group_yes.append(answer)
    # Add the group total to the grand total
    yes += len(group_yes)
    

print(f"Total 'yes' answers: {yes}")
