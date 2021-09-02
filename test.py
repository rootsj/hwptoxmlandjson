from itertools import permutations
from os import pipe
import sys

sys.stdin = open('test.txt', 'r')
n = int(input())
# k, n = map(int, input().split())
meeting = []
for _ in range(n):
    s, e = map(int, input().split())
    meeting.append([s, e])


meeting.sort(key=lambda x:(x[1], x[0]))

cnt = 1
end = meeting[0][1]
for x in meeting[1:]:
    if end <= x[0]:
        cnt += 1
        end = x[1]

print(cnt)