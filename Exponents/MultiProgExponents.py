# Jacob Miller
# 4/14/2021
# Project Code: Python's Built in Multiprogramming Library Exponential Function

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
    vals = []

    exponNum = getNumExpon(expon)

    if expon == 1:
        return base
    else:
        p = Pool(processes=expon//2 if expon % 2 == 0 else (expon//2)+1)
        args = partial(exponent, base)
        data = p.map(args, exponNum)
        p.close()

        vals.extend(data)

    for i in vals:
         answer *= i

    return answer


def doWork():
    print(mult_exponent(256, 256))

def main():
    cProfile.run('doWork()')

if __name__ == '__main__':
    main()