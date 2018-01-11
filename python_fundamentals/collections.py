def tuple_practice():
    print("tuple Practice")

    t = ("Norway", 4.342, 4)

    for item in t:
        print(item)

    h = (381)
    print(type(h))

    k = (381,)
    print(type(k))

    print(4 in t)

def str_practice():
    print("str Practice")

    m = ' '.join(['hello', 'world'])
    print(m)

    print(m.split(' '))

    hello, _, world = m.partition(' ')
    print('{hello}, {world}'.format(hello=hello, world=world))

def range_practice():
    for i in range(5):
        print(i)

    print(list(range(5, 10)))

    print(list(range(-1, 10, 2)))

    t = [6, 12, 243, 23, 2342]
    for item in enumerate(t):
        print(item)

    for k, v in enumerate(t):
        print("k={}, v={}".format(k, v))

def list_practice():
    m = "hello world my friends are here".split(' ')
    print(m[-1])

    print(m[2:])
    print(m[:4])
    full = m[:]
    print(full)
    print(m.copy())
    print(list(m))

    k = [[3, 4], [5, 6]]
    v = k.copy()
    print(k[0] is v[0]) # they point to the same object, it shadow copy reference but not recursively
    print(k is v)
    print(k == v)
    k[0].append(1)
    print(v)


tuple_practice()
str_practice()
range_practice()
list_practice()
