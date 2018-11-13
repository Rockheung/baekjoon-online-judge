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
    idx, t, idx_l = 0, 0, []
    for i in range(n):
        cars[idx] += times[idx]
        pre_idx, idx = idx, cars.index(min(cars))
        idx_l.append(pre_idx+1)
        print(i+1, "children enterd.\t", cars)
        if pre_idx >= idx :
            t += 1
            log = t, ('s' if t >1 else ''), sum((t//x + (1 if t%x > 0 else 0) for x in times))
            print(">> Now {} min{} passed. Expect {}\n".format(*log))
    return pre_idx+1, cars[pre_idx], max(cars), idx_l


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


# shema7k's code on acmicpc.net
def damn_right(n,m,ts):
    k = n//m if n%m else n//m - 1
    # 모든 놀이기구의 탑승 시간이 min(tx) 인 경우보다는 무조건 길거나 같고,
    # max(tx) 인 경우보다는 무조건 짧거나 같다.
    lo, hi = min(ts)*k, max(ts)*k
    md = (lo+hi)//2
    while lo < hi:
        # 루프문을 빠지는 경우 무조건 True인 경우가 실행되고 나서다.
        print(lo, hi, md, sum((md+t)//t for t in ts))
        if sum((md+t)//t for t in ts) < n:
            lo = md+1
            md = (lo+hi)//2
        else:
            hi = md
            md = lo if lo+1==hi else (lo+hi)//2
    print(lo, hi, md, sum((md+t)//t for t in ts))
    l = [i for (i, t) in enumerate(ts, 1) if not md%t]
    idx = n-1-sum((md+t)//t for t in ts)
    print(l,idx)
    return l[idx]


def sol3(n, m, times):
    lower, upper = 0, n * max(times)
    entered_children_func = lambda p, ts: sum((p//t + (1 if p%t else 0) for t in ts))
    while (True):
        ref_time = (upper + lower)//2
        d = n - entered_children_func(ref_time, times)
        if not upper > lower:
            while d > 0:
                ref_time += 1
                d = n - entered_children_func(ref_time, times)
            break
        if d < 0:
            upper = ref_time - 1
        elif d > 0:
            lower = ref_time + 1
        else:
            break
        print(lower, upper, ref_time, d)
    last_one_list_reversed = [(ref_time%t if ref_time%t else t) for t in times[::-1]]
    idx_map = {x:[] for x in set(last_one_list_reversed)}
    for i, x in enumerate(last_one_list_reversed): idx_map[x].append(i)
    sorted_idx = []
    for _,j in sorted(idx_map.items()): sorted_idx.extend(j)
    print('d: {}'.format(d), sorted_idx, last_one_list_reversed)
    return m - sorted_idx[(-d if d < 0 else d)]


def test(n, m, times):
    t = nc = 0
    while (n >= nc):
        nc = sum([t//x for x in times])
        print(t,nc, [x*(t//x) for x in times])
        t += 1


if __name__ == '__main__':
    nm = [int(i) for i in input().split()]
    times = [int(t) for t in input().split()]
    #print('Last played car index: {0}, takes maximum time: {2}, \n{3}'.format(*sol0(*nm,times)))
    #print(sol3(*nm, times))
    print(damn_right(*nm, times))
