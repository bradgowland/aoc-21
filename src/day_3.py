import pandas as pd

INFILE = 'input/day_3.txt'


def get_data():
    with open(INFILE) as infile:
        lines = infile.readlines()

    binary_nums = []
    for line in lines:
        binary_nums.append(str(line).replace('\n',''))

    return binary_nums


def part_1(binary_nums):
    gamma = ''
    epsilon = ''

    # for each of the twelve positions
    for i in range(0, 12):
        current_position = ''
        # for every line in the file
        for num in binary_nums:
            current_position += str(num[i])

        # check which digit is most common
        ones = 0
        zeroes = 0
        for digit in current_position:
            if digit == '1':
                ones += 1
            else:
                zeroes += 1

        if ones > zeroes:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    gamma_base10 = int(gamma, 2)
    epsilon_base10 = int(epsilon, 2)

    return gamma_base10, epsilon_base10


def part_2(binary_nums):
    binary_df = pd.DataFrame(binary_nums)

    o2_level = binary_df
    co2_level = binary_df

    for i in range(0, 12):
        o2_mode = o2_level[0].str[i].mode()
        # pd.mode() returns a series if multiple values occur equally, default to 1
        if len(o2_mode) != 1:
            o2_mode = 1
        else:
            o2_mode = int(o2_mode)

        co2_mode = co2_level[0].str[i].mode()
        # pd.mode() returns a series if multiple values occur equally, default to 1
        if len(co2_mode) != 1:
            co2_mode = 1
        else:
            co2_mode = int(co2_mode)

        # only subset if more than 1 is left
        if len(o2_level) > 1:
            o2_level = o2_level[o2_level[0].str[i] == str(o2_mode)]
        if len(co2_level) > 1:
            co2_level = co2_level[co2_level[0].str[i] != str(co2_mode)]

    # clean from binary to base 10
    o2_level = int(o2_level.iloc[0,0], 2)
    co2_level = int(co2_level.iloc[0,0], 2)

    return o2_level, co2_level


if __name__ == '__main__':
    # part 1
    binary_nums = get_data()
    gamma, epsilon = part_1(binary_nums)

    print('*~*~*~*~*')
    print('Part 1:')
    print('Gamma:', gamma)
    print('Epsilon:', epsilon)
    print('Product:', gamma * epsilon)

    # part 2
    o2_level, co2_level = part_2(binary_nums)

    print('*~*~*~*~*')
    print('Part 2:')
    print('O2 level:', o2_level)
    print('CO2 level:', co2_level)
    print('Product:', o2_level * co2_level)
