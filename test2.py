n = 7
data = [6, 6, 0, 1]

s = data[:2]
d = data[2:]

def m1(lst):
    lst[0] = lst[0] - 2
    lst[1] = lst[1] - 1
    return lst

def m2(lst):
    lst[0] = lst[0] - 2
    lst[1] = lst[1] + 1
    return lst

def m3(lst):
    lst[1] = lst[1] - 2
    return lst

def m4(lst):
    lst[1] = lst[1] + 2
    return lst

def m5(lst):
    lst[0] = lst[0] + 2
    lst[1] = lst[1] - 1
    return lst

def m6(lst):
    lst[0] = lst[0] + 2
    lst[1] = lst[1] + 1
    return lst

def move(s):
    move1 = m1(s.copy())
    move2 = m2(s.copy())
    move3 = m3(s.copy())
    move4 = m4(s.copy())
    move5 = m5(s.copy())
    move6 = m6(s.copy())
    return [move1, move2, move3, move4, move5, move6]
    
cnt = 0
slst = [s]
while True:
    cnt += 1
    
    for i in slst:
        temp = move(i)
        slst += temp
        del slst[slst.index(i)]
        
    for i in slst:
        if i[0] < 0 or i[0] >= n or i[1] < 0 or i[1] >= n:
            del slst[slst.index(i)]

    if d in slst:
        break
            
print(cnt)
    