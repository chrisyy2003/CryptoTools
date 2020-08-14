from random import uniform
from functools import cmp_to_key
from queue import PriorityQueue
import random
from tqdm import tqdm
import time

a0 = 4567688158292282644392204923129050407
a1 = 15927344100562897639822569631319390846
a2 = 16237186638727926404247881172951578768
a3 = 38428663813550082938695681489310882781
a4 = 26762485993137928931191297170284354307
a5 = 19507304947152413870700753726628409355
a6 = 15999583898447444907510051284366619278
a7 = 8654700076446528076464481966653478561
a8 = 11312553221539392202530199828204167382
a9 = 42390604411832728552562349957908002661
a10 = 8103623835644602806025265773965104963
a11 = 41699530062391518260703911156981461982
a12 = 42162669395936189974813031367012227585
a13 = 36353988447753212774500023635411113422
a14 = 36698285709394284859191624739760274617
a15 = 5144840550162988336200904134484359068
a16 = 13431961279774162602320810660377646880
a17 = 22389752099679506297914621391405132345
a18 = 24211567140437798229301905104719264047
a19 = 21748988818466326720487696288652040438
a20 = 1536935992636212460552146428522445450
a21 = 361926138094157837701439684380004053
a22 = 15092040138347985991135069282772565904
a23 = 10038412336191200672351991024258037194
a24 = 13545593721246684026341886897562101303
a25 = 20884641930880210972659401719751786193
a26 = 41944448402516921263334251152685638319
a27 = 8083635254800012436395531559610598167
a28 = 12647630630295935590260181963471635645
a29 = 4932639572554527595255668629189369146
a30 = 11547244442759018917554499082638887486
a31 = 7248419660281149473311311527657489800
a32 = 33853860407396646787677206805196572638
a33 = 26480492816737306784372625180338477026
a34 = 32610575993900535833437976576653873948
a35 = 30419256352783157268586784260010172443
a36 = 31064359147059452147735291066910051251
a37 = 29251030857103998592496246128095904752
a38 = 16056388254453939264579529133626972112
a39 = 33907053726119174829433109792276595254



n = 40
Hamingweight = 5

alist = []
for i in range(n):
    eval("alist.append({})".format('a' + str(i)))

# this is for test,it will gen test data randomly
ans = [alist.index(i) for i in
       random.sample(alist, Hamingweight)]

target = 0
for i in ans:
    target += alist[i]
print(target, ans)
print(''.join(['1' if i in ans else '0' for i in range(n)]))

t = target


def shamir(elements, target, Hamingweight):
    lent = len(elements)
    assert(lent % 4 == 0)
    quarter = lent // 4

    start = time.time()
    sl1 = inits(0, quarter - 1, elements, Hamingweight)
    sr1 = inits(quarter, 2 * quarter - 1, elements, Hamingweight)
    sl2 = inits(2 * quarter, 3 * quarter - 1, elements, Hamingweight)
    sr2 = inits(3 * quarter, lent - 1, elements, Hamingweight)
    print('init in ', time.time() - start)
    print('quarter len', len(sl1), len(sr1), len(sl2), len(sr2))

    algorithm3(sl1, sr1, sl2, sr2, n, target, Hamingweight)


def inits(left, right, elements, Hamingweight):

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
        if HMW > Hamingweight:
            '''
            if hmw > Hamingweight, we skip it
            '''
            continue
        slist.append((ssum, HMW))
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
                    ans.append(slist[i])
                else:
                    break
            ans.append(slist[mid])
            for i in range(mid + 1, len(slist)):
                if slist[i][0] == slist[mid][0]:
                    ans.append(slist[i])
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


def algorithm3(sl1, sr1, sl2, sr2, n, target, Hamingweight):
    ll = 2 ** ((1 / 4) * n)
    rr = 2 ** (((1 / 4) * n) + 1)
    M = int(uniform(ll, rr))
    print(ll, rr)
    print("Mod:", M)
    start = time.time()
    sr1m = [(sr1[i][0] % M, i) for i in range(len(sr1))]
    sr2m = [(sr2[i][0] % M, i) for i in range(len(sr2))]
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
            tmp = (m - sl1[sl1_index][0]) % M

            return_list = binarySearch(sr1m, tmp)
            '''
            find if any sigma_m - sl1[i] exists in sr1, if it is existed, then we add it into solulist
            '''

            for tmp, sr1_index in return_list:
                if sl1[sl1_index][1] + sr1[sr1_index][1] > Hamingweight:
                    '''
                    check HMW
                    '''
                    continue
                s.append((sl1[sl1_index][0] + sr1[sr1_index][0],
                          (sl1_index, sr1_index)))

        s = sorted(s, key=cmp_to_key(cmpfun))

        '''
        sort solution list by value of left member of each pair
        '''
        for sl2_index in range(len(sl2)):
            '''
            we loop sl2 to find whether target - sigma_m - sl2[k] mod M exists in sr2
            '''
            tmp = (target - m - sl2[sl2_index][0]) % M

            return_list = binarySearch(sr2m, tmp)
            '''
            find if any target - sigma_m - sl2[sl2_index] exists in sr2
            '''
            for tmp, sr2_index in return_list:
                if sl2[sl2_index][1] + sr2[sr2_index][1] > Hamingweight:
                    '''
                    check HMW
                    '''
                    continue
                '''
                we loop all the sr2[sl2_index] we found, and search whether \
                     target - sl2[sl2_index] - sr2[sr2_index] exists in temp solution list 
                '''
                tt = target - sl2[sl2_index][0] - sr2[sr2_index][0]
                return_ans = binarySearch(s, tt)
                '''
                return the list if sigma_sl1 + sigma_sr1 = target - sigma_sl2 + sigma_sr2
                '''
                for (T, (i, j)) in return_ans:
                    '''
                    ans, we finally found it, but it is sum of quarter kanspack
                    because we calc the quarter kanspack is so easy that \
                        we don't need to store the 01 string in this situation (which we know the HammingWight)
                        so, the reult is we only need to save the sum of each situation which will help saving space a lot
                    '''
                    ans = (sl1[i][0], sr1[j][0], sl2[sl2_index]
                           [0], sr2[sr2_index][0])
                    ssum = 0
                    for i in ans:
                        ssum += i
                    exit(str(ans) + '\n' + 'Ans: ' + str(ssum))

shamir(alist, t, Hamingweight)
