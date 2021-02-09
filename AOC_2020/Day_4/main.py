import re

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

def passport_validator_2():
    """ This function is for finding the answer to Part 2 """
    # Variable for storing the number of valid passports
    valid_passport_count = int(0)

    # Loops through each passport entry yielded from passport_parse
    for entry in passport_parse():

        # For the start of each loop, set each of these variables to False
        byr_check = False
        iyr_check = False
        eyr_check = False
        hgt_check = False
        hcl_check = False
        ecl_check = False
        pid_check = False

        # Checks byr, iyr, eyr to see if they fall within the needed integer range and that they each contain 4 digits
        if entry.get('byr') != None and 1920 <= int(entry.get('byr')) <= 2002 and len(str(entry.get('byr'))) == 4:
            byr_check = True

        if entry.get('iyr') != None and 2010 <= int(entry.get('iyr')) <= 2020 and len(str(entry.get('iyr'))) == 4:
            iyr_check = True

        if entry.get('eyr') != None and 2020 <= int(entry.get('eyr')) <= 2030 and len(str(entry.get('eyr'))) == 4:
            eyr_check = True

        # Checks if hgt entry ends with 'cm', then checks if the integer falls within the wanted range
        if entry.get('hgt') != None and entry.get('hgt').endswith('cm'):

            if 150 <= int(''.join(i for i in entry.get('hgt') if i.isdigit())) <= 193:
                hgt_check = True

        # Same with last if statement, except it checks if the entry ends with 'in'
        if entry.get('hgt') != None and entry.get('hgt').endswith('in'):

            if 59 <= int(''.join(i for i in entry.get('hgt') if i.isdigit())) <= 76:
                hgt_check = True

        # Checks if the length of hcl entry is 7 and if the first character is a #
        if entry.get('hcl') != None and len(entry.get('hcl')) == 7 and entry.get('hcl')[0] == '#':
            
            # Using regex, search if every character after the first is either a digit, or a letter between a and f
            if not bool(re.compile(r'[^0-9a-f.]').search(entry.get('hcl')[1:])):
                hcl_check = True

        # Checks if ecl entry is one of the listed options
        if entry.get('ecl') != None and entry.get('ecl') in 'amb blu brn gry grn hzl oth'.split(' '):
            ecl_check = True

        # Checks if pid only contains 9 digits
        if entry.get('pid') != None and entry.get('pid').isdigit() and len(str(entry.get('pid'))) == 9:
            pid_check = True

        # If every check was set to True, increment valid_passport_count by 1
        if byr_check and iyr_check and eyr_check and hgt_check and hcl_check and ecl_check and pid_check:
            valid_passport_count += 1

    return f"The number of valid passports for Part 2 is {valid_passport_count}"



print(passport_validator_2())