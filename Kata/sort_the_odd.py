def sort_array(source_array):
    n=[i for i in source_array if i%2!=0]
    n.sort(reverse=True)
    for i,a in enumerate(source_array):
        if a%2!=0:
            source_array[i]=n.pop()
    return source_array

    