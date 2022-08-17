import hashlib

def adventofcode_2015_one_part1(file):
    floor = 0
    with open(file) as f:
        contents = f.read()
        for i in contents:
            if(i=='('):
                floor +=1
            elif(i==')'):
                floor -=1
    return floor
def adventofcode_2015_one_part2(file):
    floor = 0
    count = 0
    with open(file) as f:
        contents = f.read()
        for i in contents:
            if(i=='('):
                floor +=1
            elif(i==')'):
                floor -=1
            count +=1
            if(floor == -1):
                return count

def adventofcode_2015_two_part1(file):
    paper_needed = 0
    with open(file) as f:
        for line in f:
            sides = line.strip().split('x')
            paper_needed += (2*int(sides[0])*int(sides[1])) + (2*int(sides[1])*int(sides[2])) + (2*int(sides[0])*int(sides[2])) + min(int(sides[0])*int(sides[1]),int(sides[1])*int(sides[2]),int(sides[0])*int(sides[2]))
    return paper_needed

def adventofcode_2015_two_part2(file):
    ribbon_needed = 0 
    with open(file) as f:
        for line in f:
            sides = line.strip().split('x')
            sides = [int(x) for x in sides]
            #print(sides)
            ribbon_needed += sides[0] * sides[1] * sides[2]
            sides.remove(max(sides))
            #print(sides)
            ribbon_needed += sides[0] + sides[0] + sides[1] + sides[1]
    return ribbon_needed

def adventofcode_2015_three_part1(file):
    places_been = [[0,0]]
    curr = [0,0]
    with open(file) as f:
        contents = f.read()
        for i in contents:
            if(i == '^'):
                curr[1] +=1
            elif(i == '>'):
                curr[0] +=1
            elif(i == '<'):
                curr[0] -=1
            elif(i == 'v'):
                curr[1] -=1
            if(curr not in places_been):
                places_been.append(curr.copy())
    return len(places_been)

def adventofcode_2015_three_part2(file):
    places_been = [[0,0]]
    santa_curr = [0,0]
    robo_santa_curr = [0,0]
    iterator = 0 
    with open(file) as f:
        contents = f.read()
        for i in contents:
            if(iterator%2==0):
                if(i == '^'):
                    santa_curr[1] +=1
                elif(i == '>'):
                    santa_curr[0] +=1
                elif(i == '<'):
                    santa_curr[0] -=1
                elif(i == 'v'):
                    santa_curr[1] -=1
            else:
                if(i == '^'):
                    robo_santa_curr[1] +=1
                elif(i == '>'):
                    robo_santa_curr[0] +=1
                elif(i == '<'):
                    robo_santa_curr[0] -=1
                elif(i == 'v'):
                    robo_santa_curr[1] -=1
            if(santa_curr not in places_been):
                places_been.append(santa_curr.copy())
            if(robo_santa_curr not in places_been):
                places_been.append(robo_santa_curr.copy())
            iterator +=1
    return len(places_been)

#part 1 -> 5 zeros
#part 2 -> 6 zeros 
def adventofcode_2015_four_part1_and_2(hash_val):
    five_leading_zeros = False
    starting_num = 1
    while(not five_leading_zeros):
        temp = hash_val + str(starting_num)
        our_hash = hashlib.md5(temp.encode()).hexdigest()
        if(len(our_hash) - len(our_hash.lstrip("0")) == 6):        
            return starting_num
        starting_num += 1

def adventofcode_2015_five_part1(file):
    instant_naughty = ['ab','cd','pq','xy']
    vowels = ['a','e','i','o','u']
    nice = 0
    with open(file) as f:
        for line in f:
            vowel_count = 0
            naughty = False
            twice_in_row = False  
            for i in range(len(line)-1):
                check = line[i] + line[i+1]
                if(check in instant_naughty):
                    naughty = True
                if(line[i]==line[i+1]):
                    twice_in_row = True
                if(line[i] in vowels):
                    vowel_count += 1
            if(line[-1] in vowels):
                vowel_count +=1
            if(not naughty and twice_in_row and vowel_count>=3):
                nice += 1
    return nice

def adventofcode_2015_five_part2(file):
    nice = 0
    with open(file) as f:
        for line in f:
            overlap = True
            repeat_one_letter_bwt = False
            for i in range(len(line)):
                if(i < len(line)-2):
                    if(line[i]==line[i+2]):
                        repeat_one_letter_bwt = True
                if(i < len(line)-1):
                    if(len(line) - len(line.replace(line[i]+line[i+1],''))>=4):
                        #print(line)
                        #print(line.strip(line[i]+line[i+1]))
                        overlap = False
            if(not overlap and repeat_one_letter_bwt):
                nice +=1
    return nice

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

#2015
#---------------------------------------------

#Day 1
#print(adventofcode_2015_one_part1('text_inputs/adventofcode_2015_1.txt'))
#print(adventofcode_2015_one_part2('text_inputs/adventofcode_2015_1.txt'))

#Day 2 
#print(adventofcode_2015_two_part1('text_inputs/adventofcode_2015_2.txt'))
#print(adventofcode_2015_two_part2('text_inputs/adventofcode_2015_2.txt'))

#Day 3
#print(adventofcode_2015_three_part1('text_inputs/adventofcode_2015_3.txt'))
#print(adventofcode_2015_three_part2('text_inputs/adventofcode_2015_3.txt'))

#Day 4 
#print(adventofcode_2015_four_part1_and_2('bgvyzdsv'))

#Day 5 
#print(adventofcode_2015_five_part1('text_inputs/adventofcode_2015_5.txt'))
#print(adventofcode_2015_five_part2('text_inputs/adventofcode_2015_5.txt'))

#Day 6 
#print(adventofcode_2015_six_part1('text_inputs/adventofcode_2015_6.txt'))
#print(adventofcode_2015_six_part2('text_inputs/adventofcode_2015_6.txt'))

#Day 7 
