import math
import random

file_path = "AOC_2020\\"

with open(f'{file_path}Day1\\Part1\\inputD1P1.txt', 'r') as f:
    nums = f.read().split('\n')

num_1 = nums[:]
num_2 = nums[:]


def find_sum():


    for i in num_1:
        for u in num_2:
            i = int(i)
            u = int(u)

            if i + u == 2020:
                return f"{i} and {u} add up to make {i + u}, and their product is {i * u}"

print(find_sum())
