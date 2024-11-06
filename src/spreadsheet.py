from src import ExpressionEvaluator


class Cell:
    def __init__(self, reference, expression):
        self.reference = reference
        self.expression = expression
        self.value = None
        self.evaluating = False


class Spreadsheet:
    def __init__(self, width, height, cells):
        self.width = width
        self.height = height
        self.cells = self._initialize_cells(cells)
        self.evaluator = ExpressionEvaluator(self)

    def _initialize_cells(self, cells):
        cell_dict = {}
        for i, expression in enumerate(cells):
            row = chr(65 + (i // self.width))
            col = str((i % self.width) + 1)
            cell_dict[f"{row}{col}"] = Cell(f"{row}{col}", expression)
        return cell_dict

    def evaluate(self):
        for cell in self.cells.values():
            self.evaluate_cell(cell)
        return [f"{cell.value:.5f}" for cell in self.cells.values()]

    def evaluate_cell(self, cell):
        if cell.value is not None:
            return cell.value
        if cell.evaluating:
            raise Exception(f"Cyclic dependency detected at {cell.reference}")
        cell.evaluating = True
        cell.value = self.evaluator.evaluate_expression(cell.expression)
        cell.evaluating = False
        return cell.value
