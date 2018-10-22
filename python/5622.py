
# Problem: https://www.acmicpc.net/problem/5622


def charToNum(char):
    if ord(char) in range(ord('A'),ord('D')):
        return 2+1
    elif ord(char) in range(ord('D'),ord('G')):
        return 3+1
    elif ord(char) in range(ord('G'),ord('J')):
        return 4+1
    elif ord(char) in range(ord('J'),ord('M')):
        return 5+1
    elif ord(char) in range(ord('M'),ord('P')):
        return 6+1
    elif ord(char) in range(ord('P'),ord('T')):
        return 7+1
    elif ord(char) in range(ord('T'),ord('W')):
        return 8+1
    elif ord(char) in range(ord('W'),ord('Z')+1):
        return 9+1


if __name__ == '__main__':
    print(sum(map(charToNum,list(input()))))
    pass


