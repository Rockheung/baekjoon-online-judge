def time(n, m, play_time):
    t = 0
    while(True):
        t += 1
        children = sum([t%x for x in play_time])
        yield children

def _1561(n, m, play_time):
    play = [0 for _ in range(m)]
    i = idx = t = 0
    children = time(n,m,play_time)
    child = next(children)
    for _ in range(n):
        i += 1
        idx = play.index(min(play))
        play[idx] += play_time[idx]
        print(i,'child on play: ', play)
        if i == child:
            t += 1
            child = next(children)
            print('============== {} mins ============= {} children\n'.format(t, child))
    return idx+1

def time_child(n,m,m_t):
    time = child = 0
    while(n >= child):
        time += 1
        each_play = [time//mt for mt in m_t]
        left_time = [time%mt for mt in m_t]
        child = sum(each_play)
        yield time, child, each_play, left_time


# N: Children, M: Number of cars, M_T: time per car
def _1561_2(n, m, m_t):
    buf = [ 0 for _ in range(m) ]
    child = last_idx = 0
    children = time_child(n,m,m_t)
    time, child = next(children)[:2]
    for i in range(n):
        # last_idx = buf.index(min(buf))
        # buf[last_idx] += m_t[last_idx]
        buf = [time - time%x for j, x in enumerate(m_t)]
        if (i+1 < child):
            time, child = next(children)
        print('{:2d} @ {:2d} mins, {}'.format(i+1,time,buf))
    return last_idx + 1


def _1561_binary_search(n, m, m_t):
    lower, upper = 0, n * max(m_t)
    while (upper > lower):
        # even number => clearly half, odd number => bigger integer
        ref_time = (upper + lower)//2 if (upper + lower)%2 == 0 else (upper + lower)//2 + 1
        if ref_time == upper: break
        how_many_children = sum([ref_time//x for x in m_t])
        if how_many_children > n:
            upper = ref_time
        elif how_many_children < n :
            lower = ref_time +1
        else :
            break
    # min_ref_time <= ref_time, same or less
    min_ref_time = ref_time - min([ref_time%x for x in m_t])
    # can not be 0
    gap_children = n - sum([(min_ref_time-1)//x for x in m_t])
    pre_step_idx = [i+1 for i, x in enumerate([(min_ref_time-1)%x for x in m_t]) if m_t[i] - 1 == x]
    print(ref_time, min_ref_time, gap_children, pre_step_idx)
    return pre_step_idx[gap_children-1] # if gap_children > 0 else pre_step_idx[0]


def test(n, m, m_t):
    t = nc = 0
    while (n >= nc):
        nc = sum([t//x for x in m_t])
        print(t,nc, [x*(t//x) for x in m_t])
        t += 1



if __name__ == '__main__':
    # for _ in range(int(input())):
    #     n,m = map(int, tuple(input().split()))
    #     play_time = [int(x) for x in list(input().split())]
    #     print(ans(n,m,play_time))


    n,m = map(int, tuple(input().split()))
    play_time = [int(x) for x in input().split()]
    # test(n,m,play_time)
    # print(ans_1561_reversed(n,m,play_time))
    for t,c,ec,lt in time_child(n,m,play_time):
        print('time: ', t, '\tchild: ', c, '\teach play: ', ec, '\tleft time: ', lt)
    # print('the answer: ',_1561(n,m,play_time))

    # n,m = map(int, tuple(input().split()))
    # play_time = [int(x) for x in input().split()]
    print(_1561_binary_search(n,m,play_time))
