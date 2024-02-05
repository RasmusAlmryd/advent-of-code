file = open('inputs/day4.txt', 'r')

lines = file.readlines()

total = 0
for line in lines:
    temp = line.split(':')[1].split('|')
    winning = temp[0].split()
    picked_numbers = temp[1].split()
    # print(winning, chosen)
    count = 0
    for number in picked_numbers:
        for winner in winning:
            if(number == winner):
                count += 1 
                break
    
    if(count > 0):
        total += pow(2, count-1)

print('Answer: ',total)

file.close()