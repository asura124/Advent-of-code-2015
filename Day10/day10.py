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

print(adventofcode_2015_ten_part1_and_part2('1321131112'))