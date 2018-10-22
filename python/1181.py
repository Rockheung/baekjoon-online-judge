
# Problem: https://www.acmicpc.net/problem/1181

from sys import stdin

l = []
for _ in range(int(input())):
    s = stdin.readline().rstrip()
    l.append((len(s),s))

print('\n'.join([word[1] for word in sorted(set(l))]))
