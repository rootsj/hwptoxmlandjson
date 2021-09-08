import sys
from collections import deque
sys.stdin = open('test.txt', 'r')

# n = int(input())
# arr=list(map(int, input().split()))

n, k = map(int, input().split())

lst = list(map(int, str(n)))
lst = deque(lst)
cnt = 0
while cnt < k:
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            del lst[i]
            cnt += 1
            break
    else:
        # tmp = min(lst)
        # lst.remove(tmp)
        lst.pop()
        cnt += 1

res = 0
for i in range(len(lst)):
    res += lst[i]*10**(len(lst)-i-1)

print(res)