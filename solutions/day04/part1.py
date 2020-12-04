from solutions.common.file_reader import FileReader
from solutions.day04.passport_validator import PassportValidator
from solutions.day04.passport_parser import PassportParser

if __name__ == '__main__':
    puzzle_input = FileReader.to_string("input.txt")
    passports = [PassportParser.create_passport_dictionary(passport_str) for passport_str in puzzle_input.split("\n\n")]
    valid_passports = sum([PassportValidator.contains_all_fields(passport) for passport in passports])
    print("There are {} valid passports".format(valid_passports))
