rome_t = [(1000,'M'),(500,'D'),(100,'C'),(50,'L'),(10,'X'),(5,'V'),(1,'I')]
n_map = {**{ str(n): n for n in range(10) },**{ j: i for i,j in rome_t }}


def rome(str_):
    istr_, l = 0, 1
    try :
        istr_ = int(str_)
        l = 10**(len(str_)-1)
    except ValueError:
        pass
    pre_s, s = 10**4, 0
    for i in str_:
        s += n_map[i]*l if n_map[i]*l <= pre_s else -pre_s*2 + n_map[i]
        pre_s = n_map[i]*l
        l //= 10 if l > 1 else l
    return s if not istr_ else int_to_roman(s)


def rome_gen():
    is_tens = False
    for i,j in rome_t:
        is_tens = not is_tens
        yield i,j

def int_to_roman(a):
    all_roman_digits = []
    digit_lookup_table = [
        "", "0", "00", "000", "01",
        "1", "10", "100", "1000", "02"]
    for i,c in enumerate(reversed(str(a))):
        roman_digit = ""
        for d in digit_lookup_table[int(c)]:
          roman_digit += ("IVXLCDM"[int(d)+i*2])
        all_roman_digits.append(roman_digit)
    return "".join(reversed(all_roman_digits))

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
