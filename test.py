import sys
from collections import deque
sys.stdin = open('test.txt', 'r')

# n = int(input())
# arr=list(map(int, input().split()))

dq = deque(list(input()))
n = int(input())


for _ in range(n):
    tmp = dq.copy()
    a = list(input())
    for x in a:
        if tmp :
            if tmp[0] == x:
                tmp.popleft()
        else:
            break
    if tmp:
        print('NO')
    else:
        print('YES')