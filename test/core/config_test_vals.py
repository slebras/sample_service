def s(d):
    return dict(sorted(d.items()))


def val1(d1):
    def f(d2):
        return f'1, {s(d1)}, {s(d2)}'
    return f


def val2(d1):
    def f(d2):
        return f'2, {s(d1)}, {s(d2)}'
    return f


def fail_val(d):
    raise ValueError("we've no functions 'ere")