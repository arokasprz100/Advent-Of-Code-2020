from solutions.day18.expression_tree import Number, Addition, Multiplication


class MathExpressionParser:

    def __init__(self, operators_by_priorities):
        self.operators_by_priorities = operators_by_priorities
        self.__operations_by_operators = {
            '+': Addition,
            '*': Multiplication
        }

    def parse(self, expression):
        expression_parts = self.__split_expression_into_parts_at_same_level(expression)
        expression_parts = self.__parse_digits_and_parenthesis_enclosed_operations(expression_parts)
        for priority in self.operators_by_priorities.keys():
            expression_parts = self.__parse_operations_with_given_priority(expression_parts, priority)
        return expression_parts[0]

    def __parse_digits_and_parenthesis_enclosed_operations(self, expression_parts):
        for index, part in enumerate(expression_parts):
            if part.startswith('('):
                expression_parts[index] = self.parse(part[1:-1])
            elif part.isdigit():
                expression_parts[index] = Number(int(part))
        return expression_parts

    def __parse_operations_with_given_priority(self, expression_parts, priority):
        while current_operation := self.__get_next_operation_with_given_priority(expression_parts, priority):
            rhs = expression_parts.pop(current_operation[0] + 1)
            lhs = expression_parts.pop(current_operation[0] - 1)
            op = self.__operations_by_operators[current_operation[1]](rhs, lhs)
            expression_parts[current_operation[0] - 1] = op
        return expression_parts

    def __get_next_operation_with_given_priority(self, expression_parts, priority):
        return next(iter(item for item in enumerate(expression_parts)
                         if item[1] in self.operators_by_priorities[priority]), None)

    @classmethod
    def __extract_expression_withing_parenthesis(cls, expression):
        counter = 0
        for index, character in enumerate(expression):
            if character == '(':
                counter += 1
            elif character == ')':
                counter -= 1
            if counter == 0:
                return expression[:index + 1].strip(), expression[index + 1:].strip()

    @classmethod
    def __split_expression_into_parts_at_same_level(cls, expression):
        expression_parts = []
        while expression:
            if expression.startswith("("):
                part, expression = cls.__extract_expression_withing_parenthesis(expression)
                expression_parts.append(part)
            elif " " in expression:
                part, expression = tuple(map(lambda x: x.strip(), expression.split(" ", 1)))
                expression_parts.append(part)
            else:
                expression_parts.append(expression)
                expression = ""
        return expression_parts
