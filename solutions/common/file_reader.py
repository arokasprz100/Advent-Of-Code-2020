
class FileReader:

    @staticmethod
    def to_line_list(file_path):
        with open(file_path) as input_file:
            file_content = input_file.read().splitlines()
        return file_content

    @staticmethod
    def to_string(file_path):
        with open(file_path) as input_file:
            file_content = input_file.read()
        return file_content
