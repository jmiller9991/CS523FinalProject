# Jacob Miller
# 4/19/2021
# Project Code: Python's Built in Multiprogramming Library Data Loading Program

import multiprocessing as mp
import cv2
import os
import cProfile
import math

num_images = len([name for name in os.listdir('./Data/OldFiles') if os.path.isfile(name)])
num_processes = 5

def worker(img):
    modWidth = math.floor(1920/2.5)
    modHeight = math.floor(1080/2.5)

    image = cv2.imread(img)
    newimage = cv2.resize(image, (modWidth, modHeight))
    imagegrey = cv2.cvtColor(newimage, cv2.COLOR_BGR2GRAY)
    blurimg = cv2.GaussianBlur(imagegrey, (3, 3), 0)
    logimg = cv2.Laplacian(blurimg, cv2.CV_64F)

    return logimg


def doWork():
    print('')

def main():
    cProfile.run('doWork()')

if __name__ == '__main__':
    main()