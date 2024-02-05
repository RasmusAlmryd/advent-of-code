file = open('inputs/day1.txt', 'r')

lines = file.readlines()

written_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# lines = lines[3:4]
total = 0

def getMatchingSubstring(string, substring_list):
    index = -1
    for i, substring in enumerate(substring_list):
        if(substring in string):
            index = i
            break
    return index

for line in lines:
    first_letters = ''
    last_letters = ''
    first = None
    last = None

    for i in range(len(line)-1):

        first_letters = first_letters + line[i]
        last_letters = line[len(line)-i-2] + last_letters


        if(first == None):
            if(line[i].isdigit()):
                first = (line[i])

            elif(getMatchingSubstring(first_letters, written_digits) != -1):
                first = getMatchingSubstring(first_letters, written_digits) + 1

        if(last == None):
            if(line[len(line)-i-2].isdigit()):
                last = line[len(line)-i-2]
            
            elif(getMatchingSubstring(last_letters, written_digits) != -1):
                last = getMatchingSubstring(last_letters, written_digits) + 1

        if(first != None and last != None):
            break
    
    res = str(first) + '' + str(last)
    total = total + int(res)

print('Answer: ',total)
    
file.close()

