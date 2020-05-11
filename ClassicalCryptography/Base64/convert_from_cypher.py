key_list = []
value_list = []
s = 'FlZNfnF6Qol6e9w17WwQQoGYBQCgIkGTa9w3IQKw'
mydisc = {0: 'J', 1: 'K', 2: 'L', 3: 'M', 4: 'N', 5: 'O', 6: 'x', 7: 'y', 8: 'U', 9: 'V', 10: 'z', 11: 'A', 12: 'B', 13: 'C', 14: 'D', 15: 'E', 16: 'F', 17: 'G', 18: 'H', 19: '7', 20: '8', 21: '9', 22: 'P', 23: 'Q', 24: 'I', 25: 'a', 26: 'b', 27: 'c', 28: 'd', 29: 'e', 30: 'f', 31: 'g', 32: 'h',
          33: 'i', 34: 'j', 35: 'k', 36: 'l', 37: 'm', 38: 'W', 39: 'X', 40: 'Y', 41: 'Z', 42: '0', 43: '1', 44: '2', 45: '3', 46: '4', 47: '5', 48: '6', 49: 'R', 50: 'S', 51: 'T', 52: 'n', 53: 'o', 54: 'p', 55: 'q', 56: 'r', 57: 's', 58: 't', 59: 'u', 60: 'v', 61: 'w', 62: '+', 63: '/', 64: '='}
for key, value in mydisc.items():
    key_list.append(key)
    value_list.append(value)


def value_to_key(a):
    get_value = a
    if get_value in value_list:
        get_value_index = value_list.index(get_value)
    else:
        raise TypeError
    return(get_value_index)


ss = []
for i in s:
    ss.append(value_to_key(i))
bin_new = []
for i in ss:
    bin_new.append(bin(i)[2:])

temp = []
for i in bin_new:
  if len(i) < 6:
    i = (6-len(i))*'0' + i
  else:
    i = i
  temp.append(i)

ans = ''
for i in temp:
    ans += i
ans = [ans[i: i + 8] for i in range(0, len(ans), 8)]
for i in ans:
    print(chr(int(i, 2)), end='')
