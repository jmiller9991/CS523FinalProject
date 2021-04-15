# Jacob Miller
# 4/12/2021
# Project Code: Dask Synchronous Matrix Multiplication

import dask.array as dar
import cProfile

def workMethod():
    matrix1 = dar.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]])
    matrix2 = dar.array([[5, 10, 15], [20, 25, 30], [35, 40, 45], [50, 55, 60], [65, 70, 75], [80, 85, 90]])

    # Expected Results:
    # [1155, 1260, 1365]
    # [2685, 2970, 3255]
    # [4215, 4680, 5145]

    print('Matrix 1:')
    print(matrix1.compute())
    print('\n')

    print('Matrix 2:')
    print(matrix2.compute())
    print('\n')

    result = dar.dot(matrix1, matrix2)

    result.visualize(filename='./Results/DaskSyncMatrixMultFiles/DaskSyncMatrixMultGraph')

    print('Final Result')
    print(result.compute())
    print('\n')


def main():
    cProfile.run('workMethod()')

if __name__ == '__main__':
    main()