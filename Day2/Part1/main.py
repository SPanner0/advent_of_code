import math
import re

file = open("input.txt", "r")
pws = file.read().replace("-", "\n").split("\n")

nums = []
for t in pws:
    try:
        nums.append(int(t))
    except ValueError:
        pass

x = 0
while x <= 500:
    min = 2 * x
    print(min)
    x += 1

y = 0
while y <= 500:
    max = 1 + (2 * y)
    print(max)
    y += 1

target = re.findall