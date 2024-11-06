# Spreadsheet Calculator

A Python-based spreadsheet calculator that reads cell expressions from a CSV file, evaluates their values in Reverse Polish Notation (RPN), and outputs the evaluated results in a specified format.

## Features
- Supports integer values and expressions in RPN format.Also supports increment and decrement operators
- Detects cyclic dependencies among cell references.
- Outputs each cell's final value formatted to five decimal places.

## Requirements
- Python 3.x
- `pytest` for running unit tests

## Installation
1. Clone the repository.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt

## Test 
To run test : 
   ```bash
   pytest -v tests/