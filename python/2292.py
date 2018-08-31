
def d(n):
    if n == 1: return 1
    return (n-1) * 6


if __name__ == '__main__' :
    th = 1
    octo = 0
    n = int(input())
    while (True):
        octo += d(th)
        if n <= octo:
            break
        else:
            th +=1

    print(th)
