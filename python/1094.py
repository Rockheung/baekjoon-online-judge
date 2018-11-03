
# Problem: https://www.acmicpc.net/problem/1094


def f(x):
    st_len = [64]

    while( sum(st_len) > x ):
        st_len.append(int(st_len[-1]/2))
        st_len[-2] = st_len[-1]

        if sum(st_len[0:-1]) >= x:
            st_len.pop()

    return len(st_len)

if __name__ == '__main__':
    print(f(int(input())))

