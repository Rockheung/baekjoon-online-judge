
# Problem: https://www.acmicpc.net/problem/1978

from sys import stdin

ns = [int(n) for n in stdin.read().split('\n')[1].split() if n is not '']

count = 0
for n in ns:
    if n is 1 or n//2 == 0:
        continue
    for i in range(n//2,1,-1):
        if n%i is 0:
            break
    else:
        count += 1

print(count)