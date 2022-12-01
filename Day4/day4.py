import hashlib
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

print(adventofcode_2015_four_part1_and_2('bgvyzdsv'))