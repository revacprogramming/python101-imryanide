

def get_cs():
    s = str(input("enter a string: "))
    return s


def cs_to_lot(cs):
    l = cs.split(';')
    for i in range(len(l)):
        l[i] = (tuple(l[i].split("=")))
    return l

def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
