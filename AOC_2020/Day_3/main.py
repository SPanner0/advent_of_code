with open("AOC_2020\\Day_3\\input.txt", 'r') as f:
    dt = f.read().split('\n')


def count_trees():

    # Stores the current grid index and the current number of trees in encountered, respectively
    grid_index = int(0)
    tree_count = int(0)

    # Checks for each row...
    for row in dt:

        # If a tree (represented by a '#') was encountered, increment tree_count by 1
        if row[grid_index] == "#":
            tree_count += 1

        # Increment the index to check the next row by 3 (3 to the right, and 1 down)
        if grid_index <= 27:
            grid_index += 3
        # If the current index is greater than 27, reset by subtracting current index by 28
        else:
            grid_index = grid_index - 28

    # Returns the answer
    return f"The number of trees that were encountered was {tree_count}"

print(count_trees())