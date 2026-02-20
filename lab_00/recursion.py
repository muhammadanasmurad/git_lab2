def m(x,y):
    if y == 0:
        return 0
    return x + m(x,y-1)