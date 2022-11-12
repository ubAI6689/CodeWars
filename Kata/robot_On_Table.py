 
# He needs help to find out where to put his robot on a table to keep 
# it on the table for the longest.

# The size of the table is n feet by m feet (1 <= n, m <= 10000), 
# and is labeled from 1 to n (top to bottom) and from 1 to m (left to right). 
# Directions are given to the robot as a string consisting of 
# 'U', 'D', 'L', and 'R', corresponding to up, down, left, and 
# right respectively, and for each instruction given, the robot 
# moves one foot in the given direction. If the robot moves outside 
# the bounds of the table, it falls off. Your task is to find the 
# coordinates at which the robot must start in order to stay on the table for the longest.

# Return your answer as a tuple. If there are multiple solutions, 
# return the one with the smallest coordinate values.

# Example:

# robot(3, 3, "RRDLUU") => (2, 1)

def robot(n, m, s):
    x, y, xmin, ymin, xmax, ymax = 0, 0, 0, 0, 0, 0
    for cur in s:
        y += (cur=='D') - (cur=='U')
        x += (cur=='R') - (cur=='L')
        xmin = min(xmin, x)
        ymin = min(ymin, y)
        xmax = max(xmax, x)
        ymax = max(ymax, y)
        if xmax - xmin + 1 > m or ymax - ymin + 1 > n:
            xmin += cur=='L'
            ymin += cur=='U'
            break
    return 1 - ymin, 1 - xmin

print(robot(3, 3, "RRDLUU"))


