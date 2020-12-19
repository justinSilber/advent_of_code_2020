def traverse_map(map_input):
    map = open(map_input)
    map = map.readlines()

    for index in range(len(map)):
        map[index] = map[index].strip()

    x, y = (0, 0)
    tree_count = 0

    for line in range(len(map)):
        x += 3
        y += 1
        if x > (len(map[0]) - 1):
            x = x - (len(map[0]))
        if y == len(map):
            print(f"The total tree count is: {tree_count}")
            break
        if map[y][x] == '#':
            tree_count += 1

sample_input = ['..##.......', '#...#...#..', '.#....#..#.', '..#.#...#.#', '.#...##..#.',\
                '..#.##.....', '.#.#.#....#', '.#........#', '#.##...#...', '#...##....#',\
                '.#..#...#.#']

#traverse_map('sample_input')
traverse_map('day3_input')


