# Jacob Miller
# 4/19/2021
# Project Code: Python's Built in Multiprogramming Library Data Loading Program

import multiprocessing as mp
import cv2
import os
import cProfile

num_images = len([name for name in os.listdir('./Data/OldFiles') if os.path.isfile(name)])
num_processes = 5

def worker(img):
    print('')

def doWork():
    print('')

def main():
    cProfile.run('doWork()')

if __name__ == '__main__':
    main()