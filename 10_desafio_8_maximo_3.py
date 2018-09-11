def maximo(x, y, z):
    if (x > y > z):
        return x
    else:
        if (y > x > z):
            return y
        else:
            return z
