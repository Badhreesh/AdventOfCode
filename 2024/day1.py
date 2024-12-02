from collections import Counter

from utils import Input, get_input

data = get_input(year=2024, day=1, _input=Input.GIVEN)

numbers = data.split()

# Part 1
list1 = sorted([int(number) for idx, number in enumerate(numbers) if idx % 2 == 0])

list2 = sorted([int(number) for idx, number in enumerate(numbers) if idx % 2 != 0])

total_distance = 0

for num1, num2 in zip(list1, list2):
    total_distance += abs(num1 - num2)

print(f"{total_distance=}")

# Part 2
list2_num_count = Counter(list2)

similarity_score = 0

for num in list1:
    similarity_score += num * list2_num_count[num]

print(f"{similarity_score=}")
