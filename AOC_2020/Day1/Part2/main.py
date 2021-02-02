import math

with open("AOC_2020\\Day1\\Part2\\inputD1P2.txt", 'r') as f:
    dt = f.read().replace("\n", " ").split()


def find_sum():

<<<<<<< HEAD
    # Nested loop for for three sets to find 3 numbers that sum to 2020 and print the product
=======

>>>>>>> 3a5268b712c19a4336be675ba9e9091bd32001fb
    for x in dt:
        for y in dt:
            for z in dt:
                x = int(x)
                y = int(y)
                z = int(z)
                sum = x + y + z

                if sum == 2020:
                    return f"The three numbers that sum to {sum} are: {x}, {y}, and {z}; and their product is {x * y * z}"


print(find_sum())