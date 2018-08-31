
def reverse(n):
    new_n = 0
    for i in range(3):
        if n > 0:
            new_n *= 10
            new_n += n%10
            n = n//10
    return new_n

if __name__ == '__main__':
    print(max(map(reverse,map(int,input().split()))))
