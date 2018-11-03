
# Problem: https://www.acmicpc.net/problem/2941


def croatiaAl(s):
    length = 0
    jump = 0
    for i in range(1,len(s)+1):
        if jump > 0:
            jump -= 1
            continue

        if s[-i] == '=':
            if s[-i-1] == 'z':
                try:
                    if s[-i-2] == 'd':
                        # dz=
                        jump =1
                        continue
                    else:
                        # z=
                        continue
                except IndexError:
                    # string starts z=
                    continue
            elif s[-i-1] == 'c':
                # c=
                continue
            elif s[-i-1] == 's':
                # s=
                continue

        elif s[-i] == '-':
            if s[-i-1] == 'c':
                # c-
                continue
            elif s[-i-1] == 'd':
                # d-
                continue

        elif s[-i] == 'j':
            try :
                if s[-i-1] == 'l':
                    # lj
                    continue
                elif s[-i-1] == 'n':
                    # nj
                    continue
            except IndexError:
                # string starts j~
                pass

        length +=1

    return length

if __name__ == '__main__' :
    print(croatiaAl(input()))
