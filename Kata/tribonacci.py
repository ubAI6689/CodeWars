def tribonacci(signature, n, index=3):
    if n<=3:
        return [signature[i] for i in range(n)]
    if len(signature)==n:
        return(signature)
    else:
        new_element=signature[index-1]+signature[index-2]+signature[index-3]
        signature.append(new_element)
        return tribonacci(signature, n, index+1)
    #your code here

print(tribonacci([1, 1, 1], 10))