a = (1, 3, 56, 7, 8)


class haha():
    def __init__(self, l):
        self.strl = l + l

    def __enter__(self):
        return self.strl

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("end")


with haha("1") as file:
    print("few" + str(file))
