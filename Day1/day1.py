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

print(adventofcode_2015_one_part1('adventofcode_2015_1.txt'))
print(adventofcode_2015_one_part2('adventofcode_2015_1.txt'))