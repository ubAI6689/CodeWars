def remove_every_other(my_list):
    copy_list=[i for i in my_list]
    for i, element in enumerate(copy_list):
        if (i+1)%2==0:
            my_list.remove(element)
    return my_list

print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))