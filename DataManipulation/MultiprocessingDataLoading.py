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
        if os.path.isfile(os.path.join(fileLocation, file)):
            dataStrings.append(os.path.join(fileLocation, file))

    return dataStrings

def splitArray(array):
    final_array = []
    count = 1
    valueStop = math.floor(num_images/num_processes)
    tempArray = []
    for string in array:
        tempArray.append(string)

        if count % valueStop == 0:
            final_array.append(tempArray)
            tempArray = []

        count += 1

    return final_array


def worker(imgarr):
    for img in imgarr:
        value = img.lstrip('.\\Data\\OldFiles\\frame').rstrip('.png')

        image = cv2.imread(img)
        imagegrey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurimg = cv2.GaussianBlur(imagegrey, (3, 3), 0)
        logimg = cv2.Laplacian(blurimg, cv2.CV_64F)
        cv2.imwrite(filename=os.path.join('.\\Data\\NewDataMP', f'file{value}.png'), img=logimg)


def doWork():
    dataStrings = collectImages()
    print(dataStrings)

    dataList = splitArray(dataStrings)

    processes = []

    for a in dataList:
        p = mp.Process(target=worker, args=[a])
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


def main():
    cProfile.run('doWork()')

if __name__ == '__main__':
    main()