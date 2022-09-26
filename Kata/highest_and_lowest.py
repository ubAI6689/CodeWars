# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
def high_and_low(numbers):
    res=numbers.split()
    num=[]
    for n in res:
        num.append(int(n))
    num.sort()
    # print(num)
    return str(num[-1])+' '+str(num[0])

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))