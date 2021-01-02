import math

file = open('key.txt')
nums = file.read().replace("\n", " ").split()
file.close()

while sum != 2020:
    for x in nums:
        for y in nums:
                for z in nums:
                    sum = int(x) + int(y) + int(z)    

                    if sum == 2020:           
                        print(x, "+", y, "+", z, "=", sum)
                        print("Product =", int(x)*int(y)*int(z))
                        break