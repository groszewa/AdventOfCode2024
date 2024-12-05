import numpy as np
import re

test_matrix = [['a','b','c'],['d','e','f'],['g','h','i']]

def get_diags(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    diags = []
    for i in range(num_rows):
        diag = []
        for j in range(i+1):
            row_idx = i-j
            col_idx = j
            diag.append(matrix[row_idx][col_idx])
        diags.append(diag)
    for i in range(num_rows-2,-1,-1):
        diag = []
        for j in range(i+1):
            row_idx = i-j
            col_idx = j
            diag.append(matrix[num_rows-col_idx-1][num_cols-row_idx-1])
        diags.append(diag)
    return diags

def main():
    with open('input.txt','r') as file:
        matrix = []
        for line in file:
            row = []
            for ch in line.strip():
                row.append(ch)
            matrix.append(row)
        #matrix = test_matrix
        #print("grid:")
        #for row in matrix:
        #    print(row)
        matrix_rev = matrix.copy()
        matrix_rev.reverse()
        #print("grid_rev:")
        #for row in matrix_rev:
        #    print(row)
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        rows  = matrix
        #print("rows:")
        #print(rows)
        cols = []
        for col_idx in range(num_cols):
            col = []
            for row_idx in range(num_rows):
                col.append(matrix[row_idx][col_idx])
            cols.append(col)
        #print("cols:")
        #print(cols)
        diags1 = get_diags(matrix)
        #print("diags1:")
        #print(diags1)
        diags2 = get_diags(matrix_rev)
        #print("diags2:")
        #print(diags2)
        search_list = []
        for row in rows:
            search_list.append(''.join(row))
        for col in cols:
            search_list.append(''.join(col))
        for diag in diags1:
            search_list.append(''.join(diag))
        for diag in diags2:
            search_list.append(''.join(diag))
        print(search_list)
        count = 0
        for item in search_list:
            count += len(re.findall('XMAS', item))
            count += len(re.findall('SAMX', item))
        print(f'Total occurences of XMAS = {count}')


if __name__ == '__main__':
    main()
