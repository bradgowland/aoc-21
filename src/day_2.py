INFILE = 'input/day_2.txt'


def get_data():
    with open(INFILE) as infile:
        lines = infile.readlines()

    moves = []
    for line in lines:
        moves.append(str(line).replace('\n',''))

    return moves


def clean_data(moves):
    moves_dicts = []
    for move in moves:
        direction, count = move.split(' ')
        new = {
            "dir": direction,
            "ct": int(count)
        }
        moves_dicts.append(new)

    return moves_dicts


def get_position_1(moves_dicts):
    horizontal = 0
    depth = 0
    for move in moves_dicts:
        if move['dir'] == 'forward':
            horizontal += move['ct']
        elif move['dir'] == 'up':
            depth -= move['ct']
        elif move['dir'] == 'down':
            depth += move['ct']

    return horizontal, depth


def get_position_2(moves_dicts):
    horizontal = 0
    depth = 0
    aim = 0
    for move in moves_dicts:
        if move['dir'] == 'forward':
            horizontal += move['ct']
            depth += move['ct'] * aim
        elif move['dir'] == 'up':
            aim -= move['ct']
        elif move['dir'] == 'down':
            aim += move['ct']

    return horizontal, depth


if __name__=="__main__":
    moves = get_data()
    moves_dicts = clean_data(moves)
    horizontal_1, depth_1 = get_position_1(moves_dicts)
    horizontal_2, depth_2 = get_position_2(moves_dicts)

    print('~*~*~*~*~')
    print('Part 1')
    print('Horizontal position:', horizontal_1)
    print('Depth:', depth_1)
    print('Product:', horizontal_1 * depth_1)

    print('~*~*~*~*~')
    print('Part 2')
    print('Horizontal position:', horizontal_2)
    print('Depth:', depth_2)
    print('Product:', horizontal_2 * depth_2)
