fields = ['1', '  43', 4]
escaped_fields = list(map(lambda f: '`%s`' % f, fields))

print(escaped_fields)


class ga():
    pass


p = ga()

if callable(p):
    print('tt')


class A(object):
    def foo1(self):
        print(self)

    @staticmethod
    def foo2(n):
        print(n)

    @classmethod
    def foo3(cls):
        print(cls)

    def jaj(self):
        pass


a = A()

a.foo1()
a.foo3()

A.foo1(a)
A.foo3()
print(A)
