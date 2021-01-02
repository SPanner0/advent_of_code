import math
import random
from key import nums

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