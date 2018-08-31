def d(n):
    # maximum distance with n space jumping
    dis = (n//2)*((n//2)+1)
    if n%2 != 0:
        dis = dis +n//2 +1

    return dis

def d_(d):
    # a^2 <= a^2 + a <= (a+1)^2 = a^2 + 2*a + 1
    from math import sqrt, ceil
    n = ceil(sqrt(d))
    if d <= n*(n-1):
        return 2*(n-1)
    else:
        return 2*(n-1) +1


if __name__ == '__main__':
    for _ in range(int(input())):
        x,y = tuple(map(int,input().split()))
        #jump = 0
        #while (True):
        #    if d(jump) >= y-x:
        #        break
        #    else:
        #        jump += 1
        #print(jump)
        print(d_(y-x))


