def maximo(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z

x = int(input())
y = int(input())
z = int(input())

maximo(x, y, z)