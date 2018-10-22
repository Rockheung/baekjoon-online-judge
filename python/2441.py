
# Problem: https://www.acmicpc.net/problem/2441

def ans(n):
    for i in range(1,n+1):
        for j in range(i-1):
            print(' ',end='')
        for j in range(n-i+1):
            print('*',end='')
        print('')

if __name__ == '__main__' :
    ans(int(input()))

