
# Problem: https://www.acmicpc.net/problem/10989


def sorting(n, ns={}):
    try:
        ns[n] +=1
    except KeyError:
        ns[n] = 1

    #return ns


if __name__ == '__main__':
    from sys import stdin, stdout
    global ns
    ns = {}
    for _ in range(int(stdin.readline())):
        sorting(int(stdin.readline()), ns)

    for i in range(10001):
        try:
            for _ in range(ns[i]):
                stdout.write('{}\n'.format(i))
        except KeyError:
            continue
