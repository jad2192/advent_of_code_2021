from functools import reduce
from typing import Literal, Tuple

from solutions.inputs.utils import AoCInput, day


def gamma_pos(positional_bits) -> Literal[0, 1]:
    return int(2 * sum(int(bit) for bit in positional_bits) >= len(positional_bits))


def get_gamma_and_epsilon(report: AoCInput) -> Tuple[int, int]:
    positional_binaries = list(zip(*report))
    gamma, epsilon = [], []
    for bin_col in positional_binaries:
        gamma_k = gamma_pos(bin_col)
        gamma.append(str(gamma_k))
        epsilon.append(str((gamma_k + 1) % 2))
    return int("".join(gamma), 2), int("".join(epsilon), 2)


def get_life_support_rating(report: AoCInput) -> int:
    o2_gen, co2_gen = report, report
    pos_bits_o2, pos_bits_co2 = list(zip(*o2_gen)), list(zip(*co2_gen))
    k = 0
    while len(o2_gen) > 1 or len(co2_gen) > 1:
        gamma_o2, gamma_co2 = str(gamma_pos(pos_bits_o2[k])), str(gamma_pos(pos_bits_co2[k]))
        o2_gen = [b for b in o2_gen if b[k] == gamma_o2] if len(o2_gen) > 1 else o2_gen
        co2_gen = [b for b in co2_gen if b[k] != gamma_co2] if len(co2_gen) > 1 else co2_gen
        pos_bits_o2, pos_bits_co2 = list(zip(*o2_gen)), list(zip(*co2_gen))
        k += 1
    return int(o2_gen[0], 2) * int(co2_gen[0], 2)


# Tests
test_report = day(3, test=True)
test_gamma, test_epsilon = get_gamma_and_epsilon(test_report)
assert (test_gamma, test_epsilon) == (22, 9)
assert get_life_support_rating(test_report) == 230

diagnostic_report = day(3, test=False)
print("Part 1: ", reduce(lambda g, e: g * e, get_gamma_and_epsilon(diagnostic_report)))
print("Part 2: ", get_life_support_rating(diagnostic_report))
