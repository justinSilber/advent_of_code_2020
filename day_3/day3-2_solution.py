def tree_loop(across, down, map):

    x, y = (0, 0)
    tree_count = 0

    for line in range(len(map)):
        x += across
        y += down
        if x > (len(map[0]) - 1):
            x = x - (len(map[0]))
        if y >= len(map):
            print(f"For {across} across and {down} down the total tree count is: {tree_count}")
            return(tree_count)
            break
        if map[y][x] == '#':
            tree_count += 1

def traverse_map(map_input):
    map = open(map_input)
    map = map.readlines()

    for index in range(len(map)):
        map[index] = map[index].strip()

    a = tree_loop(1, 1, map)
    b = tree_loop(3, 1, map)
    c = tree_loop(5, 1, map)
    d = tree_loop(7, 1, map)
    e = tree_loop(1, 2, map)

    print(f"Multiplied together, these come to: {a * b * c * d * e}")

#traverse_map('sample_input')
traverse_map('day3_input')


