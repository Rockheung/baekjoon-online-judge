
def queue_basic(cmd, val=None, l=[]):
    # cmd : (one of [push,pop,size,empty,top], int)
    l_empty = len(l) == 0
    if cmd == 'push':
        return l.append(val)
    elif cmd == 'pop':
        return -1 if l_empty else l.pop(0)
    elif cmd == 'size':
        return len(l)
    elif cmd == 'empty':
        return 1 if l_empty else 0
    elif cmd == 'front':
        return -1 if l_empty else l[0]
    elif cmd == 'back':
        return -1 if l_empty else l[-1]


if __name__ == '__main__' :
    from sys import stdin, stdout
    queue = []
    for _ in range(int(input())):
        said = queue_basic(*tuple(stdin.readline().rstrip().split()), l =queue)
        if said != None:
            stdout.write('{}\n'.format(said))


