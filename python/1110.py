
i = 0
n = int(input())
tmp = n
while(True):

    tmp = tmp%10 * 10 + (tmp%10 + tmp//10)%10
    i += 1
    if tmp == n:
        print(i)
        break



