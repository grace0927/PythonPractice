from itertools import count, islice


from fundamentals.comprehensions import is_prime


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


def take(count, iterable):
    """Take the first count element"""
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item

def run_take():
    print("testing take:")
    items = [2, 4, 6, 8]
    for item in take(3, items):
        print(item)


def distinct(iterable):
    """Return unique items by eliminating duplicates.

    Args:
        iterable: the source series.

    Yields:
        unique elements in order from 'iterable'.
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_distinct():
    print("testing distinct:")
    items = [1, 7, 5, 7, 3, 5, 5]
    for item in distinct(items):
        print(item)

def run_pipeline():
    print("testing pipeline:")
    items = [3, 1, 3, 5, 1, 10, 7]
    for item in take(3, distinct(items)):
        print(item)


def tool_exec():
    print("itertools exec:")
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print(thousand_primes)
    print(list(thousand_primes))
    print(sum(islice((x for x in count() if is_prime(x)), 1000)))
    print(any([False, True, False]))
    print(all([False, True, True]))
    monday = [12, 3, 13, 4, 2, 12, 24]
    sunday = [13, 4, 3, 4, 5, 20, 33]
    for item in zip(monday, sunday):
        print(item)
    for mon, sun in zip(monday, sunday):
        print("average = {}".format((mon + sun) / 2.0))


if __name__ == "__main__":
    gen123_exec()
    run_take()
    run_distinct()
    run_pipeline()
    tool_exec()
