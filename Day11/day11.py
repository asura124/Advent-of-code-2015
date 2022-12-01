def adventofcode_2015_eleven(password):
    ascii_password = []
    bad_letters_ascii = [105,108,111] #i,l,o
    for i in password:
        ascii_password.append(ord(i))
    good_pass = False
    ascii_password = password_increment(ascii_password)
    while( not good_pass):
        straight_increase = False
        contains_bad_letters = False
        pairs = 0
        pair_index = [] 
        for i in range(len(ascii_password)):
            if(ascii_password[i] in bad_letters_ascii):
                contains_bad_letters = True
            if(i<len(ascii_password)-2):
                if(ascii_password[i+1]==ascii_password[i]+1 and (ascii_password[i+2]==ascii_password[i+1]+1)):
                    straight_increase = True
            if(i<len(ascii_password)-1):
                if(ascii_password[i]==ascii_password[i+1] and (i not in pair_index) and ((i+1) not in pair_index)):
                    pairs +=1
                    pair_index.append(i)
                    pair_index.append(i+1)
        if(pairs>=2 and not contains_bad_letters and straight_increase):
            good_pass = True
        else:
            ascii_password = password_increment(ascii_password)
    new_pass = ""
    for i in ascii_password:
        new_pass += chr(i)
    return new_pass

def password_increment(ascii_password):
    last = -1
    ascii_password[last] += 1
    while(123 in ascii_password):
        ascii_password[last] -= 26
        last -= 1
        ascii_password[last] +=1
    return ascii_password

print(adventofcode_2015_eleven('hepxcrrq'))
print(adventofcode_2015_eleven('hepxxyzz'))