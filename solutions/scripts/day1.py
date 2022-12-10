from typing import List

from solutions.inputs.utils import AoCInput, day


def decrease_resolution(depths: AoCInput, factor: int) -> List[int]:
    return [sum(int(d) for d in depths[k : k + factor]) for k in range(len(depths))]


def get_depth_increase_positions(depths_unresolved: AoCInput, resolution: int = 1) -> List[int]:
    depths = decrease_resolution(depths_unresolved, resolution)
    return [prev_ix + 1 for prev_ix, depth in enumerate(depths[1:]) if depth > depths[prev_ix]]


# Tests
test_depths: AoCInput = day(1, test=True)
assert len(get_depth_increase_positions(test_depths)) == 7
assert len(get_depth_increase_positions(test_depths, resolution=3)) == 5

print("Part 1: ", len(get_depth_increase_positions(day(1))))
print("Part 1: ", len(get_depth_increase_positions(day(1), resolution=3)))
