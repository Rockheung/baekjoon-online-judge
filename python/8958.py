
def cal(ox):
    score = 0
    plus = 1
    for i in range(80):
        try :
            if ox[i] == 'O':
                score += plus
                plus += 1
            else:
                plus = 1
        except IndexError :
            break
    return score


if __name__ == '__main__' :

    for i in range(int(input())):
        print(cal(input()))
