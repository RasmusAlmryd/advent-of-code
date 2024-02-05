

file = open('inputs/day1.txt', 'r')

lines = file.readlines()

total = 0

for line in lines:
    first = None
    last = None

    for i in range(len(line)-1):

        if(first == None and line[i].isdigit()):
            first = (line[i])

        if(last == None and line[len(line)-i-2].isdigit()):
            last = (line[len(line)-i-2])

        if(first != None and last != None):
            break
    
    res = first + '' + last

    total = total + int(res)

print('Answer: ',total)
    
file.close()