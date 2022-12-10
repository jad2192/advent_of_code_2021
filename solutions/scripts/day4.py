from typing import Dict, List, Set, Tuple, TypeAlias

from solutions.inputs.utils import AoCInput, day

BoardGrid: TypeAlias = Dict[int, Tuple[int, int]]
BoardState: TypeAlias = Dict[int, Set[int]]


class BingoBoard:
    def __init__(self, board_string: str):
        self.winning_state = False
        self.board_grid: BoardGrid = dict()
        self.row_state: BoardState = dict()
        self.col_state: BoardState = dict()
        for row_ix, row in enumerate(board_string.split("\n")):
            self.row_state[row_ix] = set()
            for col_ix, num in enumerate(row.split()):
                self.col_state[col_ix] = set()
                self.board_grid[int(num)] = (row_ix, col_ix)

    def update_state(self, called_number: int):
        if called_number in self.board_grid:
            row_ix, col_ix = self.board_grid[called_number]
            self.row_state[row_ix].add(called_number)
            self.col_state[col_ix].add(called_number)
            self.winning_state = (len(self.col_state[col_ix]) == 5) or (len(self.row_state[row_ix]) == 5)


def parse_input(input: AoCInput) -> Tuple[List[int], List[BingoBoard]]:
    call_order = [int(x) for x in input[0].split(",")]
    boards = [BingoBoard(board_string) for board_string in input[1:]]
    return call_order, boards


def play_squid_bingo(input: AoCInput, let_squid_win=False) -> int:
    call_order, bingo_boards = parse_input(input)
    called_numbers = []
    board_order = []
    stop_cond = len(bingo_boards) if let_squid_win else 1
    while len(board_order) < stop_cond:
        called_numbers.append(call_order.pop(0))
        for board in bingo_boards:
            if not board.winning_state:
                board.update_state(called_numbers[-1])
                if board.winning_state:
                    board_order.append(board)
    return called_numbers[-1] * sum(set(board_order[-1].board_grid).difference(called_numbers))


# Tests
test_input = day(4, test=True, split_char="\n\n")
assert play_squid_bingo(test_input) == 4512
assert play_squid_bingo(test_input, let_squid_win=True) == 1924


game_input = day(4, split_char="\n\n")
print("Part 1: ", play_squid_bingo(game_input))
print("Part 2: ", play_squid_bingo(game_input, let_squid_win=True))
