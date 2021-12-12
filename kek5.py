import numpy as np
# import sys
# np.set_printoptions(threshold=sys.maxsize)

def get_size():
    xmax=0
    ymax=0
    lines_out=0
    with open("/Users/patri/Desktop/input5.txt", "r") as f:
        while True:
            buffer= f.readline().rstrip().split()
            if not buffer: break
            buffer.pop(1)
            output = list()
            for item in buffer:
                output.append(item.split(','))
            output= sum(output, [])
            for i in range(0,3,2):
                if int(output[i],10) >xmax: xmax=int(output[i],10)
            for i in range(1,4,2):
                if int(output[i],10) >ymax: ymax=int(output[i],10)
            lines_out+=1
    return list([xmax, ymax]), lines_out

def update_grid(cords_input, grid): #output index tuples
    line_output = 0
    y_line=[]
    x_line=[]
    x1 = int(cords_input[0],10)
    x2 = int(cords_input[2],10)
    y1 = int(cords_input[1],10)
    y2 = int(cords_input[3],10)
    #determine if hor or ver line
    #if x1=x2 then ver line and vice verse
    #enough to check once
    if x1==x2:
        #determine direction and fill line
        if y1<=y2:
            y_line =list(range(y1,y2+1,1))
        else:
            y_line = list(range(y1,y2-1,-1))
        for i in y_line:
            grid[i,x1]=grid[i,x1]+ 1
            #print('grid val:',grid[i,x1], ' i=', i, ' x1=',x1 )
    else:
        if x1<=x2:
            x_line =list(range(x1,x2+1,1))
        else:
            x_line = list(range(x1,x2-1,-1))
        for i in y_line:
            grid[y1,i]=grid[y1,i]+1

    return grid


buffer=[]
output=0

#find max x and y coordinate
max_cords, lines_to_read = get_size()

#make main grid
grid = np.zeros((max_cords[1]+1,max_cords[0]+1), dtype=int)

with open("/Users/patri/Desktop/input5.txt", "r") as f:
    for i in range(lines_to_read):
        buffer= f.readline().rstrip().split()
        buffer.pop(1) #remove '->'
        sample = list()
        for item in buffer:
            sample.append(item.split(','))
        sample= sum(sample, [])
        grid = update_grid(sample,grid)
        i+=1

#remains to count overlapping coordinates
for i in range(max_cords[1]+1):
    for k in range(max_cords[0]+1):
        if grid[i,k]>1:
            output+=1
            print(grid[i,k])


print('output:',output)
