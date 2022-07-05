
def add(a, b):
    return a + b


def output(a, b, sum):
    print(f"The sum of {a} and {b} is {sum}")


def input_two_numbers():
    a = input("Enter A")
    b = input("Enter B")
    return a, b


def main():
    a, b = input_two_numbers()
    sum = add(a, b)

    output(a, b, sum)


if __name__ == '__main__':
    main()
