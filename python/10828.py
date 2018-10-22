
# Problem: https://www.acmicpc.net/problem/10828


def stack_basic(cmd, val=None, l=[]):
    # cmd : (one of [push,pop,size,empty,top], int)
    if cmd == 'push':
        return l.append(val)
    elif cmd == 'pop':
        return l.pop() if len(l) != 0 else -1
    elif cmd == 'size':
        return len(l)
    elif cmd == 'empty':
        return 1 if len(l) == 0 else 0
    elif cmd == 'top':
        return -1 if len(l) == 0 else l[-1]


if __name__ == '__main__' :
    from sys import stdin, stdout
    stack = []
    for _ in range(int(input())):
        said = stack_basic(*tuple(stdin.readline().rstrip().split()), l =stack)
        if said != None:
            stdout.write('{}\n'.format(said))


