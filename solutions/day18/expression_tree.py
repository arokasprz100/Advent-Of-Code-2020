from abc import ABC, abstractmethod


class ExpressionTreeNode(ABC):

    @abstractmethod
    def evaluate(self):
        pass


class Number(ExpressionTreeNode):

    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

    def __str__(self):
        return "Number({})".format(self.value)


class Addition(ExpressionTreeNode):

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self):
        return self.lhs.evaluate() + self.rhs.evaluate()

    def __str__(self):
        return "Addition({} + {})".format(str(self.lhs), str(self.rhs))


class Multiplication(ExpressionTreeNode):

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self):
        return self.lhs.evaluate() * self.rhs.evaluate()

    def __str__(self):
        return "Multiplication({} * {})".format(str(self.lhs), str(self.rhs))

