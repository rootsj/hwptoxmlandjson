import sys
from collections import deque

sys.stdin = open('test.txt', 'r')

n = int(input())
arr=list(map(int, input().split()))


arr = deque(arr)
def bool(arr, tmp):
    if len(arr) == 1:
        return True
    if arr[0] < arr[-1] and arr[0] > tmp:
        return True
    elif arr[0] > arr[-1] and arr[-1] > tmp:
        return True
    else:
        return False

def test(arr, tmp):
    if len(arr) == 1:
        return (arr.pop(), "L")
    elif arr[0] < arr[-1] and arr[0] > tmp:
        return (arr.popleft(), "L")
    elif arr[0] > arr[-1] and arr[-1] > tmp:
        return (arr.pop(), "R")

res = ''
tmp = 0
for _ in range(len(arr)):
    if bool(arr, tmp):
        n, s = test(arr, tmp)
        res += s
        tmp = n
    else:
        break

print(len(res))
print(res)