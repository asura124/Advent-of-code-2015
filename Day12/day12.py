def adventofcode_2015_twelve_part1(file):
    total = 0
    curr = ""
    with open(file) as f:
        for line in f:
            for l in line:
                if(l=="-" or l.isnumeric()):
                    curr += l
                elif(curr!=""):
                    total += int(curr)
                    curr = ""
    print(total)
    return 0 

#unfinished
def adventofcode_2015_twelve_part2(file):
    bracket_arr = []
    brack_sum = 0
    total = 0
    curly_sum = 0 
    ignore = False
    with open(file) as f:
        for line in f:
            line = line.replace('"','').replace('[','[,').replace(']',',]').replace(':',',').replace('{','{,').replace('}',',}').strip('\n')
            line = line.split(',')
            for l in line:
                l = l.strip()
                print(l)
                if(l=='{'):
                    bracket_arr.append('{')
                elif(l=='['):
                    bracket_arr.append('[')
                elif(l=='}'):
                    if(ignore):
                        total += 0
                    else:
                        total = total + curly_sum + brack_sum
                    curly_sum = 0
                    brack_sum = 0 
                    bracket_arr.pop()
                    ignore = False
                elif(l==']'):
                    bracket_arr.pop()
                elif(len(bracket_arr)>0):
                    if(bracket_arr[-1]=='{' and l=='red'):
                        ignore = True
                    elif(l.strip('-').isnumeric() and bracket_arr[-1]=='{'):
                        curly_sum += int(l)
                    elif(l.strip('-').isnumeric() and bracket_arr[-1]=='['):
                        brack_sum += int(l)
                elif(l.isnumeric() and len(bracket_arr)==0):
                    total += int(l)
                #print(l,curly_sum,bracket_arr,total)
    return total


print(adventofcode_2015_twelve_part1('adventofcode_2015_12.txt'))
print(adventofcode_2015_twelve_part2('adventofcode_2015_12.txt'))