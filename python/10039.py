
avg = 0
for i in range(5):
    a = int(input())
    if a < 40: a = 40
    avg = ( avg * i + int(input()) ) / (i+1)
print(int(avg))
