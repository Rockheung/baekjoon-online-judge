
def josephus(n,m):
    s = [x for x in range(1, n+1)]
    l = []
    while s:
        idx = m-1 if len(s) >= m else m%len(s)-1
        s = s[idx+1:] + s[:idx+1]
        l.append( s.pop() )

    return l

if __name__ == '__main__':
    n,m = [int(x) for x in input().split()]
    print('<{}>'.format(josephus(n,m).__repr__()[1:-1]))

