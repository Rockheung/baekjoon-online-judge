
# Problem: https://www.acmicpc.net/problem/1065


def isHansoo(n):
    while ( True ):
        gap = n //10 %10 - n %10
        n = n//10
        if n < 10:
            return True
        elif gap != n //10 %10 - n %10:
            return False

if __name__ == '__main__' :
    N = 110
    cnt = 0
    for i in range(1, N+1):
        if isHansoo(i):
            cnt +=1

    print(cnt)
