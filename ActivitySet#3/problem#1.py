from mimetypes import init


class vertice:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class rectangle:
    def __init__(self, vertices):
        self.v1, self.v2, self.v3 = vertices
        self.l, self.b = self.get_atts()

    def get_atts(self):
        x = ((self.v2.x - self.v1.x) ** 2 + (self.v2.y - self.v1.y) ** 2) ** 0.5
        y = ((self.v2.x - self.v1.x) ** 2 + (self.v2.y - self.v1.y) ** 2) ** 0.5
        z = ((self.v2.x - self.v1.x) ** 2 + (self.v2.y - self.v1.y) ** 2) ** 0.5

        if x >= y and x >= z:
            return y, z
        elif y >= z:
            return x, z
        else:
            return x, y

    def get_area(self):
        return self.l * self.b


def inp_vert():
    x = float(input("Enter X : "))
    y = float(input("Enter Y : "))
    v = vertice(x, y)
    return v


def inp_rect():
    vl = []
    for i in range(3):
        vl.append(inp_vert())
    r = rectangle(vl)
    return r


def inp_rects() -> list:
    n = int(input("Enter no. of rectangles"))
    rects = []
    for i in range(n):
        rects.append(inp_rect())
    return rects


def output(rects):
    for r in rects:
        print(
            f"Area of rectangle with vertices ({r.v1.x},{r.v1.y}),({r.v2.x},{r.v2.y}),({r.v3.x},{r.v3.y}) is {round(r.get_area(),1)}"
        )


def main():
    r = inp_rects()
    output(r)


if __name__ == "__main__":
    main()
