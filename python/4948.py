
def bertrand(n):

    # from 2 to 2n, n = i + 2
    prime_table = [True] * (2*n-1)
    for i in range(int((2*n)**0.5)+1):
        real_n= i + 2
        prime_table[2*(i+1)::i+2] = [False]*((2*n)//real_n-1)

    return prime_table[n-1:].count(True)


if __name__ == '__main__':
    from sys import stdin, stdout

    n =-1
    m = []
    while (n != 0):
        n = int(stdin.readline().rstrip())
        m.append(bertrand(n))

    stdout.write('\n'.join(map(str, m[:-1])))

