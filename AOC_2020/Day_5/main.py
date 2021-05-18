import math



def read():
    """Reads the data from the input file and splits it into a list on line breaks."""

    with open("AOC_2020\\Day_5\\input.txt") as f:
        dt = f.read().split("\n")

    return dt


def process_code(seat_code):
    """Function to get the answer to Part 1."""

    # Test ID: FBFBBFFRLR

    def process_rows(seat_code):
        row_letters = seat_code[:7]
        row_number = [0, 127]

        for letter in row_letters:
            if letter == "F":
                row_number = [row_number[0], row_number[0] + math.floor((row_number[1] - row_number[0]) / 2)]
            elif letter == "B":
                row_number = [row_number[1] - math.floor((row_number[1] - row_number[0]) / 2), row_number[1]]
            else:
                raise Exception(f"Unexpected character detected: {letter}.")

        if row_number[0] == row_number[1]:
            row_number = row_number[0]
        else:
            raise Exception(f"Did not receive expected outcome: Unable to narrow {id}'s row number down to one number.")

        return row_number


    def process_columns(seat_code):
        column_letters = seat_code[-3:]
        column_number = [0, 7]

        for letter in column_letters:
            if letter == "L":
                column_number = [column_number[0], column_number[0] + math.floor((column_number[1] - column_number[0]) / 2)]
            elif letter == "R":
                column_number = [column_number[1] - math.floor((column_number[1] - column_number[0]) / 2), column_number[1]]
            else:
                raise Exception(f"Unexpected character detected: {letter}.")

        if column_number[0] == column_number[1]:
                column_number = column_number[0]
        else:
            raise Exception(f"Did not receive expected outcome: Unable to narrow {id}'s column number down to one number.")

        return column_number

    
    def find_seat_id(seat_code):
        row_number = process_rows(seat_code)
        column_number = process_columns(seat_code)

        seat_id = (row_number * 8) + column_number

        return seat_id

    return find_seat_id(seat_code)

    
def part_1():

    highest_id = 0
    seat_codes = read()

    for seat_code in seat_codes:
        current_id = process_code(seat_code)

        if current_id > highest_id:
            highest_id = current_id

    print(highest_id)


part_1()


def part_2():

    id_list = []
    seat_codes = read()

    for seat_code in seat_codes:
        current_id = process_code(seat_code)
        id_list.append(current_id)

    id_list = sorted(id_list)
    complete_list = []
    
    for x in range(min(id_list), max(id_list)):
        complete_list.append(x)

    my_id = set(complete_list) - set(id_list)

    print(my_id)

part_2()