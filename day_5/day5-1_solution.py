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


# We are also looking for the highest 'seat ID'
# given by the formula "row * 8 + column" so we will
# create a variable to hold that.

highest_id = 0

for ticket in day5:
    row = row_num(ticket[0:7])
    col = col_num(ticket[7:10])
    ticket_id = row * 8 + col
    if ticket_id > highest_id:
        highest_id = ticket_id

print(f"The highest ticket ID is: {highest_id}")