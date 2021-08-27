import sys
from traceback import print_tb

sys.stdin = open('test.txt', 'r')
# n = int(input())
n = 7
all = [list(map(int, input().split())) for _ in range(n)]

def our_five(lst):
    for i in range(2):
        if lst[i] != lst[4-i]:
            return False
    return True

cnt = 0

for i in range(n):
    for j in range(3):
        if our_five(all[i][j:5+j]):
            cnt += 1
    templ = []7
    for k in range(n):
        templ.append(all[k][i])
    
    for l in range(3):
        if our_five(templ[l:5+l]):
            cnt += 1

print(cnt)