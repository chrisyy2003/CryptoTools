import itertools

key = []
cipher = "ouauuuoooeeaaiaeauieuooeeiea"
for i in itertools.permutations('aeiou', 5):
    key.append(''.join(i))
for each in key:
    temp_cipher = ""
    result = ""
    for temp in cipher:
        temp_cipher += str(each.index(temp))
#这里其实是将字母的表换成数字的表以便后续计算
    for i in range(0, len(temp_cipher), 2):
        current_ascii = int(temp_cipher[i])*5+int(temp_cipher[i+1])+97
#因为棋盘密码是采用两位一起表示一个字母
        if current_ascii > ord('i'):
            current_ascii += 1
        result += chr(current_ascii)
    if "flag" in result:
        print(each, result)
