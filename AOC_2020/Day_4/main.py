with open("AOC_2020\\Day_4\\input.txt") as f:
    dt = f.read()

# Contains a list of each passport and a list of each passport fields that exists, respectively
passport_list = dt.split('\n\n')
passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

def passport_parse():
    """ This function takes each passport in passport_list and parses them from a string to a dict, with empty keys containing None """

    passport_dict = {}

    # Iterates through each passport in passport_list
    for passport in passport_list:

        # Splits each passport into it's component parts; like ['eyr', '2021', 'byr', '2003', ...]
        passport = passport.replace(':', ' ').replace('\n', ' ').split(' ')


        # Runs through each field in the specified global variable passport_fields
        for field in passport_fields:
            
            # Checks if each passport contains the field and convert it to a key
            # If the field is in the passport, enter the value of the index one above the field name in the passport
            # Otherwise, enter None as the value of that key
            if field in passport:
                passport_dict[field] = passport[passport.index(field) + 1]
            else:
                passport_dict[field] = None

        # yield each parsed passport dictionary, ready to be retrieved using a for loop
        yield passport_dict


def passport_validator():
    """ Validator for Part 1. It checks if each key has a value other than None, ignoring the 'cid' key """
    valid_passport_count = int(0)

    for entry in passport_parse():

        # Deletes the 'cid' key because it will be ignored
        del entry['cid']

        # Checks if all the values of each key is not None, increment valid_passport_count by 1 if this condition is met
        if all(entry.get(value) != None for value in entry):
            valid_passport_count += 1
    
    return valid_passport_count

print(passport_validator())