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

if __name__ == '__main__':
    n,m = tuple(map(int, input().split()))
    play_time = list(map(int, input().split()))
    print(_1561(n, m, play_time), '\n 번째:')

