def inherits_from(obj, a_class):
    return isinstance(obj, type) and issubclass(obj, a_class)
