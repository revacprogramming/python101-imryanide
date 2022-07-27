def get_cs():
    cs = str(input("Enter a string : "))
    return cs


def cs_to_dict(cs):
    d = dict(
        (k.strip(), v.strip()) for k, v in (word.split("=") for word in cs.split(";"))
    )
    return d


def dict_to_cs(d):
    l = [(
        k,
        "=",
        v,
    )
        for k, v in d.items()
    ]
    st = ""
    for i in l:
        a = "".join(i)
        st += f"{a};"
    return st


def main():
    # cs = get_cs()
    cs = "system=s;database=d;username=u;password=p"

    print("program being run")
    d = cs_to_dict(cs)  # convert connect string to a dictionary
    print(d)

    cs = dict_to_cs(d)
    print(cs)


if __name__ == "__main__":
    main()
