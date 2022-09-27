def delete_nth(order, max_e):
    myDict={}
    res=[]
    for n in order:
        if n in myDict.keys():
            myDict[n]+=1
        else:
            myDict[n]=1
        if myDict[n]<=max_e:
            res.append(n)
    return res

print(delete_nth([20,37,20,21], 1))