from typing import List
from re import match
def can_sum(target_sum: int, numbers: List[int]) -> bool:
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for number in numbers:
        remainder: int = target_sum - number
        is_sum = can_sum(remainder, numbers)
        if is_sum:
            return True
    return False
def can_sum_mem(target_sum: int, numbers: List[int], memo = {0: True}) -> bool:
    if target_sum in memo:
        return memo[target_sum]
    if target_sum < 0:
        return False
    for number in numbers:
        remainder = target_sum - number
        is_can_sum = can_sum_mem(remainder, numbers, memo)
        if is_can_sum:
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False

def main() -> None:
    numbers: int  = [7, 14]
    target_number: int = 300

    is_can_sum: bool = can_sum_mem(target_number, numbers)
    print(is_can_sum)

if __name__ == "__main__":
    main()