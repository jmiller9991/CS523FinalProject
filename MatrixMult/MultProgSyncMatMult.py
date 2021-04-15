# Jacob Miller
# 4/12/2021
# Project Code: Python's Built in Multiprogramming Library Synchronous Matrix Multiplication

import numpy as np
import multiprocessing
import cProfile

def matrixWork(offset, rows_to_send, matrix1, matrix2, final_matrix):
    for i in range(len(matrix1)):
        for j in range(0, rows_to_send+1):
            for k in range(len(matrix2)):
                final_matrix[i][j] += matrix1[i][k] * matrix2[k][offset]

    return final_matrix

def workMethod():
    matrix1 = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]])
    matrix2 = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45], [50, 55, 60], [65, 70, 75], [80, 85, 90]])
    final_matrix = np.zeros((3, 3))

    # Expected Results:
    # [1155, 1260, 1365]
    # [2685, 2970, 3255]
    # [4215, 4680, 5145]

    print('Matrix 1:')
    print(matrix1)
    print('\n')

    print('Matrix 2:')
    print(matrix2)
    print('\n')

    number_processes = 6

    if number_processes < 4:
        print('Error: To little processes! Must be greater than 4')
        return
    else:
        print('Filler')



def main():
    cProfile.run('workMethod()')

if __name__ == '__main__':
    main()