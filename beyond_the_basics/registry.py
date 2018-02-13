_registry = []


def registry(name):
    _registry.append(name)


def registry_names():
    return iter(_registry)
