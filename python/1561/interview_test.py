def ans(n, m, m_t):
    buf = [ 0 for _ in range(m) ]
    for _ in range(n):
        min_buf_idx = buf.index(min(buf))
        buf[min_buf_idx] += m_t[min_buf_idx]
        print(buf, "\t\t", [x//m_t[i] for i, x in enumerate(buf)])
    return max(buf)


def ans_bin(n, m, m_t):
    upper = n * max(m_t)
    lower = 0
    while (upper > lower):
        ref_time = (upper + lower)//2 if (upper + lower)%2 == 0 else (upper + lower)//2 + 1
        if ref_time == upper: break
        how_many_children = sum((ref_time//x for x in m_t))
        print("Children: {}, ref_time: {}, upper: {}, lower: {}".format(how_many_children, ref_time, upper, lower))
        if how_many_children > n:
            upper = ref_time -1
        elif how_many_children < n :
            lower = ref_time
        else :
            break

    min_ref_time = ref_time - min((ref_time%x for x in m_t))
    return min_ref_time


if __name__ == '__main__':
    for _ in range(int(input())):
        n,m = map(int, tuple(input().split()))
        play_time = [int(x) for x in list(input().split())]
        ans1, ans2 =ans(n,m,play_time), ans_bin(n,m,play_time)
        exit()
        if ans1 != ans2:
            print("Wrong!: expect {}, but {}".format(ans1, ans2))
        else:
            print("Right!: %s" % ans2)
