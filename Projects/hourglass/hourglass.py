from array import *

arr=[[1,1,1,0,0,0], [0,1,0,0,0,0], [1,1,1,0,0,0],
     [0,0,2,4,4,0],[0,0,0,2,0,0], [0,0,1,2,4,0]]

i_max = None
for i in range(4):
    for j in range(4):
        current = arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
                  arr[i+1][j+1] + \
                  arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if i_max == None or current > i_max:
            i_max = current
print(i_max)