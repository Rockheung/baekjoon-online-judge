
def ans(x,y):
    days_per_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    days = 0
    for i in range(x-1):
        days += days_per_month[i]
    days += y
    con = days % 7

    if con == 0:
        return 'SUN'
    elif con == 1:
        return 'MON'
    elif con == 2:
        return 'TUE'
    elif con == 3:
        return 'WED'
    elif con == 4:
        return 'THU'
    elif con == 5:
        return 'FRI'
    elif con == 6:
        return 'SAT'

if __name__ == '__main__':
    x,y = tuple(map(int,input().split()))
    print(ans(x,y))

