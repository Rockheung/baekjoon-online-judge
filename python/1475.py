
def ans(n):
    if n == 0:
        return 1
    count_n = [0 for i in range(10)]
    while (n>0):
        count_n[n%10] += 1
        n = n//10
    count_n[6] += count_n.pop()
    count_n[6] = (count_n[6]+1)//2
    return max(count_n)


if __name__ == '__main__':
    print(ans(int(input())))
