
def ans(s):

    for i in range(len(s)):
        if i < 2:
            continue
        if s[i] == s[i-1]:
            continue
        else:
            if s[i] in s[:i-1]:
                break
    else:
        return True
    return False


if __name__ == '__main__' :
    cnt = 0
    for i in range(int(input())):
        if ans(input()):
            cnt +=1
            print(cnt)
    print(cnt)
