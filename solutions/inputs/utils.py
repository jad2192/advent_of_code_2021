from typing import List, TypeAlias

AoCInput: TypeAlias = List[str]


def day(day_number: int, test: bool = False, split_char: str = "\n") -> AoCInput:
    fp = f"solutions/inputs/day{day_number}.txt" if not test else f"solutions/inputs/day{day_number}_test.txt"
    return open(fp).read().split(split_char)
