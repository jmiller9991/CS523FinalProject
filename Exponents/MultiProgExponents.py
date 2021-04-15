# Jacob Miller
# 4/12/2021
# Project Code: Python's Built in Multiprogramming Library Exponential Function

import multiprocessing as mp
import cProfile
import math

def getNumExpon(exponent):
    exponentArray = []

    if exponent % 2 == 0:
        for _ in range(1, exponent+1):
            exponentArray.append(2)
    else:
        for _ in range(1, exponent+1):
            exponentArray.append(2)

        exponentArray.append(1)

    return exponentArray

def exponent(base, expon, ret_val):
    if expon == 1:
        pass
    else:
        for _ in range(expon-1):
            base *= base

    ret_val.value = base

def mult_exponent_work(base, expon, vals):
    processes = []
    if vals is None:
        vals = []

    exponNum = getNumExpon(expon)

    if expon == 1:
        return base
    else:
        for i in range(len(exponNum)):
            ret_val = mp.Value('I', 0, lock=False)
            p = mp.Process(target=exponent, args=[base, exponNum[i], ret_val])

            p.start()
            vals.append(ret_val.value)

        for p in processes:
            p.join()

def mult_exponent(base, expon):
    return mult_exponent_work(base, expon, None)


def doWork():
    print('works')

def main():
    print(exponent(8, 5))
    print(mult_exponent(8, 5))
    cProfile.run('doWork()')

if __name__ == '__main__':
    main()