import AND, NAND, OR

def XOR(x1, x2):
    s1 = NAND.NAND(x1, x2)
    s2 = OR.OR(x1, x2)
    y = AND.AND(s1, s2)
    return y


