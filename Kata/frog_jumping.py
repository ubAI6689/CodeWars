def solution(a):
    # your code here
    path=[]
    current_index=0
    path.append(current_index)
    jump=a[current_index]
    cnt=1
    while(current_index + jump < len(a) and current_index + jump >= 0):
        current_index = current_index + jump
        if current_index in path:
            return -1
        else:
            path.append(current_index)
            jump = a[current_index]
            cnt+=1
    return cnt

print(solution([1, 2, 2, -1]))



