def outer():
    print("Yo im outer")

    def inner():
        print("Yo im inner ")

    inner()


outer()


def shu():
    print("My name is shubham")

    def num():
        print("My name is num")

    num()


shu()


def add(a, b):

    return a + b


print(add(3, 5))
