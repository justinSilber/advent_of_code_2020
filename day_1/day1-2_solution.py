advent = []

with open('day1-1_input') as doc:
    for each in doc:
        advent.append(int(each))
stop = False
for num_a in advent:
    if stop:
        break
    for num_b in advent:
        if stop:
            break
        if (num_a != num_b) and ((num_a + num_b) < 2020):
            for num_c in advent:
                if ((num_a + num_b + num_c) == 2020):
                    print(f"The numbers are {num_a}, {num_b}, and {num_c}")
                    print(f"They multiply to {num_a * num_b * num_c}")
                    stop = True
                    break