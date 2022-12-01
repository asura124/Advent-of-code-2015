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

print(adventofcode_2015_three_part1('adventofcode_2015_3.txt'))
print(adventofcode_2015_three_part2('adventofcode_2015_3.txt'))