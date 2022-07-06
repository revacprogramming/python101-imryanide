class Menu:
    def __init__(self):
        self.items = dict()

    def __add__(self, item):
        self.items[item[0]] = item[1]
        return self

    def __setitem__(self, a, b):
        self.items[a] = b

    def __str__(self):
        f = "\n".join(" ".join((k, str(v))) for k, v in self.items.items())

        return f


m = Menu()
m["idly"] = 10
m["vada"] = 20

print(m)
