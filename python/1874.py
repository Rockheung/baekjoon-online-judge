
# Problem: https://www.acmicpc.net/problem/1874

from sys import stdin

n, *l = [int(s.rstrip()) for s in stdin.readlines()]
stack = [0]
process = []
i, j = 0, 1
for _ in range(n*2):
    poped_n = -1 if l[i] > stack[-1] else stack.pop()
    if poped_n < 0:
        stack.append(j)
        process.append('+')
        j += 1
    elif poped_n == l[i]:
        process.append('-')
        i += 1
    else:
        process = ['NO']
        break
print('\n'.join(process))
