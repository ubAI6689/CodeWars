def tower_builder(n_floors):
    base=1+2*(n_floors-1)
    res=[]
    for i in range(n_floors):
        floor=""
        floor+=int((base-(1+2*i))/2)*' '
        floor+=(1+2*i)*"*"
        floor+=int((base-(1+2*i))/2)*' '
        res.append(floor)
    return res
        # print((1+2*i)*"*")
        # print((int(n_floors/2)-1-i)*" ")
    # build here
    # 1+2n
print(tower_builder(3))