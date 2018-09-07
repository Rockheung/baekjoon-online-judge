
def is_prime(n):
    if n is 1 or (n%2 == 0 and n>2):
        return False
    for i in range(n//2,1,-1):
        if n%i is 0:
            break
    else:
        return True
    return False

if __name__ == '__main__' :
    from sys import stdin

    bw = [int(n) for n in stdin.read().split('\n')[:2] if n is not '']
    l = [n for n in range(bw[0],bw[1]+1) if is_prime(n)]
    print('{}\n{}'.format(sum(l), min(l)) if len(l) is not 0 else -1)
