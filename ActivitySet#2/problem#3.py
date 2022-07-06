

def get_cs():
    s = str(input("enter a string: "))
    return s


def cs_to_lot(cs):
    l = cs.split(';')
    for i in range(len(c)):
        l[i] = tuple()


def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
