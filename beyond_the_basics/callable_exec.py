def sequence_class(immutable):
    return tuple if immutable else list


def class_is_callable():
    seq = sequence_class(immutable=True)
    t = seq("Hello, World")
    print(t)
    print(type(t))


class_is_callable()
