
# Problem: https://www.acmicpc.net/problem/1193


def d(n):
    return int(n*(n+1)/2)


if __name__ == '__main__':
    th = 1
    n = int(input())
    while (True):
        if n <= d(th):
            break
        else:
            th +=1

    m = n - d(th-1)
    if th % 2 == 0:
        print('{}/{}'.format(m,th+1-m))
    else:
        print('{}/{}'.format(th+1-m,m))


