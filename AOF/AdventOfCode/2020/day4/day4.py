from dotenv import load_dotenv
import os
import re
 
load_dotenv()
FILE_PATH = os.getenv('FILE_PATH')
FILE_PATH_DEBUG = os.getenv('FILE_PATH_DEBUG')

def get_data():
    with open(FILE_PATH) as f:
        return f.read()

def isValidField(field, value): #or maybe use match-case for newer python versions
    if field =="byr":
        return len(value) == 4 and 1920 <= int(value) <= 2002
    
    if field =="iyr":
        return len(value) == 4 and 2010 <= int(value) <= 2020
    
    if field =="eyr":
        return len(value) == 4 and 2020 <= int(value) <= 2030
    
    if field =="hgt":
        if 'cm' not in value and 'in' not in value:
            return False
        num, unit = int(value[:-2]), value[-2:]        
        if unit == 'cm':
            return 150 <= num <= 193
        if unit == 'in':
            return 59 <= num <= 76
        
    if field =="hcl":
        hex_regex = re.compile(r"^[0-9a-fA-F]{6}$")
        if value[0] != '#':
            return False

        hair_color = value[1:]
        return hex_regex.match(hair_color)

    if field =="ecl":
        return value in ['amb', 'blu', 'brn', 'gry', 'grn','hzl','oth']
    
    if field =="pid":
        if len(value) == 9 and (value.isdigit()):
            return True
    if field =="cid":
        return True
    

def isValidPassport(pass_fields, REQUIRED_FIELDS, valid_passports):
    if len(pass_fields) == len(REQUIRED_FIELDS):
        valid_passports +=1
    if 'cid' not in pass_fields and len(pass_fields) == (len(REQUIRED_FIELDS)-1):
        valid_passports +=1

    return valid_passports

def part2(passports, REQUIRED_FIELDS):
    pass_fields = []
    valid_passports = 0
    for passport in passports:
        pass_fields = []
        passport=passport.split()
        for line in passport:
            field, value = line.split(":")
            if isValidField(field, value):
                pass_fields.append(field)

        valid_passports =isValidPassport(pass_fields, REQUIRED_FIELDS, valid_passports)

    return(valid_passports)

def part1(passports, REQUIRED_FIELDS):
    pass_fields = []
    valid_passports = 0
    for passport in passports:
        pass_fields = []
        passport=passport.split()
        for line in passport:
            field = line.split(":")[0]
            pass_fields.append(field)

        valid_passports =isValidPassport(pass_fields, REQUIRED_FIELDS, valid_passports)

    return(valid_passports)

def main():
   data = get_data()   
   passports=data.split('\n\n')
   REQUIRED_FIELDS= ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
   #num_of_valid_passportsJ=part1(passports, REQUIRED_FIELDS)
   num_of_valid_passportsJ = part2(passports, REQUIRED_FIELDS)
   print(num_of_valid_passportsJ)


if __name__ == "__main__":
    main()