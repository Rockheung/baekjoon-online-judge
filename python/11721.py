
def ans(str):
    for i, char in enumerate(list(str)):
        print(char, end='')
        if i > 0 and (i+1) % 10 == 0:
            print('')


if __name__ == '__main__' :
    ans(input())

