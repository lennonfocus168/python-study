def add_end(L=[]):
    print("l=%s" % L)
    L.append('END')
    return L


def add_str(L=None):
    print("l=%s" % L)
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())

print("---------------")
print(add_str())
print(add_str())

print("---------------")
