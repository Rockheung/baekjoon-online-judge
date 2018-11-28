def f(a):
  i,r,t=0,[],((),(0,),(0,0),(0,0,0),(0,1),(1,),(1,0),(1,0,0),(1,0,0,0),(0,2))
  while a:a,c,l=a//10,a%10,'';l=''.join(["IVXLCDM"[d+i*2] for d in t[c]]);r.append(l);i+=1
  return "".join(r[::-1])
r=range(1,4000);l={**{str(x):f(x) for x in r},**{f(a):a for a in r}}
for _ in range(int(input())):print(l[input()])
exit()

q={**{str(n):n for n in range(10)},**{j:i for i,j in [(1000,'M'),(500,'D'),(100,'C'),(50,'L'),(10,'X'),(5,'V'),(1,'I')]}}
def y(u):
  t,l=0,1
  try:t=int(u);l=10**(len(u)-1)
  except ValueError:pass
  p,s=8**4,0
  for i in u:s+=q[i]*l if q[i]*l<=p else -p*2+q[i];p=q[i]*l;l//=10 if l>1 else l
  return s if not t else f(t)

def rome_gen():
    is_tens = False
    for i,j in rome_t:
        is_tens = not is_tens
        yield i,j


def conv_to_rome(int_, rome_num=None, gen=None):
    if rome_num == None: rome_num = ''
    if gen == None: gen = rome_gen()
    try:
        if not int_:
            gen.close()
        i,j = next(gen)
        rome_cnt = int_//i
        if rome_cnt < 4:
            rome_num += rome_cnt*j
            next(gen)
            int_ -= rome_cnt*i
        # not working
        elif rome_cnt < 5:
            l_j = conv_to_rome(i*5)
            next(gen)
            rome_num += j + l_j
            int_ -= -i + n_map[l_j]
        elif rome_cnt == 5:
            rome_dic = dict(rome_t)
            return rome_dic[int_]
        # not working
        elif rome_cnt < 9:
            l_j = conv_to_rome(i*5)
            next(gen)
            rome_num += l_j + rome_cnt*j
            int_ -= n_map[l_j] + rome_cnt*i
        else:
            l_j = conv_to_rome(i*10)
            rome_num += j + l_j
            next(gen)
            int_ -= -i + n_map[l_j]
    except StopIteration:
        return rome_num
    rome_num = conv_to_rome(int_, rome_num=rome_num, gen=gen)
    return rome_num


if __name__ == '__main__':
    for _ in range(int(input())):
        print(rome(input()))
