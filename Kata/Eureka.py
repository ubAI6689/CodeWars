import re

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    array=[i for i in range(a, b+1)]
    for i, num in enumerate(array):
        array[i]=str(num)
    
    res=[]
    for num in array:
        if len(num)==1:
            res.append(int(num))
        elif len(num)>1:
            sum=0
            for i, no in enumerate(num):
                sum+=(int(no))**(i+1)
            if sum==int(num):
                res.append(int(num))

    return res            

print(sum_dig_pow(1,100))