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

print(adventofcode_2015_two_part1('adventofcode_2015_2.txt'))
print(adventofcode_2015_two_part2('adventofcode_2015_2.txt'))