def accum(s):
    index=0
    res=""
    for a in s:
        index+=1
        res+=a.upper()
        for i in range(index-1):
            res+=a.lower()
        if index<len(s):
            res+='-'
    return res

print(accum('abcdef'))