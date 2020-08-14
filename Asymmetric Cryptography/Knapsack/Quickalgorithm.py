import itertools
import random


a0 = 225108935779
a1 = 128643524893
a2 = 1089198518028
a3 = 909640564507
a4 = 724803740287
a5 = 352811075551
a6 = 93194394032
a7 = 365713407336
a8 = 183091396210
a9 = 775501103314
a10 = 436693537021
a11 = 1076837758820
a12 = 580854875356
a13 = 1002915944953
a14 = 378334726
a15 = 652468123846
a16 = 688115115109
a17 = 776255128947
a18 = 1061278491136
a19 = 122343782910

elements = []
for i in range(20):
    eval("elements.append({})".format('a' + str(i)))
    
ans = [elements.index(i) for i in
       random.sample(elements, random.randint(1, len(elements)))]
target = 0
for i in ans:
    target += elements[i]
print(target, ans)


def check():
    global elements
    elements = sorted(elements)
    prefixsum = []
    for i in range(len(elements)):
        if i == 0:
            prefixsum.append(elements[i])
        else:
            temp = prefixsum[i - 1] + elements[i]
            prefixsum.append(temp)

    for i in prefixsum:
        if i == target:
            print('sovled')
            return True
        if target < i and i < 2 * target:
            r = i - target
            if r in elements:
                print('sovled')
                return True
            else:
                for j in range(0, prefixsum.index(i)):
                    if r == prefixsum[j]:
                        print('sovled')
                        return True
                    elif prefixsum[j] > r:
                        if j == 0:
                            del(elements[j])
                        else:
                            a = prefixsum[j] - prefixsum[j - 1]
                            elements.remove(a)
                        return False


while True:
    if check():
        break
