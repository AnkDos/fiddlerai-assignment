import sys
from src import Spreadsheet


def main():
    try:
        input_data = sys.stdin.read().strip().splitlines()
        width, height = map(int, input_data[0].split())
        cells = input_data[1:]
        spreadsheet = Spreadsheet(width, height, cells)
        output = spreadsheet.evaluate()
        print("\n".join(output))
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
