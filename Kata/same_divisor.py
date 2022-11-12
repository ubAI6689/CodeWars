import math

def count_pairs_int(diff, n_max):
    #your code here
    x = 0
    for i in range(1,n_max):
        if i + diff >= n_max:
            break
        if countDivisors(i) == countDivisors(i+diff):
            print(i, i+diff)
            x = x+1
    return x

def countDivisors(n):
    cnt=0
    for i in range(1, (int)(math.sqrt(n)) + 1):
        if (n%i == 0):
            if (n/i == i):
                cnt = cnt+1
            else:
                cnt = cnt+2
    return cnt

