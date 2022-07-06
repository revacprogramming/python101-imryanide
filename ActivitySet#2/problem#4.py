def get_cs():
    cs = str(input("Enter a string : "))
    return cs


def cs_to_lot(cs):
    l = cs.split(";")
    for i in range(len(l)):
        l[i] = tuple(l[i].split("="))
    return l


def lot_to_cs(lot):
    st = ""
    for i in lot:
        s = "=".join(i)
        st += f"{s};"
    print(st)


def main():
    cs = get_cs()

    lot = cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs = lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == "__main__":
    main()
