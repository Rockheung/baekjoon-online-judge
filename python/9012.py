
# Problem: https://www.acmicpc.net/problem/9012


def isClosed(ps):
    if len(ps) % 2 != 0:
        return False
    buf = []
    for p in ps:
        try:
            if '(' == p:
                buf.append('(')
            else :
                buf.pop()
        except IndexError:
            return False
    else:
        return True if len(buf) == 0 else False
    return False


if __name__ == '__main__':
    from sys import stdin
    n,*l = [s.rstrip() for s in stdin.readlines()]
    [print('YES') if isClosed(ps) else print('NO') for ps in l]
