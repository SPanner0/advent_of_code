import math

with open("AOC_2020\\Day2\\input.txt", 'r') as f:
    dt = f.read().split('\n')


def validate_password():


    valid_pw_count = 0


    for el in dt:
        el = el.replace('-', ' ').replace(': ', ' ').split(' ')
        
        pass_dict = {
            "char_min" : int(el[0]),
            "char_max" : int(el[1]),
            "character" : str(el[2]),
            "password" : str(el[3])
        }

        if pass_dict.get("char_min") <= pass_dict.get("password").count(pass_dict.get("character")) <= pass_dict.get("char_max"):
            valid_pw_count += 1

    return f"There are a total of {valid_pw_count} valid passwords"


print(validate_password())

