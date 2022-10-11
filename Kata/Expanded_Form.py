def expanded_form(num):
    num_str=str(num)
    res=[]
    for i, number in enumerate(num_str):
        if number=='0':
            continue
        res.append(number+(len(num_str)-i-1)*'0')
    return " + ".join(res)

print(expanded_form(123))