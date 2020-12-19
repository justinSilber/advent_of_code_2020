advent = []

with open('day1-1_input') as doc:
    for each in doc:
        advent.append(int(each))

for num_a in advent:
    for num_b in advent:
        if (num_a != num_b) and ((num_a + num_b) < 2020):
            print(f"The numbers are {num_a} and {num_b}")
            print(f"They multiply to {num_a * num_b}")