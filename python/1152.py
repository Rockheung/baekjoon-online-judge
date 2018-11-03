
# Problem: https://www.acmicpc.net/problem/1152

from sys import stdin, stdout

def ans():
    cnt = 0
    was_word, is_word = False, False
    s = stdin.buffer.read(1)
    while (True):

        stdout.write("'{}'".format(s.decode('utf8')))
        if s == b'' :
            stdout.write('EOF detected')
            if was_word :
                cnt += 1
                break
            else :
                break
        elif s == b' ' :
            stdout.write('blank detected')
            is_word = False
        else:
            stdout.write('charator detected')
            is_word = True

        if is_word != was_word :
            if was_word :
            # word end
                stdout.write('wordend')
                cnt += 1

            else:
            # word start
                stdout.write('wordstart')
                pass
        was_word = is_word
        print('')
        s = stdin.buffer.read1(1)

    return cnt


if __name__ == '__main__' :
    print(ans())
    #s = stdin.read()
    #print('EOF detected')

    #words = s.split()
    #try :
    #    if words[0] == '':
    #        words = words[1:]
    #    elif words[-1] == '':
    #        words = words[:-1]
    #    print(len(words))
    #except IndexError:
    #    print(0)


