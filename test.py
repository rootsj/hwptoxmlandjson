import sys
from collections import deque
sys.stdin = open('test.txt', 'r')

# n = int(input())
# arr=list(map(int, input().split()))

n, k =map(int, input().split())

# lst = [1] * n

# m = sum(lst)

# i = 0
# lstsum = 0
# while m != 1 :
#     s = i%n
#     lstsum += lst[s] 
#     if lstsum == k :
#         lst[s] = 0
#         lstsum = 0
#         m = sum(lst)

#     i += 1


# print(lst.index(1) +1)

dq = list(range(1, n+1))
dq = deque(dq)

while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) ==1:
        print(dq[0])
        dq.popleft()