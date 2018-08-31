
def ans(s):
    char_count = dict()
    for char in s:
        if ord(char) >= ord('a'):
            char = chr(ord(char) -32)
        try:
            char_count[char] += 1
        except KeyError:
            char_count[char] = 1

    char_values = list(char_count.values())
    maximum_value = max(char_values)
    if char_values.count(maximum_value) >1 :
        return '?'

    for key in char_count.keys():
        if char_count[key] == maximum_value:
            return key


if __name__ == '__main__':
    print(ans(input()))
