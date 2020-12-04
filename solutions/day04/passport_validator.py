import re


class PassportValidator:

    @staticmethod
    def contains_all_fields(passport):
        required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        return all([field in passport for field in required_fields])

    @staticmethod
    def all_fields_have_correct_values(passport):
        return PassportValidator.__validate_birth_year(passport) and \
               PassportValidator.__validate_issue_year(passport) and \
               PassportValidator.__validate_expiration_year(passport) and \
               PassportValidator.__validate_height(passport) and \
               PassportValidator.__validate_hair_color(passport) and \
               PassportValidator.__validate_eye_color(passport) and \
               PassportValidator.__validate_passport_id(passport)

    @staticmethod
    def __validate_year_in_passport(passport, field_name, lower_bound, upper_bound):
        if re.match(r"^[0-9]+$", passport[field_name]):
            return lower_bound <= int(passport[field_name]) <= upper_bound
        return False

    @staticmethod
    def __validate_birth_year(passport):
        return PassportValidator.__validate_year_in_passport(passport, "byr", 1920, 2002)

    @staticmethod
    def __validate_issue_year(passport):
        return PassportValidator.__validate_year_in_passport(passport, "iyr", 2010, 2020)

    @staticmethod
    def __validate_expiration_year(passport):
        return PassportValidator.__validate_year_in_passport(passport, "eyr", 2020, 2030)

    @staticmethod
    def __validate_height(passport):
        if re.match(r"^[0-9]{3}cm$", passport["hgt"]):
            return 150 <= int(re.sub(r"[^0-9]", "", passport["hgt"])) <= 193
        elif re.match(r"^[0-9]{2}in$", passport["hgt"]):
            return 59 <= int(re.sub(r"[^0-9]", "", passport["hgt"])) <= 76
        return False

    @staticmethod
    def __validate_hair_color(passport):
        return True if re.match(r"^#[0-9a-f]{6}$", passport["hcl"]) else False

    @staticmethod
    def __validate_eye_color(passport):
        return passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    @staticmethod
    def __validate_passport_id(passport):
        return True if re.match(r"^[0-9]{9}$", passport["pid"]) else False
