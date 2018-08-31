for i in range(int(input())):
    h,w,n = tuple(map(int,input().split()))
    print('{}{:02d}'.format( (n-1)%h +1, (n-1)//h +1 ))
#    print('{}{:02d}'.format(h if n%h == 0 else n%h,
#                            n//h if n%h == 0 else n//h+1))
