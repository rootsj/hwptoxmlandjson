import sys
sys.stdin = open('test.txt', 'r')

# n = int(input())
# arr=list(map(int, input().split()))

razer = list(input())

stack = []
res = 0

for x in razer:
    stack.append(x)

    if x == ')':
        stack.pop()
        tmp = stack[-1]
        tmp_len = len(stack)
        cnt = 0
        for i in range(-1, -tmp_len - 1, -1):
            if stack[i+cnt] == 0:
                cnt += 1
                stack.pop()

            elif stack[i+cnt] == '(' and cnt == 0:
                stack.pop()
                stack.append(0)
                break
            else:
                stack.pop()
                res += 1
                for i in range(cnt):
                    stack.append(0)
                    res += 1
                break

print(stack)
print(res)