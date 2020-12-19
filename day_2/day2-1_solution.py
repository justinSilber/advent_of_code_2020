import re

valid = 0
xmas_reg = re.compile(r'((\d+)-(\d+))\s+(\w):\s+(\w+)')
with open('day2_input') as day2:
    for line in day2:
        mo = xmas_reg.search(line)
        if (mo.group(5)).count(mo.group(4)) >= int((mo.group(2))) and \
            (mo.group(5)).count(mo.group(4)) <= int((mo.group(3))):
            valid += 1

print(f"There are {valid} valid passwords")
