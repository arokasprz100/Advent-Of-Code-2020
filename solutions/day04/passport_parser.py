import re


class PassportParser:

    @staticmethod
    def create_passport_dictionary(passport_str):
        pairs = [PassportParser.__split_into_key_value(part) for part in re.split('[\n ]', passport_str)]
        return {pair[0]: pair[1] for pair in pairs}

    @staticmethod
    def __split_into_key_value(key_value_str):
        parts = re.split(':', key_value_str)
        return parts[0], parts[1]
