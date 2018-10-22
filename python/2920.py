
# Problem: https://www.acmicpc.net/problem/2920


def ans(s):
    d = s[-1] - s[-2]
    for i in range(7):
        if s[i+1] - s[i] == d:
            pass
        else:
            return 'mixed'
    if d > 0:
        return 'ascending'
    elif d < 0 :
        return 'descending'


if __name__ == '__main__' :
    print(ans(list(map(int,input().split()))))

