#
# https://www.acmicpc.net/problem/1561

# Generator for getting number of children as many as possible
# at each time
def time_(n, m, times):
    t = child = 0
    while (n >= child):
        t += 1
        each_play = [t//mt for mt in times]
        left_time = [t%mt for mt in times]
        child = sum(each_play)
        yield t, child, each_play, left_time

def sol(n,m,times):
    idx, cars = 0, [0 for _ in range(m)]
    for _ in range(n):
        idx = cars.index(min(cars))
        cars[idx] += times[idx]
    return idx + 1


def sol0(n, m, times):
    cars = [0 for _ in range(m)]
    idx, t = 0, 0
    for i in range(n):
        cars[idx] += times[idx]
        pre_idx, idx = idx, cars.index(min(cars))
        print(i+1, "children enterd.\t", cars)
        if pre_idx >= idx :
            t += 1
            log = t, ('s' if t >1 else ''), sum((t//x + (1 if t%x > 0 else 0) for x in times))
            print(">> Now {} min{} passed. Expect {}\n".format(*log))
    return pre_idx+1, cars[pre_idx], max(cars)


# N: Children, M: Number of cars, times: time per car
def sol1(n, m, times):
    buf = [ 0 for _ in range(m) ]
    child = last_idx = 0
    children = time_(n,m,times)
    t, child = next(children)[:2]
    for i in range(n):
        # last_idx = buf.index(min(buf))
        # buf[last_idx] += times[last_idx]
        buf = [t - t%x for j, x in enumerate(times)]
        if (i+1 < child):
            t, child = next(children)
        print('{:2d} @ {:2d} mins, {}'.format(i+1,t,buf))
    return last_idx + 1


# Problem: If how_many_children == condition provided when running,
# this way works well, but else we should calculate every each step.
# Good example: 22 children, 5 plays, 1,2,3,4,5 mins on each play.
def sol2(n, m, times):
    lower, upper = 0, n * max(times)
    while (upper > lower):
        # even number => clearly half, odd number => bigger integer
        ref_time = (upper + lower)//2 if (upper + lower)%2 == 0 else (upper + lower)//2 + 1
        if ref_time == upper: break
        how_many_children = sum((ref_time//x for x in times))
        if how_many_children > n:
            upper = ref_time
        elif how_many_children < n :
            lower = ref_time +1
        else :
            break
    # min_ref_time <= ref_time, same or less
    min_ref_time = ref_time - min((ref_time%x for x in times))
    # can not be 0
    gap_children = n - sum(((min_ref_time-1)//x for x in times))
    pre_step_idx = [i+1 for i, x in enumerate([(min_ref_time-1)%x for x in times]) if times[i] - 1 == x]
    print(ref_time, min_ref_time, gap_children, pre_step_idx)
    return pre_step_idx[gap_children-1] # if gap_children > 0 else pre_step_idx[0]


def sol3(n, m, times):
    lower, upper = 0, n * max(times)
    while (upper > lower):
        ref_time = (upper + lower)//2
        if ref_time == lower: break
        # n is exact entered_number
        escape_mark = None
        entered_children = sum((ref_time//x + (1 if ref_time%x > 0 else 0) for x in times))
        if entered_children > n:
            # ref_time is going to be lower when escape
            escape_mark = True
            upper = ref_time
        elif entered_children < n:
            # ref_time is going to be upper when escape
            escape_mark = False
            lower = ref_time + 1
        else:
            break
    # escape_mark did not changed
    if escape_mark == None:
        last_one_list_reversed = reversed([(t if ref_time%t == 0 else ref_time%t) for t in times])
        return m - last_one_list_reversed.index(min(last_one_list_reversed))
    else:
        if  escape_mark:
            pass

def test(n, m, times):
    t = nc = 0
    while (n >= nc):
        nc = sum([t//x for x in times])
        print(t,nc, [x*(t//x) for x in times])
        t += 1



if __name__ == '__main__':
    from sys import stdin
    nm = [int(i) for i in stdin.readline().rstrip().split()]
    times = [int(t) for t in stdin.readline().rstrip().split()]
    # for t,c,ec,lt in time_(n,m,times):
    #     print('time: ', t, '\tchild: ', c, '\teach play: ', ec, '\tleft time: ', lt)
    # print('Last played car index: {0}, takes maximum time: {2}'.format(*sol0(n,m,times)))
    print(sol(*nm, times))
