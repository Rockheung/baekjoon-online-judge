
# Problem: https://www.acmicpc.net/problem/1929


from sys import stdin, stdout
[_from, _to] = [int(n) for n in stdin.read().rstrip().split()[:2] if n is not '']

# from 2 to _to, n = i + 2
prime_table = [True] * (_to-1)
for i in range(int(_to**0.5)+1):
    n = i+2
    prime_table[2*(i+1)::n] = [False]*(_to//n-1)
    #if prime_table[i]:
    #    # [...,T,T,T,...,T] = [...,F,T,F,...,F]
    #    j = 1
    #    while(True):
    #        try:
    #            prime_table[j*n+i] = False
    #        except IndexError:
    #            break
    #        j += 1
    #    #prime_table[i+1:] = [(j+i+3)%n != 0 and _ for j,_ in enumerate(prime_table[i+1:])]

# when 1, not prime
prime_table.insert(0,False)
stdout.write('\n'.join([str(_from+i) for i,_ in enumerate(prime_table[_from-1:]) if _]))

