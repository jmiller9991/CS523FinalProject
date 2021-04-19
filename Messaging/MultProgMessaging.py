# Jacob Miller
# 4/19/2021
# Project Code: Python's Built in Multiprogramming Library Messaging Function

import multiprocessing as mp
import cProfile
import os

def processMessage(parentProcess):
    print(f'Hello {parentProcess}, this is {os.getpid()}.')

def doWork():
    processes = []

    for _ in range(5):
        p = mp.Process(target=processMessage, args=[os.getpid()])
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print('Done')

def main():
    cProfile.run('doWork()')

if __name__ == '__main__':
    main()