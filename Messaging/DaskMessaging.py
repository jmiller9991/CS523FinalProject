# Jacob Miller
# 4/19/2021
# Project Code: Dask Library Exponential Function

import dask as da
import cProfile
import os

def processMessage(parentProcess):
    print(f'Hello {parentProcess}, this is {os.getpid()}.')

def doWork():
    delayed_work = []
    for _ in range(5):
        p = da.delayed(processMessage)(os.getpid())
        delayed_work.append(p)

    num = 0
    for i in delayed_work:
        i.visualize(filename=f'./Results/DaskMessagingResults/DaskMessagingProcess{num}')
        num += 1

    da.compute(*delayed_work, scheduler='processes', num_processes=5)


def main():
    cProfile.run('doWork()')

if __name__ == '__main__':
    main()