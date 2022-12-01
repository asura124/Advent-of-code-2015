import itertools


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

print(adventofcode_2015_nine_part1_and_part2('adventofcode_2015_9.txt'))