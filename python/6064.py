
def ext_euclidean(x, y):
    r = (x, y)
    s = (1, 0)
    t = (0, 1)
    while r[1] != 0:
        q = r[0] // r[1]
        r = r[1], r[0] - q * r[1]
        s = s[1], s[0] - q * s[1]
        t = t[1], t[0] - q * t[1]
    return r[0], s[0], t[0]


def cain_cal_3(M, N, x, y):
    gcd, s, t = ext_euclidean(M, N)
    if x % gcd == y % gcd:
        return (x - M*s*(x-y)//gcd) % (M*N//gcd)
    else:
        return -1
    # Inspired from user:abel1802
    #
    # From Extended Euclid Algorithm
    # gcd = M * s + N * t
    #
    # From problem's condition
    # M * i + x = N * j + y
    # x - y = N * j - M * i
    #
    # gcd*(x-y) = M*s*(x-y) + N*t*(x-y)
    # x-y = M*s*(x-y)//gcd + N*t*(x-y)//gcd
    # x - M*s*(x-y)//gcd = y + N*t*(x-y)//gcd
    # {} = y + N*t*(N*j - M*i)//gcd
    # {} = y + N*N*t*j//gcd - M*N*t*i//gcd
    # {} = y + N*j - N*j + N*N*t*j//gcd - t*i * M*N//gcd
    # {} = y + N*j + (N*t//gcd - 1) * (N*j) + t*i * M*N//gcd
    # {} = y + N*j + ((gcd - M*s)//gcd - 1) * (N*j) + t*i * M*N//gcd
    # {} = y + N*j - M*s//gcd * (N*j) + t*i * M*N//gcd
    # {} = y + N*j + (t*i - s*j) * M*N//gcd
    # ... And y+N*j is what we are looking for!!


def euclidean(m,n):
    m,n = max(m,n), min(m,n)
    while(n != 1):
        if m%n == 0:
            break
        m, n = n, m%n
    return n


def cainCalender(m,n,x,y,th=1):
    # Ignoring RecursionError
    if (x,y)==(1,1):
        return th,x,y
    elif th > m*n/euclidean(m,n):
        return -1, 1, 1
    else:
        try:
            return cainCalender(m,n,
                                x-1 if x > 1 else m,
                                y-1 if y > 1 else n,
                                th+1)
        except RecursionError:
            return th,x,y


def cainCal2(m,n,x,y):
    from math import gcd
    th = 0
    for i in range(n//gcd(m,n)):
        if (m*i+x-1) % n == y-1:
            th = m*i+x
            break
    else:
        return -1
    return th


if __name__ == '__main__':
    from sys import stdin
    for i in range(int(input())):
        m,n,x,y = tuple(map(int,stdin.readline().split()))
        th = cain_cal_3(m,n,x,y)
        #th, x, y = cainCalender(m,n,x,y)
        #while ((x,y) != (1,1)):
        #    th, x, y = cainCalender(m,n,x,y,th)
        #    print('{}th, not yet!'.format(th))
        print(th)
