from typing import List
def can_sum(target_sum: int, numbers: List[int]) -> bool:
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for number in numbers:
        is_sum = can_sum(target_sum - number, numbers)
        if is_sum:
            return True
    return False

def main() -> None:
    numbers: int  = [2, 4]
    target_number: int = 7

    is_can_sum: bool = can_sum(target_number, numbers)
    print(is_can_sum)

if __name__ == "__main__":
    main()