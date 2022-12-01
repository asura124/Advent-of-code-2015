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

print(adventofcode_2015_eight_part1('adventofcode_2015_8.txt'))
print(adventofcode_2015_eight_part2('adventofcode_2015_8.txt'))