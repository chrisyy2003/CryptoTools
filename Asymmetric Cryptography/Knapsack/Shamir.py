from random import uniform
from functools import cmp_to_key
from queue import PriorityQueue
import random
from tqdm import tqdm
import time

a0 = 780007910488861179164293870887
a1 = 644757781267431438527370588084
a2 = 886344987910700007796700699622
a3 = 67037192443258799119898868140
a4 = 315956500273241342245431683326
a5 = 351211073412604835884630475291
a6 = 335995606663513190145190482978
a7 = 297359033781432237886700807123
a8 = 830856741522978372146275766502
a9 = 66237663505632806581378309121
a10 = 215381734735218549313962033405
a11 = 901490788983193928886516147592
a12 = 499548714837069155558450537001
a13 = 224630055332830997824601426897
a14 = 919172894051797483753355195026
a15 = 1245440331898780823251731300504
a16 = 298263995223321209902868895182
a17 = 736591430769582414355553278342
a18 = 1217976030016671115168136964102
a19 = 980399099884318297365025522271
a20 = 726084355132965753252062504988
a21 = 951277826840378766945561669930
a22 = 7492442200302555390486229208
a23 = 769018513342604618159516970070
a24 = 968152198590814209754881322238
a25 = 1175154665753017160833066426121
a26 = 451952196471082603080565175017
a27 = 1221094023689255701171287330816
a28 = 617456087916724185254283878151
a29 = 226112898226641715564773252737
a30 = 494810212661607333752928148148
a31 = 1244821663551343141356670958981
a32 = 679214190369761834097630749359
a33 = 745058412645059179660418453044
a34 = 1178229830813633913730449092984
a35 = 145802775498878544007250617349
a36 = 1120246265160574187528207432153
a37 = 879947206559082641568587869322
a38 = 694829766294593284811782637743
a39 = 27254432667363032997310672464
a40 = 659494232598071549477042457760
a41 = 246528894190618505904569471972
a42 = 678865008088637501445062252585
a43 = 338808883115188328216917974008
a44 = 1018882116589475681487141636385
a45 = 1158813812666127224068687083490
a46 = 264861243888267321676943341263
a47 = 957035318282481388126583643771
a48 = 121395106437898768786742821430
a49 = 733030825909285569200182100546
a50 = 305618917229574413477554522517
a51 = 75182500931530460131410629755
a52 = 586653780752038828569948879988
a53 = 332991466840391253377151142954
a54 = 296394405234869673922299039928
a55 = 805934172483659984586773930035
a56 = 656008533725072531300144122851
a57 = 517161090722432151064824834972
a58 = 928185271325990023639867434343
a59 = 1177899137071656787050480758867
a60 = 357896645320081951255458603894
a61 = 467873303098919619010073972178
a62 = 10697778856593413757096120593
a63 = 1032669931157944085613864453414
a64 = 698087824675361176886841387098
a65 = 588394770204870734332475755272
a66 = 330227773620622907404137468739
a67 = 295321540866134015452365486910
a68 = 281437885647461771317155804903
a69 = 709728628048170786125020832064
a70 = 1029768319199646500625942385046
a71 = 882416399181152563590763186600
a72 = 52221618698931979331786986840
a73 = 580957965369110356549439523530
a74 = 1030938236467422246514086978334
a75 = 48147882819944893682232344365
a76 = 613755699121297942938013297184
a77 = 212667208182638643053989035876
a78 = 1155773109402126568900579741992
a79 = 1009168609261199786533951974015


n = 80
target = 3808748539414823520119275163007
alist = []
for i in range(n):
    eval("alist.append({})".format('a' + str(i)))

# this is for ckeck ans
# check = '00000010001000011000000000000000000100000000000000000000001000100001100010000000'
# summ = 0
# for i in range(len(check)):
#     summ += int(check[i]) * alist[i]
# if summ == target:
#     print('solved!')

# this is for test,it will gen test data randomly
ans = [alist.index(i) for i in
       random.sample(alist, random.randint(1, len(alist)))]
target = 0
for i in ans:
    target += alist[i]
print(target, ans)
print(''.join(['1' if i in ans else '0' for i in range(n)]))

t = target

