INFILE_CALLS = 'input/day_4_calls.txt'
INFILE_BOARDS = 'input/day_4_boards.txt'
# INFILE_CALLS = 'input/test_calls.txt'
# INFILE_BOARDS = 'input/test_boards.txt'


def get_calls():
    with open(INFILE_CALLS) as infile:
        text = infile.read()

    calls = text.split(',')

    return calls


def get_boards():
    with open(INFILE_BOARDS) as infile:
        text = infile.read()

    lines = text.split('\n')

    boards = []
    states = []
    this_board = []
    this_state = []
    counter = 1
    for line in lines:
        if (counter % 6) > 0:
            line = line.split(' ')
            try:
                while True:
                    line.remove('')
            except ValueError:
                pass
            this_board.append(line)
            this_state.append([0,0,0,0,0])
        else:
            boards.append(this_board)
            states.append(this_state)
            this_board = []
            this_state = []
        counter += 1

    return boards, states


def make_call(call, boards, states):
    # takes a number to call, checks boards for that number and updates state
    for i in range(0, len(boards)):
        board = boards[i]
        state = states[i]
        # each board is 5 x 5
        for j in range(0, 5):
            for k in range(0, 5):
                if board[j][k] == call:
                    state[j][k] = 1
        states[i] = state

    return states


def check_row(row, state):
    total = sum(state[row])

    if total == 5:
        return True
    else:
        return False


def check_column(col, state):
    total = 0
    for row in range(0, 5):
        total += state[row][col]

    if total == 5:
        return True
    else:
        return False


def check_winner(boards, states):
    winner = False
    index = None

    # after a call is made, check for any five-in-a-row winner (no diags!)
    for i in range(0, len(states)):
        state = states[i]
        for row in range(0, 5):
            if check_row(row, state):
                winner = True
                index = i
                return winner, index

        for col in range(0, 5):
            if check_column(col, state):
                winner = True
                index = i
                return winner, index

    return winner, index


def play_bingo(calls, boards, states):
    # loop through calls until a we have a winner
    winner = False
    for call in calls:
        states = make_call(call, boards, states)
        winner, index = check_winner(boards, states)

        if winner:
            return index, call

    return False


def calculate_score(winning_call, board, state):
    score = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if state[i][j] == 0:
                score += int(board[i][j])

    score = score * int(winning_call)

    return score


if __name__ == '__main__':
    calls = get_calls()
    boards, states = get_boards()

    winning_index, winning_call = play_bingo(calls, boards, states)
    winning_board = boards[winning_index]
    winning_state = states[winning_index]

    score = calculate_score(winning_call, winning_board, winning_state)

    print('*~*~*~*~*')
    print('Winning call:', winning_call)

    print('*~*~*~*~*')
    print('Winning board:')
    for row in winning_board:
        print(row)

    print('*~*~*~*~*')
    print('Winning state:')
    for row in winning_state:
        print(row)

    print('*~*~*~*~*')
    print('Final score:', score)
