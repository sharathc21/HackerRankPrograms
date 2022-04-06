import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    sum = 0
    tarr = []
    print(arr)
    print(type(arr))

    for l in range(0, 4):
        print("*******" , l)
        for k in range(0, 4):
            print("########" , k)
            for i in range(l, l + 3):
                print("COLUMN COLUMN" , i)
                for j in range(k, k + 3):
                    print("ROW ROW" , j)
                    if i == l + 1 and (j == k or j == k + 2):
                        continue
                    else:
                        sum += arr[i][j]
            tarr.append(sum)
            sum = 0

    print(max(tarr))