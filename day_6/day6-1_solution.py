#! /usr/bin/python3
#
# Advent of Code 2020
# Day 6, Part 1

# Open input file and divide groups with blank lines between them
day6 = open('day6_input')
day6 = day6.read().split('\n\n')

# Counter for 'Yes' answers
yes = 0

for group in day6:
    # Empty list to collect respones
    group_yes = []
    # Divide that group in to its people
    subgroup = group.split('\n')
    # Cycle through the people in group
    for person in subgroup:
        # Cycle through their responses
        for response in person:
            # If their response isn't already in the group list, add it
            if response not in group_yes:
                group_yes.append(response)
    # Incremement the 'yes' counter with this group's value
    yes += len(group_yes)

print(f"Total 'yes' answers: {yes}")
    
    