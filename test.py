ans = 3

a = [1, 2, 1, 3, 1, 1, 1, 2]

l1 = 0
r1 = 1
temp = a[0]
cnt = 0

while l1 <= len(a):
    if temp > ans:
        temp -= a[l1]
        l1 += 1
    elif temp == ans:
        cnt += 1
        temp -= a[l1]
        l1 += 1
    else:
        if r1 < len(a):
            temp += a[r1]
            r1 +=1
        else:
            break
print(cnt)