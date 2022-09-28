def find_even_index(arr):
    sum_left=0
    sum_right=sum(arr)-arr[0]
    if sum_left==sum_right: 
        return 0
    for i in range(1,len(arr)):
        sum_left+=arr[i-1]
        sum_right-=arr[i]
        if sum_left==sum_right: 
            return i
    return -1

print(find_even_index([1,0,3,4,5,6,6,6]))
    #your code here