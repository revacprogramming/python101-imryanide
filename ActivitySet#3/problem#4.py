# run length decode
# S = 37 0 0 5 5 5 5 5 5 429 429 0 0 0 8 2 2 2 0 86 86 86 86 7 5 1 1 2
# (37)(0 0)(5 5 5 5 5 5)(429 429)(0 0 0)(8)(2 2 2)(0)(86 86 86 86)(7)(5)(1 1)(2)
# (1) Any run of length three or less whose members are non-zero is left unaltered.
# (2) Any run of length four or more whose members are non-zero is encoded by three numbers:
# zero (which signals that a run is being encoded), followed by the length of the run,
# followed by the value of each member. For example, a run of 5’s having length twelve is
# encoded as 0 12 5.
# (3) Any run of length two or more whose members have value zero is encoded as in (2). For
# example, a run of 0’s having length three is encoded as 0 3 0.
# (4) A run of length one whose member is zero is encoded as 0 0.
# T = 37 0 2 0 0 6 5 429 429 0 3 0 8 2 2 2 0 0 0 4 86 7 5 1 1 2


# first get the number of runs
# store each run
# encode each run

s = "0 6 4 0 0 71 71 0 4 5"
s = "4 4 4 4 4 4 0 71 71 5 5 5 5"


def decode(s: list[int]):
    res = ""
    i = 0
    while i < len(s):
        if s[i] == 0:
            if s[i + 1] == 0:
                res += "0 "
                i += 2
            else:
                n = s[i + 1]
                c = s[i + 2]
                for _ in range(n):
                    res += f"{c} "
                i += 3

        else:
            res += f"{s[i]} "
            i += 1

    return res


def main():
    l = [0, 6, 4, 0, 0, 71, 71, 0, 4, 5]
    print(decode(l))


main()
