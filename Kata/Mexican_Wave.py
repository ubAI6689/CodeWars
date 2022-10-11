def wave(people):
    people=people.lower()
    char=[i for i in people]
    res=[]
    for i in range(len(people)):
        if char[i]==" " and char[i-1]!=" " and i!=len(people)-1:
            char[i-1]=char[i-1].lower()
            char[i+1]=char[i+1].upper()
            continue
        if i>0: 
            char[i-1]=char[i-1].lower()
        char[i]=char[i].upper() 
        res.append("".join(char))
    return res

print(wave("Hello World"))
    