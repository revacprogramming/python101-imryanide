class Menu:
    def __init__(self):
        self.items = dict()

    def __add__(self, item):
        self.items[item[0]] = item[1]
        return self

    def __str__(self):
        f = "\n".join(" ".join((k, str(v))) for k, v in self.items.items())

        return f


m = Menu()

m = (
    m + ("idly", 10) + ("vada", 20)
)  # Hint: operator overloading special methods (__add__, __sub__, etc.)

print(m)  # should print the menu properly
