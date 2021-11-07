import sys
input = sys.stdin.readline


N = int(input())
stack = []
now = 1
ans = ''
for i in range(N):
    n = int(input())
    if ans == 'NO': break

    while True:
        if stack and stack[-1] == n:
            stack.pop()
            ans += '-'
            break
        elif now > N:
            ans = 'NO'
            break
        else:
            stack.append(now)
            now += 1
            ans += '+'

if ans == 'NO':
    print(ans)
else:
    for i in range(len(ans)):
        print(ans[i])
