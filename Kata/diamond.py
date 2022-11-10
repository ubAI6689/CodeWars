def diamond(n):
    if (n < 0) or (n % 2 == 0):
        return None
    
    res=""
    for i in range(1,int(n/2)+1):
        a=1+(i-1)*2
        temp=(int((n-a)/2)*" ")+a*"*"
        res=res+temp+'\n'
    
    res+=n*'*'+'\n'

    for i in reversed(range(int(n/2)+1)):
        if i==0:
            break
        a=1+(i-1)*2
        temp=(int((n-a)/2)*" ")+a*"*"
        res=res+temp+'\n'
        
    # Make some diamonds!
    return res

print(diamond(7))