
def printer_queue(n,m,values):
    count, s = 0, [(x,i) for i,x in enumerate(values)]
    while s:
        max_value_idx = s.index(max(s, key=lambda x: x[0]))
        s = s[max_value_idx+1:] + s[:max_value_idx+1]
        printed_paper = s.pop()
        count += 1
        if printed_paper[1] == m:
            break
    return count


if __name__ == '__main__':
    from sys import stdin
    for _ in range(int(stdin.readline().rstrip())):
        n, m = [int(x) for x in stdin.readline().rstrip().split()]
        values = [int(x) for x in stdin.readline().rstrip().split()]
        print(printer_queue(n,m,values))
