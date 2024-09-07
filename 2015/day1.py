from collections import Counter

from utils import Input, get_input

_input = get_input(year=2015, day=1, _input=Input.GIVEN)

parenthesis_count = Counter(_input)

p1 = parenthesis_count["("] - parenthesis_count[")"]
print(p1)

floor = 0
for idx, parenthesis in enumerate(_input):
    value = 1 if parenthesis == "(" else -1
    floor += value
    if floor == -1:
        p2 = idx + 1
        break

print(p2)
