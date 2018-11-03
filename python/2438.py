
# Problem: https://www.acmicpc.net/problem/2438

def ans(n):
    for i in range(1,n+1):
        for j in range(i):
            print('*',end='')
        print('')

if __name__ == '__main__' :
    ans(int(input()))
