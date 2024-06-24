#!/bin/python3

import math
import os
import random
import re
import sys


def insertionSort1(n, arr):
    ans = arr[-1]
    p = n - 2

    while p >= 0 and arr[p] > ans:
        arr[p + 1] = arr[p]
        print(' '.join(map(str, arr)))
        p -= 1
    
    arr[p + 1] = ans
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
