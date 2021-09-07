import sys

sys.stdin = open('test.txt', 'r')

n = int(input())
arr=list(map(int, input().split()))

lst = [1] * n
res = [0] * n
for i in range(n):
    cnt = 0
    for j in range(n+1):
        if arr[i] == cnt - 1:
            lst[j-1] = 0
            res[j-1] = i+1
            break
        cnt += lst[j]
            
print(res)