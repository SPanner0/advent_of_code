import math
import random

file = open('inputD1P1.txt')
nums = file.read().replace("\n", " ").split()
file.close()

num_1 = nums
num_2 = nums
x = random.choice(num_1)
y = random.choice(num_2)
sum = x + y

while sum != 2020:
    x = random.choice(num_1)
    y = random.choice(num_2)
    sum = x + y
    print(str(x), '+', str(y), '=', str(sum))