def shamir(elements, target):
    lent = len(elements)
    assert(lent % 4 == 0)
    quarter = lent // 4

    start = time.time()
    sl1 = inits(0, quarter - 1, elements)
    sr1 = inits(quarter, 2 * quarter - 1, elements)
    sl2 = inits(2 * quarter, 3 * quarter - 1, elements)
    sr2 = inits(3 * quarter, lent - 1, elements)
    print('init in ', time.time() - start)
    print('quarter len', len(sl1), len(sr1), len(sl2), len(sr2))

    algorithm3(sl1, sr1, sl2, sr2, n, target)


def inits(left, right, elements):

    lent = right - left + 1

    slist = []
    for i in tqdm(range(2 ** lent)):
        count = 0
        value = i
        HMW = 0
        ssum = 0
        while value > 0:
            last = value & 0x1
            if last == 1:
                ssum += elements[right - count]
                HMW += 1
            count += 1
            value = value >> 1
        slist.append(ssum)
    return slist


def binarySearch(slist, x):
    '''
    return the list which left value equal to x in slist
    '''
    l = 0
    r = len(slist) - 1
    ans = []
    while l <= r:
        mid = (l + r) // 2
        if slist[mid][0] == x:
            for i in range(mid - 1, -1, -1):
                if slist[i][0] == slist[mid][0]:
                    ans.append(slist[i][1])
                else:
                    break
            ans.append(slist[mid][1])
            for i in range(mid + 1, len(slist)):
                if slist[i][0] == slist[mid][0]:
                    ans.append(slist[i][1])
                else:
                    break
            return ans
        elif slist[mid][0] > x:
            r = mid - 1
        else:
            l = mid + 1
    else:
        return []


def cmpfun(x, y):
    return x[0] - y[0]


def algorithm3(sl1, sr1, sl2, sr2, n, target):
    ll = 2 ** ((1 / 4) * n)
    rr = 2 ** (((1 / 4) * n) + 1)
    print(ll, rr)
    M = int(uniform(ll, rr))
    print("Mod:", M)
    start = time.time()
    sr1m = [(sr1[i] % M, i) for i in range(len(sr1))]
    sr2m = [(sr2[i] % M, i) for i in range(len(sr2))]
    end = time.time()
    print('list created in', end - start)

    sr1m = sorted(sr1m, key=cmp_to_key(cmpfun))
    sr2m = sorted(sr2m, key=cmp_to_key(cmpfun))
    print('list sorted in ', time.time() - end)


    sol = []
    '''
    solution list
    '''
    for m in tqdm(range(M)):
        s = []
        '''
        create empyt temp solution list
        '''

        for sl1_index in range(len(sl1)):
            '''
            loop sl1, and compute sigma_m, which equal to sigma_l1 + sigma_r1,
            we simply let sigma_t equal to sigma_m - sigma_l1
            '''
            tmp = (m - sl1[sl1_index]) % M
            return_list = binarySearch(sr1m, tmp)
            '''
            find if any sigma_m - sl1[i] exists in sr1, if it is existed, then we add it into solulist
            '''

            for sr1_index in return_list:
                # print(sr1_index)
                s.append((sl1[sl1_index] + sr1[sr1_index],
                          (sl1_index, sr1_index)))

        s = sorted(s, key=cmp_to_key(cmpfun))
        # print('-----')

        '''
        sort solution list by value of left member of each pair
        '''
        for sl2_index in range(len(sl2)):
            '''
            we loop sl2 to find whether target - sigma_m - sl2[k] mod M exists in sr2
            '''
            tmp = (target - m - sl2[sl2_index]) % M
            return_list = binarySearch(sr2m, tmp)
            '''
            find if any target - sigma_m - sl2[sl2_index] exists in sr2
            '''
            for sr2_index in return_list:
                # print(sr2_index)
                '''
                we loop all the sr2[sl2_index] we found, and search whether \
                     target - sl2[sl2_index] - sr2[sr2_index] exists in temp solution list 
                '''
                tt = target - sl2[sl2_index] - sr2[sr2_index]
                return_ans = binarySearch(s, tt)
                '''
                return the list if sigma_sl1 + sigma_sr1 = target - sigma_sl2 + sigma_sr2
                '''
                for i, j in return_ans:
                    '''
                    ans, we finally found it
                    '''
                    ans = ''
                    for i in (i, j, sl2_index, sr2_index):
                        ans += bin(i)[2:].rjust(n // 4, '0')
                    exit(ans)
shamir(alist, t)
