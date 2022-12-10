from typing import Tuple, TypeAlias

from solutions.inputs.utils import AoCInput, day

Coord: TypeAlias = Tuple[int, int, int]  # (x_pos, y_pos, aim)


def update_position(cur_position: Coord, dx: int, dy: int, da: int) -> Coord:
    return (cur_position[0] + dx, cur_position[1] + dy, cur_position[2] + da)


def plot_course(course_steps: AoCInput, use_aim: bool = False) -> int:
    sub_pos = (0, 0, 0)
    for step in course_steps:
        dx, dy, da = 0, 0, 0
        match step.split():
            case ["forward", dist]:
                dx, dy = int(dist), use_aim * sub_pos[-1] * int(dist)
            case ["down", dist]:
                dy, da = (1 - use_aim) * int(dist), int(dist)
            case ["up", dist]:
                dy, da = (use_aim - 1) * int(dist), -int(dist)
        sub_pos = update_position(sub_pos, dx, dy, da)
    return sub_pos[0] * sub_pos[1]


# Tests
test_course = day(2, test=True)
assert plot_course(test_course) == 150
assert plot_course(test_course, use_aim=True) == 900

print("Part 1: ", plot_course(day(2), use_aim=False))
print("Part 1: ", plot_course(day(2), use_aim=True))
