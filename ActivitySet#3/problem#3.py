st = "test palinalin racecar"


def check_both_side(st, low, high):
    palins = []
    while low >= 0 and high < len(s) and st[low] == st[high]:
        if len(st[low : high + 1]) >= 3:
            palins.append(st[low : high + 1])
        low -= 1
        high += 1
    return palins


def find_pals(st):
    p = []
    for i in range(len(st)):
        p.append(check_both_side(st, i, i))
        p.append(check_both_side(st, i, i + 1))
    return p


def output(lst):
    for i in lst:
        if i:
            print(i)


s = str(input("Enter string"))
p = find_pals(s)
output(p)
