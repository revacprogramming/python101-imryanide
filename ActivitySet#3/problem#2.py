class fraction:
    def __init__(self, num, den) -> None:
        self.num = num
        self.den = den

    def get_gcd(self):
        x, y = self.num, self.den
        while y:
            x, y = y, x % y
        return x

    def reduce(self):
        gcd = self.get_gcd()
        self.num = self.num // gcd
        self.den = self.den // gcd


def main():
    eglist = []
