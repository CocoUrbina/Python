# coding: utf8
# Copyright: MathDecision

from xlrd import open_workbook


def explore_excel(filepath, lines=3):
    wb = open_workbook(filepath)
    for s in wb.sheets():
        print('Sheet:',s.name)
        for row in range(min(s.nrows, lines)):
            col_values = []
            for col in range(s.ncols):
                col_values.append(str(s.cell(row,col).value))
            print('Row {}: '.format(row), ','.join(col_values))
        print('\n')


def explore_csv(filepath, lines=3):
    with open(filepath, 'r') as f:
        for _ in range(lines):
            print(f.readline())
