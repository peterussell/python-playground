from typing import List

def multiply_by_2(li: List[int]) -> List[int]:
    new_list: List[int] = []
    for item in li:
        new_list.append(item * 2)

    return new_list

print(multiply_by_2([1,2,3,4,5]))