
def ans(str_n):
    from functools import reduce
    return reduce(lambda x,y: x+y,map(int,list(str_n)))

if __name__ == '__main__':
    input()
    print(ans(input()))
