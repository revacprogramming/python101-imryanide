# Functions


def computepay(h, r):
    return (r*h if h<40 else ((h-40)*(r*1.5)+(40*r)))


hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))

p = computepay(hrs, rte)
print("Pay", p)
