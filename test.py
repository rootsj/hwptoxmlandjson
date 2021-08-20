import sys

sys.stdin = open('test.txt', 'r')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

maxv = 0
for i in range(n):
    if sum(a[i]) > maxv:
        maxv = sum(a[i])
    
    verv = 0
    for j in range(n):
        verv += a[j][i]
    if verv > maxv:
        maxv = verv

x1 = 0
x2 = 0
for i in range(n):
    x1 += a[i][i]
    x2 += a[i][n-i-1]

if max(x1, x2) > maxv:
    maxv = max(x1, x2)

print(maxv)