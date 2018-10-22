
# Problem: https://www.acmicpc.net/problem/2577


result = list(str(int(input()) * int(input()) * int(input())))

result.sort()
cnt = []

for i in range(10):
    cnt.append(0)
    while (str(i) in result):
        cnt[-1] += 1
        result = result[1:]
    print(cnt[i])
