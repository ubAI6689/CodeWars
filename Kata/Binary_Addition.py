from decimal import Decimal


def add_binary(a,b):
    res=a+b
    return bin(res).replace("0b", "")

print(add_binary(3,4))