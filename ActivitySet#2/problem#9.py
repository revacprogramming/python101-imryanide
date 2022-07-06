class Menu(dict):
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


class Order:
    def __init__(self, menu):
        self.menu = menu
        self.ordereditems = dict()

    def __setitem__(self, dish, no):
        self.menu[dish]
        self.ordereditems[dish] = no


class Bill:
    def __init__(self, menu, order):
        self.bill = self._calc_bill(menu, order)

    def _calc_bill(self, menu, order):
        sum = 0
        for key, val in order.ordereditems.items():
            t = val * menu[key]
            sum += t
        return sum

    def __str__(self) -> str:
        return f"Your total bill is {self.bill} rupees"


m = Menu()
m["idly"] = 20
m["vada"] = 20

o = Order(m)
try:
    o["vada"] = 2
    o["pongal"] = 2

except KeyError as e:
    print(e)

b = Bill(m, o)
print(b)
