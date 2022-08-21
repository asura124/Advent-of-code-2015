import hashlib
import itertools

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

def adventofcode_2015_seven_part1_and_2(file):
    our_var = {}
    while('a' not in our_var):
        with open(file) as f:
            for line in f:
                line = line.replace('-> ','').strip('\n').split(' ')
                if(len(line)==2 and line[0].isnumeric()):
                    our_var[line[1]] = int(line[0]) 
                elif(len(line)==2 and not line[0].isnumeric() and line[0] in our_var):
                    our_var[line[1]] = int(our_var[line[0]])
                elif(len(line)==3 and not line[0].isnumeric() and line[1] in our_var):
                    our_var[line[2]] = 65535 - int(our_var[line[1]])
                elif(len(line)==4 and line[1]=='RSHIFT' and line[2].isnumeric() and line[0] in our_var):
                    our_var[line[3]] = our_var[line[0]] >> int(line[2])
                elif(len(line)==4 and line[1]=='LSHIFT' and line[2].isnumeric() and line[0] in our_var):
                    our_var[line[3]] = our_var[line[0]] << int(line[2])
                elif(len(line)==4 and line[1]=='AND' and line[0].isnumeric() and line[2] in our_var):
                    our_var[line[3]] = int(line[0]) & our_var[line[2]]
                elif(len(line)==4 and line[1]=='AND' and line[2].isnumeric() and line[0] in our_var):
                    our_var[line[3]] = int(line[2]) & our_var[line[0]]
                elif(len(line)==4 and line[1]=='AND' and line[0] in our_var and line[2] in our_var):
                    our_var[line[3]] = our_var[line[0]] & our_var[line[2]]
                elif(len(line)==4 and line[1]=='OR' and line[0].isnumeric() and line[2] in our_var):
                    our_var[line[3]] = int(line[0]) | our_var[line[2]]
                elif(len(line)==4 and line[1]=='OR' and line[2].isnumeric() and line[0] in our_var):
                    our_var[line[3]] = int(line[2]) | our_var[line[0]]
                elif(len(line)==4 and line[1]=='OR' and line[0] in our_var and line[2] in our_var):
                    our_var[line[3]] = our_var[line[0]] | our_var[line[2]]
    return our_var['a']

def adventofcode_2015_eight_part1(file):
    str_literal = 0 #just len of str
    char_memory = 0 #actual
    with open(file) as f:
        for line in f:
            line = line.strip('\n')
            str_literal += (len(line))
            char_memory += count_string(line)
    return str_literal - char_memory

def count_string(string):
    hex =['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    curr_len = 0
    string = string.lstrip('"')[:-1]
    print(string)
    pos = 0 
    while(pos<len(string)):
        if(string[pos]!="\\"):
            curr_len +=1
        else:
            if(string[pos+1]!='x'):
                curr_len +=1
                pos+=1
            elif(string[pos+1]=='x' and (string[pos+2] in hex) and (string[pos+3] in hex)):
                curr_len +=1
                pos +=3
        pos +=1
    return curr_len

def adventofcode_2015_eight_part2(file):
    str_literal = 0 #just len of str
    new_encode = 0 
    with open(file) as f:
        for line in f:
            line = line.strip('\n')
            str_literal += (len(line))
            line = line.lstrip('"')[:-1] #+6
            for i in line:
                if(i.isalpha() or i.isnumeric()):
                    new_encode +=1
                else:
                    new_encode +=2
            new_encode += 6 #from the stripped "" 
    return new_encode - str_literal 

def adventofcode_2015_nine_part1_and_part2(file):
    location_1 =[]
    location_2 =[]
    distance = []
    starting_unique_locations = [] 
    with open(file) as f:
        for line in f:
            line = line.strip('\n').replace('to ','').replace('= ','').split(' ')
            if(line[0] not in starting_unique_locations):
                starting_unique_locations.append(line[0])
            if(line[1] not in starting_unique_locations):
                starting_unique_locations.append(line[1])
            location_1.append(line[0])
            location_2.append(line[1])
            distance.append(int(line[2]))
    comb = list(itertools.permutations(starting_unique_locations))
    total_distances = []
    for i in comb:
        curr_dis = 0
        for city in range(len(i)-1):
            for k in range(len(location_1)):
                if((i[city]==location_1[k] and i[city+1]==location_2[k]) or (i[city]==location_2[k] and i[city+1]==location_1[k])):
                    curr_dis += distance[k]
        total_distances.append(curr_dis)
    return min(total_distances) #return max(total_distances) for part 2

def adventofcode_2015_ten_part1_and_part2(code):
    for i in range(40): #change to 50 for part 2 
        count = 1
        temp = ""
        for j in range(len(code)-1):
            if(code[j]==code[j+1]):
                count+=1
            else:
                temp = temp + str(count) + code[j]
                count = 1
        #print(count)
        temp = temp + str(count) + code[-1]
        code = temp
        #print(temp) 
    return len(code)
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
#print(adventofcode_2015_seven_part1_and_2('text_inputs/adventofcode_2015_7.txt'))

#Day 8 
#print(adventofcode_2015_eight_part1('text_inputs/adventofcode_2015_8.txt'))
#print(adventofcode_2015_eight_part2('text_inputs/adventofcode_2015_8.txt'))

#Day 9 
#print(adventofcode_2015_nine_part1_and_part2('text_inputs/adventofcode_2015_9.txt'))

#Day 10 
#print(adventofcode_2015_ten('1'))
print(adventofcode_2015_ten_part1_and_part2('1321131112'))
