import sys

sys.stdin = open('test.txt', 'r')
n = int(input())
# k, n = map(int, input().split())
lst = list(map(int, input().split()))

m = int(input())

lst.sort(reverse=True)

print(lst)
# max = 0
# for i in range(m):
#     if x > max:
#         x = x -1
#         max = x
    

