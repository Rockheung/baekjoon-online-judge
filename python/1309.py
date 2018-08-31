
def f(n, all = (1,1,1)):
    if n <1 or n >100000:
        return -1
    for i in range(n-1):
        all = (sum(all),
               all[0]+all[2],
               all[0]+all[1])


    return sum(all)

if __name__ == '__main__' :
    print(f(int(input()))%9901)
