# Jacob Miller
# 4/14/2021
# Project Code: Dask Exponential Function

import dask as da

import multiprocessing as mp
from multiprocessing import Pool
import cProfile
from functools import partial

def getNumExpon(exponent):
    exponentArray = []

    if exponent % 2 == 0:
        for _ in range(0, exponent//2):
            exponentArray.append(2)
    else:
        for _ in range(0, exponent//2):
            exponentArray.append(2)

        exponentArray.append(1)

    return exponentArray

def exponent(base, expon):
    if expon == 1:
        pass
    else:
        for _ in range(expon-1):
            base *= base

    return base


def mult_exponent(base, expon):
    answer = 1
    processes = []
    vals = []

    exponNum = getNumExpon(expon)

    if expon == 1:
        return base
    else:
        vals = [da.delayed(exponent)(base, x) for x in exponNum]
        num = 0
        for i in vals:
            i.visualize(filename=f'./Results/DaskExponentsResults/DaskExponentsProcess{num}')
            num += 1
        results = da.compute(*vals, scheduler='processes', num_workers=expon//2 if expon % 2 == 0 else (expon//2)+1)

    for i in results:
         answer *= i

    return answer


def doWork():
    print(mult_exponent(8, 5))

def main():
    cProfile.run('doWork()')

if __name__ == '__main__':
    main()