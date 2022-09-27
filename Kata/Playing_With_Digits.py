def dig_pow(n, p):
    # your code
    s = str(n)
    sum=0
    for char in s:
        sum+=int(char)**p
        p+=1
    res = sum/n
    return res if sum%n==0 else -1

print(dig_pow(42688,3))

