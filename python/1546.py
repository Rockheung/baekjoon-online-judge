
lec_num = int(input())
score_list = list(map(int,input().split()))
max_score = max(score_list)
alter_score_list = list(map(lambda x: x/max_score*100,score_list))

print(sum(alter_score_list)/lec_num)
