import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    #print(arr)
    for i in range(n):
        print(arr[-i])
    print(arr)
    arr2 = list( reversed(arr))
    print(*reversed(arr))
    print(*(arr2))
    print(" ".join(map(str, arr[::-1])))