from sys import stdin, stdout

ns = []
for i in range(int(stdin.readline()[:-1])):
    ns.append(int(stdin.readline()[:-1]))

ns.sort()
for i in range(len(ns)):
    stdout.write('{}\n'.format(ns[i]))
