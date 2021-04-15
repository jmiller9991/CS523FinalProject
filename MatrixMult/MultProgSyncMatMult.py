# Jacob Miller
# 4/12/2021
# Project Code: Python's Built in Multiprogramming Library Synchronous Matrix Multiplication

import numpy as np
import multiprocessing as mp
import ctypes as c
import cProfile

def CreateArray(m, n):
    mp_array = mp.Array('d', m*n)
    array = np.frombuffer(mp_array.get_obj(), c.c_int64)
    b = array.reshape((m, n))

    return b

def matrixWork(offset, rows_to_send, matrix1, matrix2, final_matrix):
    for i in range(len(matrix1)):
        for j in range(offset, offset+rows_to_send):
            for k in range(len(matrix2)):
                final_matrix[i*len(matrix1)+j] += matrix1[i][k] * matrix2[k][j]


def workMethod():
    matrix1 = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]])
    matrix2 = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45], [50, 55, 60], [65, 70, 75], [80, 85, 90]])

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

    number_processes = 3

    if number_processes < 2:
        print('Error: To little processes! Must be greater than 2')
        return

    processes = []

    with mp.Manager() as manager:
        offset = 0
        rows_to_send = 1
        final_matrix = mp.Array('i', 3*3)
        for _ in range(number_processes):
            p = mp.Process(target=matrixWork, args=[offset, rows_to_send, matrix1, matrix2, final_matrix])
            p.start()
            processes.append(p)
            offset += 1

        for p in processes:
            p.join()

    array = np.frombuffer(final_matrix.get_obj(), c.c_int32)
    k = array.reshape((3, 3))

    print(k)

def main():
    cProfile.run('workMethod()')

if __name__ == '__main__':
    main()