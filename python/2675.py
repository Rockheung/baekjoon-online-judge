
def ans(n,s):
    repeated_string = ''
    for char in s:
        for i in range(n):
            repeated_string += char
    return repeated_string


if __name__ == '__main__' :
    for i in range(int(input())):
        cmd = input().split()
        print(ans(int(cmd[0]),cmd[1]))
