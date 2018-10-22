
# Problem: https://www.acmicpc.net/problem/2839


def ans(n):
    if n >= 3 and n <= 5000:
        when5 = n//5
        for i in range(when5,-1,-1):
            if ( n - i * 5 ) % 3 == 0:
                when3 = ( n - i * 5 ) // 3
                return i + when3
            else:
                continue
        return -1


    else:
        print('power overwhelming.')

if __name__ == '__main__' :
    print(ans(int(input())))
