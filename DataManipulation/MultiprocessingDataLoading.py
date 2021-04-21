# Jacob Miller
# 4/19/2021
# Project Code: Python's Built in Multiprogramming Library Data Loading Program

import multiprocessing as mp
import cv2
import os
import cProfile
import math
import random

num_images = len([name for name in os.listdir('.\\Data\\OldFiles') if os.path.isfile(os.path.join('.\\Data\\OldFiles', name))])
num_processes = 5
fileLocation = '.\\Data\\OldFiles'

def collectImages():
    dataStrings = []

    for file in os.listdir(fileLocation):
        print(os.path.join(fileLocation, file))
        if os.path.isfile(os.path.join(fileLocation, file)):
            dataStrings.append(os.path.join(fileLocation, file))

    return dataStrings

def splitArray(array):
    final_array = []
    for string in array:
        tempArray = []
        for _ in range(math.floor(num_images/num_processes)):
            tempArray.append(string)
        final_array.append(tempArray)

    return final_array


def worker(img):
    image = cv2.imread(img)
    imagegrey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurimg = cv2.GaussianBlur(imagegrey, (3, 3), 0)
    logimg = cv2.Laplacian(blurimg, cv2.CV_64F)
    cv2.imwrite(filename=os.path.join('.\\Data\\OldFiles', f'file{random.randint(0, 1000000000000)}'), img=logimg)


def doWork():
    dataStrings = collectImages()
    print(dataStrings)

    dataList = splitArray(dataStrings)

    processes = []
    for array in dataList:


    print(dataList)



def main():
    cProfile.run('doWork()')

if __name__ == '__main__':
    main()