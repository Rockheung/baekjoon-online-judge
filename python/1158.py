
def josephus(n,m):
    s = [x for x in range(1, n+1)]
    l = []
    idx = m = m - 1
    while s:
        idx = m-1 if len(s) >= m else m%len(s)-1
        s = s[idx+1:] + s[:idx+1]
        l.append( s.pop() )

    return l

# a, s = map(int, input().split())
# l = [i for i in range(1, a+1)]
# d = []
# i = s = s-1
# while len(l) > 1:
#     d += [l.pop(i)]
#     i = (i + s) % len(l)
# print('<'+str(d+l)[1:-1]+'>')

if __name__ == '__main__':
    n,m = [int(x) for x in input().split()]
    print('<{}>'.format(josephus(n,m).__repr__()[1:-1]))

