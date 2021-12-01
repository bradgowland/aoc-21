INFILE = 'input/day_1.txt'


def get_data():
    with open(INFILE) as infile:
        lines = infile.readlines()

    depths = []
    for line in lines:
        depths.append(int(line))

    return depths


def count_increases(depths):
    increases = 0

    # start at 1 - no change counted on initial read
    for i in range(1, len(depths)):
        if depths[i] > depths[i-1]:
            increases += 1

    return increases


def count_window_increases(depths):
    increases = 0

    # start at 3 - no change counted on initial 3 observation window, plus lookback
    for i in range(3, len(depths)):
        window = depths[i] + depths[i-1] + depths[i-2]
        prev_window = depths[i-1] + depths[i-2] + depths[i-3]
        if window > prev_window:
            increases += 1

    return increases


if __name__=="__main__":
    depths = get_data()
    increases = count_increases(depths)
    window_increases = count_window_increases(depths)

    print('*~*~*~*~*')
    print('day 1, part 1 response:')
    print(increases)
    print('day 1, part 2 response:')
    print(window_increases)
    print('*~*~*~*~*')
