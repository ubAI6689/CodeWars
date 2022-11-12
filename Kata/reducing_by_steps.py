import math

def gcdi(a, b):
    return math.gcd(int(a),int(b))
#     # your code
#     # implementing eucledian algo
#     smaller = mini(a, b)
#     bigger = maxi(a, b)

#     while (bigger%smaller!=0):
#         gcdi(smaller, bigger%smaller)
    
#     return smaller

def lcmu(a, b):
    # your code
    return int(abs(a*b)/gcdi(a,b))

def som(a, b):
    # your code
    return a+b

def maxi(a, b):
    # your code
    return max(a, b)

def mini(a, b):
    # your code
    return min(a, b)

def oper_array(fct, arr, init):
    # your code
    res=[]
    for i in range(len(arr)):
        init = fct(init,arr[i])
        res.append(init)
        # init=res[i]
    return res

        
a = [ 18, 69, -90, -78, 65, 40 ]
r = [ 18, 3, 3, 3, 1, 1 ]
op = oper_array(gcdi, a, a[0])
# testing(op, r)
# r = [ 18, 414, 2070, 26910, 26910, 107640 ]
# op = oper_array(lcmu, a, a[0])
# testing(op, r)
# r = [ 18, 87, -3, -81, -16, 24 ]
# op = oper_array(som, a, 0)
# testing(op, r)
# r = [ 18, 18, -90, -90, -90, -90 ]
# op = oper_array(mini, a, a[0])
# testing(op, r)
# r = [ 18, 69, 69, 69, 69, 69 ]
# op = oper_array(maxi, a, a[0])
# testing(op, r)
print(r)
print(op)
if op == r:
    print("YEAY")
else:
    print("Fvck")