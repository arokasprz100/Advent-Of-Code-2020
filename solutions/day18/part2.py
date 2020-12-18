from solutions.common.file_reader import FileReader
from solutions.day18.math_expression_parser import MathExpressionParser

if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")
    operators_by_priority = {1: ['+'], 2: ['*']}
    expression_parser = MathExpressionParser(operators_by_priority)
    parsed_expressions = list(map(lambda line: expression_parser.parse(line), puzzle_input))
    evaluated_expressions = list(map(lambda expression: expression.evaluate(), parsed_expressions))
    print("[PART 2] Sum of expressions evaluation results: {}".format(sum(evaluated_expressions)))
