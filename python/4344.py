
def ans(str_read):
    classes = int(str_read[0])
    for line in str_read[1:]:
        values = list(map(int, line.split()))
        students = values[0]
        cls_avg = sum(values[1:])/students
        over_avg_n = 0
        for student_score in values[1:]:
            if student_score > cls_avg:
                over_avg_n += 1
        print('{:5.3f}%'.format(over_avg_n/students*100))

if __name__ == '__main__' :
    from sys import stdin

    ans(stdin.read().split('\n')[:-1])


