def pos(string, x, y):
    return '\x1b[%d;%dH%s' % (y, x, string)


def cls():
    print('\x1b[2J')