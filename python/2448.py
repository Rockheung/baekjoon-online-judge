from sys import stdout

def triStar(n):
    if n % 3 == 0:
        return '  *  '
    elif n % 3 == 1:
        return ' * * '
    else:
        return '*****'


def triStarParent(n,m):
    if m == 3:
        return triStar(n)
    else:
        m = m//2
        space = ' ' * m
        if n < m:
            stars = triStarParent(n,m)
            return '{space}{stars}{space}'.format(space=space,
                                                  stars=stars)
        else:
            n = n - m
            stars = triStarParent(n,m)
            return '{stars} {stars}'.format(stars=stars)


if __name__ == '__main__' :
    N = int(input())
    for line in range(N):
        stdout.write(triStarParent(line,N) + '\n')
