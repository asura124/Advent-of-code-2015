def adventofcode_2015_six_part1(file):
    #lights = [[0]*10] * 10 #shallow list: causes column for value to change rather than 1 element
    lights = [[0 for i in range(1000)] for j in range(1000)]
    with open(file) as f:
        for line in f:
            line = line.replace('through ',"").strip('\n').split(' ')
            if(line[0] == 'turn' and line[1]=='on'):
                start = line[2].split(',')
                end = line[3].split(',')
                #print(start)
                #print(end)
                for i in range(int(start[0]),int(end[0])+1):
                    for j in range(int(start[1]),int(end[1])+1):
                        lights[i][j] = 1
            elif(line[0] == 'turn' and line[1]=='off'):
                start = line[2].split(',')
                end = line[3].split(',')
                #print(start)
                #print(end)
                for i in range(int(start[0]),int(end[0])+1):
                    for j in range(int(start[1]),int(end[1])+1):
                        lights[i][j] = 0
            elif(line[0] == 'toggle'):
                start = line[1].split(',')
                end = line[2].split(',')
                #print(start)
                #print(end)
                for i in range(int(start[0]),int(end[0])+1):
                    for j in range(int(start[1]),int(end[1])+1):
                        if(lights[i][j]==1):
                            lights[i][j]=0
                        else:
                            lights[i][j]=1
    on_counter = 0
    #print(lights)
    for i in lights:
        for j in i:
            if(j==1):
                on_counter +=1
    return on_counter

def adventofcode_2015_six_part2(file):
    lights = [[0 for i in range(1000)] for j in range(1000)]
    with open(file) as f:
        for line in f:
            line = line.replace('through ',"").strip('\n').split(' ')
            #print(line)
            if(line[0] == 'turn' and line[1]=='on'):
                start = line[2].split(',')
                end = line[3].split(',')
                #print(start)
                #print(end)
                for i in range(int(start[0]),int(end[0])+1):
                    for j in range(int(start[1]),int(end[1])+1):
                        lights[i][j] +=1
            elif(line[0] == 'turn' and line[1]=='off'):
                start = line[2].split(',')
                end = line[3].split(',')
                #print(start)
                #print(end)
                for i in range(int(start[0]),int(end[0])+1):
                    for j in range(int(start[1]),int(end[1])+1):
                        if(lights[i][j]>0):
                            lights[i][j] -=1
            elif(line[0] == 'toggle'):
                start = line[1].split(',')
                end = line[2].split(',')
                #print(start)
                #print(end)
                for i in range(int(start[0]),int(end[0])+1):
                    for j in range(int(start[1]),int(end[1])+1):
                        lights[i][j] +=2
    total_bright = 0
    for i in lights:
        for j in i:
            total_bright += j
    return total_bright 


print(adventofcode_2015_six_part1('adventofcode_2015_6.txt'))
print(adventofcode_2015_six_part2('adventofcode_2015_6.txt'))