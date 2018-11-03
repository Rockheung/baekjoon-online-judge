
# Problem: https://www.acmicpc.net/problem/2504

def cal_unit(ps,
             buf=0):
    try:
        s = ps.pop()
        while(ps[-1] in [')',']']):
            ps, buf_tmp = cal_unit(ps)
            buf += buf_tmp
        buf = 1 if buf == 0 else buf
        if (ps[-1],s) == ('(',')'):
            ps.pop()
            return ps, buf*2
        elif ps[-1] == '[' and s == ']':
            ps.pop()
            return ps, buf*3
        raise IndexError
    except IndexError:
        return ps,0


if __name__ == '__main__':
    ps, val = cal_unit(list(input().join(['[',']'])))
    print(val//3 if len(ps) == 0 else 0)
