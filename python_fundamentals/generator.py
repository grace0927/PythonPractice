def gen123():
    yield 1
    yield 2
    yield 3


def gen123_exec():
    g = gen123()
    print(type(g))
    print(next(g))
    print(next(g))
    for v in gen123():
        print(v)


gen123_exec()
