import math

with open("AOC_2020\\Day_2\\input.txt", 'r') as f:
    dt = f.read().split('\n')


def validate_password():

    # Variable to store the number of valid passwords
    valid_pw_count = 0

    # Initial parsing for each element in the list, splitting each information and passing them into a dictionary
    for el in dt:
        el = el.replace('-', ' ').replace(': ', ' ').split(' ')
        
        pass_dict = {
            "char_min" : int(el[0]),
            "char_max" : int(el[1]),
            "character" : str(el[2]),
            "password" : str(el[3])
        }

        # Checks whether or not a password is valid for each entry
        if pass_dict.get("char_min") <= pass_dict.get("password").count(pass_dict.get("character")) <= pass_dict.get("char_max"):
            valid_pw_count += 1

    # Prints out result
    return f"There are a total of {valid_pw_count} valid passwords"


print(validate_password())



def validate_password_2():


    valid_pw_count = 0


    for el in dt:
        el = el.replace('-', ' ').replace(': ', ' ').split(' ')
        
        # Note: index starts at 1 for the challange as apposed to 0; hence the -1 for first_index and second_index
        pass_dict = {
            "first_index" : int(el[0]) - 1,
            "second_index" : int(el[1]) - 1,
            "character" : str(el[2]),
            "password" : str(el[3])
        }

        # Checks if at least one index contains the correct character; return True if that is the case, otherwise False
        def one_true():
            if pass_dict.get("password")[pass_dict.get("first_index")] == pass_dict.get("character") or pass_dict.get("password")[pass_dict.get("second_index")] == pass_dict.get("character"):
                return True
            else: 
                return False

        # Checks if BOTH indexes contain the correct character; return True if that is the case, otherwise False
        def both_true():
            if pass_dict.get("password")[pass_dict.get("first_index")] == pass_dict.get("character") and pass_dict.get("password")[pass_dict.get("second_index")] == pass_dict.get("character"):
                return True
            else:
                return False

        # Checks if one_true returns True and if both_true returns False; add one to valid_pw_count if these two conditions are met
        if one_true() is True and both_true() is False:
            valid_pw_count += 1

    # Returns the answer
    return f"There are a total of {valid_pw_count} valid passwords"


print(validate_password_2())