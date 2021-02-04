with open("AOC_2020\\Day_3\\input.txt", 'r') as f:
    dt = f.read().split('\n')


def count_trees():

    # Stores the current grid index and the current number of trees in encountered, respectively
    grid_index = int(0)
    tree_count = int(0)

    # Checks for each row...
    for row in dt:

        # If a tree (represented by a '#') was encountered, increment tree_count by 1
        if row[grid_index] == '#':
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


def tree_slopes(right_steps: int, down_steps: int) -> int:
    """ A more dynamic version of the count_trees function, allowing for different slopes """
    grid_index = int(0)
    tree_count = int(0)

    # Iterates for each row, and takes in the wanted number of steps to skip
    for row in dt[::down_steps]:

        if row[grid_index] == '#':
            tree_count += 1

        # Slightly different from the count_trees function; now iterates by the passed in right_step no matter what
        grid_index += right_steps
        
        # Checks if, after previous iteration, whether grid_index exceeds 30, resets and counts back from index 0 if conditon met
        if grid_index > 30:
            grid_index = grid_index - 31

    return int(tree_count)


def trees_product():
    """ Receives all the output from tree_slopes and outputs the product """
    product = tree_slopes(1, 1) * tree_slopes(3, 1) * tree_slopes(5, 1) * tree_slopes(7, 1) * tree_slopes(1, 2)

    return f"The product of all the trees encountered on each slope is: {product}"

print(trees_product())