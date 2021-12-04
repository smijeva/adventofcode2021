class BingoNumber:
    def __init__(self, number):
        self.number = number
        self.marked = False

    def mark_number(self):
        self.marked = True


class BingoBoard:
    def __init__(self, board):
        self.board = [[BingoNumber(num) for num in row] for row in board]
        self.board_size = len(board)
        self.has_won = False
        self.winning_call = None

    def mark_number(self, called_number):
        if self.has_won:
            return False

        for row in self.board:
            for bn in row:
                if called_number == bn.number:
                    bn.mark_number()

        if self.is_winning():
            self.has_won = True
            self.winning_call = called_number

        return True

    def is_winning(self):
        for i in range(self.board_size):
            if all([self.board[i][j].marked for j in range(self.board_size)]) \
                    or all([self.board[j][i].marked for j in range(self.board_size)]):
                return True
        return False


def find_winning_board(calls, boards):
    for call in calls:
        for board in boards:
            board.mark_number(call)
            if board.is_winning():
                return call, board


def find_losing_board(calls, boards):
    last_board = None
    for call in calls:
        for board in boards:
            if board.mark_number(call) is True:
                last_board = board
        if all([board.is_winning() for board in boards]):
            return call, last_board


def parse_bingo():
    with open("input4.txt") as file:
        calls = [int(num) for num in file.readline().split(",")]
        boards = []
        while True:
            line = file.readline()
            if not line:
                break

            board = [[int(num) for num in file.readline().split()] for _ in range(5)]
            boards.append(BingoBoard(board))
    return boards, calls


def part1():
    boards, calls = parse_bingo()

    winning_call, winning_board = find_winning_board(calls, boards)
    flat_board = [j for sub in winning_board.board for j in sub]
    unmarked_numbers = [bn.number for bn in flat_board if bn.marked is False]

    return sum(unmarked_numbers) * winning_call


def part2():
    boards, calls = parse_bingo()

    losing_call, losing_board = find_losing_board(calls, boards)
    flat_board = [j for sub in losing_board.board for j in sub]
    unmarked_numbers = [bn.number for bn in flat_board if bn.marked is False]

    return sum(unmarked_numbers) * losing_call


print(part1())
print(part2())
