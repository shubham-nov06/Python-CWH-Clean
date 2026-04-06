def outer():
    print("Yo im outer")

    def inner():
        print("Yo im inner ")


outer()

inner()
