
# Problem: https://www.acmicpc.net/problem/2775


def d(a,b,
      people = [[0]*15 for i in range(15)]):
    if a == 0 or b == 1:
        people[a][b] = b
        return people
    else:
        people[a][b] = people[a][b-1] + people[a-1][b]

        return people

if __name__ == '__main__':
    for i in range(int(input())):
        k = int(input())
        n = int(input())
        people = d(0,1)
        for i in range(k+1):
            for j in range(1,n+1):
                people = d(i,j,people)
        print(people[k][n])

