
# Problem: https://www.acmicpc.net/problem/10809


s = input()

for i in range(ord('a'),ord('z')+1):
    for j in range(len(s)):
        if ord(s[j]) == i:
            print('{}'.format(j), end=' ')
            break
    else:
        print('{}'.format(-1), end=' ')
