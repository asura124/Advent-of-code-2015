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

print(adventofcode_2015_five_part1('adventofcode_2015_5.txt'))
print(adventofcode_2015_five_part2('adventofcode_2015_5.txt'))