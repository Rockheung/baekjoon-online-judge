
# Problem: https://www.acmicpc.net/problem/15552

from sys import stdin

for i in range(int(input())):
    print(sum(map(int,stdin.readline().rstrip().split())))

