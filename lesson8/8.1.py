


def oops():
    raise IndexError


def oops_2():
    try:
        oops()
    except IndexError:
        return print('oops')

oops_2()


