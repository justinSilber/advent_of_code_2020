import re

valid = 0
xmas_reg = re.compile(r'((\d+)-(\d+))\s+(\w):\s+(\w+)')
with open('day2_input') as day2:
    for line in day2:
        mo = xmas_reg.search(line)
        pos1 = int(mo.group(2)) - 1
        pos2 = int(mo.group(3)) - 1
        lttr = mo.group(4)
        pwrd = mo.group(5)
        
        if  lttr == pwrd[pos1] and lttr != pwrd[pos2]:
            valid += 1
            continue
        elif lttr == pwrd[pos2] and lttr != pwrd[pos1]:
            valid += 1
            continue

print(f"There are {valid} valid passwords")
