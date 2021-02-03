import math

# Reads input from txt file
with open('AOC_2020\\Day_1\\input.txt', 'r') as f:
    dt = f.read().split('\n')


def find_two_to_sum():

# Nested loop to check through every pair of numbers

    for i in dt:
        for u in dt:
            i = int(i)
            u = int(u)

            if i + u == 2020:
                return f"{i} and {u} add up to make {i + u}, and their product is {i * u}"

print(find_two_to_sum())



def find_three_to_sum():

    # Nested loop for for three sets to find 3 numbers that sum to 2020 and print the product
    for x in dt:
        for y in dt:
            for z in dt:
                x = int(x)
                y = int(y)
                z = int(z)
                sum = x + y + z

                if sum == 2020:
                    return f"The three numbers that sum to {sum} are: {x}, {y}, and {z}; and their product is {x * y * z}"


print(find_three_to_sum())
