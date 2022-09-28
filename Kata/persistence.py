def persistence(n, count=0):
    if n<10:
        return count
    else:
        s=str(n)
        res=1
        for i in s:
            res*=int(i)
        # print(res)
        n=res
        return persistence(n, count+1)
    
print(persistence(999))