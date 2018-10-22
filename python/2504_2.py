
# Problem: https://www.acmicpc.net/problem/2504


def cal(ps):
    ps = list(ps)
    buf = []
    res, buf_val = 0, []
    recent_closed, recent_opend = True, True
    while (True):
        try:
            s = ps.pop()
            if s == ')':
                if recent_closed:
                    buf_val.append(1)
                    recent_closed = False
                buf.append(s)
                recent_opend = True
            elif s == ']':
                if recent_closed:
                    buf_val.append(1)
                    recent_closed = False
                buf.append(s)
                recent_opend = True
            elif s == '(' and not buf[-1] == ']' :
                if recent_opend:
                    buf_val = [sum(buf_val) * 2]
                    recent_opend = False
                else :
                    buf_val[-1] *= 2
                recent_closed = True
                buf.pop()
            elif s == '[' and not buf[-1] == ')' :
                if recent_opend:
                    buf_val = [sum(buf_val) * 3]
                    recent_opend = False
                else :
                    buf_val[-1] *= 3
                buf_val = [sum(buf_val) * 3]
                recent_closed = True
                buf.pop()
            else:
                res = 0
                raise IndexError

            if len(buf) == 0:
                res, buf_val = res + sum(buf_val), []
            print('{}, {}: {}, {}'.format(ps,buf[::-1],buf_val,res))
        except IndexError:
            break

    return res


if __name__ == '__main__':
    from sys import stdin
    print(cal(stdin.readline().rstrip()))
