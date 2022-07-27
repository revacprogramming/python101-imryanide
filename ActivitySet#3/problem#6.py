def get_goals(x):
    if x <= 1:
        return 1
    elif x == 2:
        return 2

    return get_goals(x - 1) + get_goals(x - 2) + get_goals(x - 3)


def output(res: list[tuple[int, int]]):
    for i, j in res:
        print(f"{i} points: {j} ways")


def main():
    pts = [0, 3, 10, 13]
    res = []
    for i in pts:
        res.append((i, get_goals(i)))

    output(res)


main()
