
def primes(n=10000):
    # Each index of elements used as integer, 0:False, 1:False
    prime_table = [False,False] + [True] * (n-1)
    for i in range(2,int(n**0.5)+1):
        if prime_table[i]:
            prime_table[2*i::i] = [False]*((n-i)//i)
    return prime_table


def goldbach(n,l = primes()):
    for i in [j for j,b in enumerate(l[n//2:n]) if b]:
        k = i + n//2
        if l[n-k]:
            partition = (n-k, k)
            break
    else:
        partition = (0,n)
    return partition


if __name__ == '__main__':
    from sys import stdin, stdout
    l = primes()
    for _ in range(int(stdin.readline().rstrip())):
        n = int(stdin.readline().rstrip())
        stdout.write('{0} {1}\n'.format(*goldbach(n,l)))

