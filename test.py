from itertools import permutations
from os import pipe
import sys

sys.stdin = open('test.txt', 'r')
k, n = map(int, input().split())
all = list(int(input()) for _ in range(k))

all.sort()

def Count(line):
    cnt = 1
    ep = all[0]
    for i in range(1, len(all)):
        if all[i]- ep>= line:
            cnt += 1
            ep = all[i]
    return cnt

lt = 1
rt = all[-1]
res = 0

while lt <= rt:
    mid = (lt + rt)//2

    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)