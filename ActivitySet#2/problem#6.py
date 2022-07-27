from copyreg import dispatch_table


class Menu:
    def __init__(self):
        self.items = []

    def add(self, dish, price):
        t = [dish, price]
        self.items.append(t)

    def show(self):
        for i in self.items:
            dish, price = i
            print(f"{dish} {price}")


m = Menu()  # Menu is a class
m.add("idly", 10)
m.add("vada", 20)

m.show()
