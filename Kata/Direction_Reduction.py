import enum


def dirReduc(arr):
    for index, direction in enumerate(arr):
        # print(len(arr))
        if index==len(arr)-1:
            if len(arr)>1:
                index=0
            else:
                break
        if ((arr[index]=="NORTH" and arr[index+1]=="SOUTH")
        or (arr[index]=="SOUTH" and arr[index+1]=="NORTH")
        or (arr[index]=="EAST" and arr[index+1]=="WEST")
        or (arr[index]=="WEST" and arr[index+1]=="EAST")):
            arr.remove(arr[index])
            arr.remove(arr[index])
            index=0
    return arr

a = ['EAST', 'EAST', 'NORTH', 'WEST']
print(dirReduc(a))
        