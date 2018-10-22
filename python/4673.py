
# Problem: https://www.acmicpc.net/problem/4673


def d(n):
    origin_n = n
    while ( n >0 ):
        origin_n += n%10
        n = n//10
    return origin_n


def under_bound(num):
    n_nine = 0
    origin_num = num
    while( num >9 ):
        num = num // 10
        n_nine += 1
    return origin_num - (num + 9*n_nine)


def is_self(num):
    for i in range(num,0,-1):
        if d(i) == num:
            return False
        elif i < under_bound(num):
            return True
    return True


if __name__ == '__main__':
    limit = 10000
    for i in range(1,limit +1):
        if is_self(i):
            print(i)
