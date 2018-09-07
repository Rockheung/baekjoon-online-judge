
def _10989(length, n_list):
    from collections import Counter
    n_dict = Counter(n_list)
    n_list = []

    n_sum = 0
    n_frq = [(4001,0)]
    for i in range(-4000,4001):
        try:
            # n_list
            n_list = n_list + [i]*n_dict[i]

            # n_sum
            n_sum += i*n_dict[i]

            # n_frq
            if n_frq[0][1] < n_dict[i]:
                n_frq = [(i,n_dict[i])]
            elif n_frq[0][1]  == n_dict[i]:
                n_frq = n_frq + [(i,n_dict[i])]

        except KeyError:
            continue

    return n_list, n_sum, n_frq

if __name__ == '__main__':
    #from sys import stdin

    #length = int(stdin.readline())
    #n_list = [int(s) for s in stdin.read().split('\n') if s is not '']
    #n_list, n_sum, n_frq = _10989(length,n_list)

    #print(n_list)
    #print(round(n_sum/length))
    #print(n_list[length//2])
    #try:
    #    print(n_frq[1][0])
    #except IndexError:
    #    print(n_frq[0][0])
    #print(n_list[-1]-n_list[0])

    from sys import stdin
    from collections import Counter

    length = int(stdin.readline())
    n_list = sorted([int(s) for s in stdin.read().split('\n') if s is not ''])
    n_dict = Counter(n_list)

    print(round(sum(n_list)/length))
    print(n_list[length//2])
    n_frq = sorted(n_dict.items(), key=lambda x: x[1], reverse=True)
    try :
        print(n_frq[1][0] if n_frq[1][1] == n_frq[0][1] else n_frq[0][0])
    except IndexError:
        print(n_frq[0][0])
    print(n_list[-1]-n_list[0])

