from typing import List

# Load data
DATA = []

with open('day_01/data.txt', 'r') as f:
    elf_calories = []
    for line in f:
        try:
            elf_calories.append(int(line))
        except ValueError:
            DATA.append(elf_calories)
            elf_calories = []
            continue


def sorted_sums(calories_list: List[List[int]]) -> List[int]:

    calories_sums = [sum(x) for x in calories_list]

    return sorted(calories_sums, reverse=True)


if __name__ == '__main__':
    print(sum(sorted_sums(DATA)[:1]))
    print(sum(sorted_sums(DATA)[:3]))
