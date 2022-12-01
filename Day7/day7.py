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

print(adventofcode_2015_seven_part1_and_2('adventofcode_2015_7.txt'))