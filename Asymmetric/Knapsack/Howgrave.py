from tqdm import tqdm
from itertools import combinations
from functools import cmp_to_key
import random


a0 = 411932160813009099596968768
a1 = 206223842814678119689155352
a2 = 1165583303451951244969522412
a3 = 1002638044019331153011927866
a4 = 233816287586745360041206385
a5 = 483623870296143976342607254
a6 = 1050310990517875188131549500
a7 = 917725109633944027616930084
a8 = 940186852470384684271100101
a9 = 1185781701307454372629841483
a10 = 820560905753503539733461089
a11 = 240493137234590661355383771
a12 = 688598200720113198366445967
a13 = 829663810480040290624352755
a14 = 637685049999056289625506058
a15 = 709802940709581207416077236
a16 = 666854736531769210075111106
a17 = 1174434140638890980975787143
a18 = 363764422762837505032517982
a19 = 277772371335696186234142429
a20 = 1191018740036282916845174318
a21 = 722264000807056562031277782
a22 = 766987517082059707231860984
a23 = 811943911834193178505266378
a24 = 883457011458449275313902574
a25 = 954598973612992820603101052
a26 = 887883440513839616955446779
a27 = 317537178979620651851826765
a28 = 1210130210346021013288750985
a29 = 854201742728924212893811255
a30 = 184710422507839712390485789
a31 = 105544720123187807500065889
a32 = 331023808952188511017342875
a33 = 360753437644216812621871870
a34 = 221653414255353369348339102
a35 = 68277580053139910520075776
a36 = 82341906981058660949980532
a37 = 367745944087605010243614868
a38 = 301257361011568893954993341
a39 = 852906026237816654058084639
a40 = 128202333168297688467525158
a41 = 301779854679546602009826969
a42 = 600458191536860483185909449
a43 = 786881079658369788002881642
a44 = 1139685457689098666026089640
a45 = 158298906158964766453158173
a46 = 992328283942144699580406991
a47 = 196635672069276344141483156
a48 = 1091441923343258427560059421
a49 = 262710869423944220446160008
a50 = 83239505561924900526734354
a51 = 299613600810755699752373627
a52 = 174168655300802157741935842
a53 = 923582443079642672001527205
a54 = 550759358139708604277656498
a55 = 753797574205607940592938385
a56 = 568487970226498117892751124
a57 = 903781830781517993245948978
a58 = 57539759117318738717717614
a59 = 485754745177424980219202194
a60 = 909624071387635104101390614
a61 = 965253095439991730727669232
a62 = 475657621959355568079940474
a63 = 106177278470117836294639524
a64 = 982017862155679179751510573
a65 = 279266373235701075526448485
a66 = 459300965550262519882995960
a67 = 46519446052525795122645311
a68 = 225779646103550983346623896
a69 = 963474101795368940401027141
a70 = 1087542063394463969767328029
a71 = 503596208456450876081126903
a72 = 549917285077238243910529138
a73 = 1192320517696502894652063460
a74 = 749672991483493936647866722
a75 = 882814678218302388677829026
a76 = 739854598920812079469590160
a77 = 407274572677529179720211450
a78 = 1237093131416207319822591416
a79 = 965829800821200772643192417
a80 = 1098824294285732232129137784
a81 = 257618775382860052144612776
a82 = 738049954247558147301410295
a83 = 523361109907488786546603186
a84 = 742019564319343924610957595
a85 = 62950677228043172425481552
a86 = 844891243558179500123095305
a87 = 490920704290570235227071909
a88 = 894181515263133384368860639
a89 = 799953668546750403320988010
a90 = 343212017156409028412243218
a91 = 571757041803707231995502076
a92 = 441480994058568755819307303
a93 = 786624011797719648704609532
a94 = 165705181598250574952238505
a95 = 87526096238651280335932257
a96 = 653986960148459549718671670
a97 = 84079681912540595437280738
a98 = 898890585008121578121182631
a99 = 265910902642054747512047728

n = 100
k = 12
target = 7052297882425420144395439173

alist = []
for i in range(n):
    eval("alist.append({})".format('a' + str(i)))


def Cni(n, i):
    if not (isinstance(n, int) and isinstance(i, int) and n >= i):
        return

    result = 1
    Min, Max = min(i, n-i), max(i, n-i)
    for i in range(n, 0, -1):
        if i > Max:
            result *= i
        elif i <= Min:
            result //= i
    return result


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


def cmpfun(x, y):
    return x[0] - y[0]


def checkOverlap(x, y):
    for i in x:
        if i in y:
            return False
    return True


def algorithm3(sl1, sr1, sl2, sr2, n, target, M, k):

    sr1m = [(sr1[i][0] % M, i) for i in range(len(sr1))]
    sr2m = [(sr2[i][0] % M, i) for i in range(len(sr2))]

    sr1m = sorted(sr1m, key=cmp_to_key(cmpfun))
    sr2m = sorted(sr2m, key=cmp_to_key(cmpfun))

    # for i in sl1:
    #     print(i)
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
            for sr1_index in return_list:
                # print(sr1_index)
                if not checkOverlap(sl1[sl1_index][1], sr1[sr1_index][1]):
                    continue
                s.append((sl1[sl1_index][0] + sr1[sr1_index][0],
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
            tmp = (target - m - sl2[sl2_index][0]) % M
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
                if not checkOverlap(sl2[sl2_index][1], sr2[sr2_index][1]):
                    continue
                tt = target - sl2[sl2_index][0] - sr2[sr2_index][0]
                return_ans = binarySearch(s, tt)
                '''
                return the list if sigma_sl1 + sigma_sr1 = target - sigma_sl2 + sigma_sr2
                '''
                for i, j in return_ans:
                    '''
                    ans, we finally found it
                    '''
                    check = list(sl1[i][1]) + list(sr1[j][1]) + \
                        list(sl2[sl2_index][1]) + list(sr2[sr2_index][1])
                    if not len(set(check)) == k:
                        print(check)
                        continue
                    check_sum = 0
                    for c in check:
                        check_sum += alist[c]
                    if check_sum == target:
                        exit(
                            ''.join(['1' if i in check else '0' for i in range(n)]))


def Howgrave(alist, k, target, M):
    assert (k % 4 == 0)

    print('Mod:', M)
    alist_index = [i for i in range(n)]
    slist = []
    comb_iter = combinations(alist_index, k // 4)
    for i in tqdm(comb_iter, total=Cni(len(alist_index), k // 4)):
        ssum = 0
        for j in i:
            ssum += alist[j]
        slist.append((ssum, i))
    random.shuffle(slist)

    sl1 = slist[: len(slist) // 4]
    sr1 = slist[len(slist) // 4: len(slist) // 2]
    sl2 = slist[len(slist) // 2: (3 * len(slist)) // 4]
    sr2 = slist[(3 * len(slist)) // 4: len(slist)]
    print('quarter len', len(sl1), len(sr1), len(sl2), len(sr2))
    algorithm3(sl1, sr1, sl2, sr2, n, target, M, k)


Howgrave(alist, k, target, 2 ** 14)
