#! /usr/bin/python3
#
# Advent of Code
# Day 5 - part 1

# Open the input file and create a list of each ticket
day5 = open('day5_input')
day5 = day5.readlines()

# Essentially, F == 0, B == 1, and L == 0, R == 1
#
# We need to split each ticket in to the first 7 (0-6)
# and the last 3 (7-9), then convert to binary, then
# to decimal.

def row_num(row_slice):
    bin_row = row_slice.replace('F', '0')
    bin_row = bin_row.replace('B', '1')
    bin_row = '0b' + bin_row
    return int(bin_row, 2)

def col_num(bin_slice):
    bin_col = bin_slice.replace('L', '0')
    bin_col = bin_col.replace('R', '1')
    bin_col = '0b' + bin_col
    return int(bin_col, 2)

# Calculate Ticket ID using "row * 8 + column"
def ticket_id(row, col):
    return(row * 8 + col)

# Search for a missing ticket number
# with tickets _+- 1 present
def find_id(sorted_ids):
    for tick in sorted_ids:
        if tick != sorted_ids[-2:-1]:
            if tick + 2 in sorted_ids and tick + 1 not in sorted_ids:
                return tick + 1

# We'll create an empty list of ticket IDs then calculate
# and append the ones from the input list.
# Our ticket (the one we need to find) will be missing.

id_list = []

for ticket in day5:
    row = row_num(ticket[0:7])
    col = col_num(ticket[7:10])
    id_list.append(ticket_id(row, col))

# Sort the id_list
id_list.sort()

# Run the sorted ID list through the id-finding function
print(f"Your seat ID is {find_id(id_list)}")