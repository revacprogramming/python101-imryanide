# Variables, Expressions & Statements

def calc(hrs,rate):
    return float(hrs) * float(rate)


hrs = input("Enter Hours:")
rate = input("Enter rate:")

print(f"Pay: {calc(hrs,rate)}")
