class ExpressionEvaluator:
    def __init__(self, spreadsheet):
        self.spreadsheet = spreadsheet

    def evaluate_expression(self, expression):
        stack = []
        tokens = expression.split()
        operator_map = {
            '++': lambda x: x + 1,
            '--': lambda x: x - 1,
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }
        for token in tokens:
            if token.isdigit():
                stack.append(float(token))
            elif token in operator_map:
                if token in ('++', '--'):
                    stack.append(operator_map[token](stack.pop()))
                else:
                    b, a = stack.pop(), stack.pop()
                    stack.append(operator_map[token](a, b))
            else:
                referenced_value = self.spreadsheet.evaluate_cell(self.spreadsheet.cells[token])
                stack.append(referenced_value)

        return stack.pop()
