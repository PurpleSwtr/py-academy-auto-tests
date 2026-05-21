from typing import Union


def find_median(numbers) -> Union[int, float]:
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)

    if n % 2 == 1:
        mid_index = n // 2
        return float(sorted_nums[mid_index])
    else:
        mid_right = n // 2
        mid_left = mid_right - 1
        return (sorted_nums[mid_left] + sorted_nums[mid_right]) / 2


def select_format(num: Union[int, float]):
    if num.is_integer():
        return int(num)
    else:
        return round(num, 1)


input_list = list(map(int, input().strip().split()))

median = find_median(input_list)
print(select_format(median))
