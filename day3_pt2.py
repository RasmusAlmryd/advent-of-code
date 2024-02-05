file = open('inputs/day3.txt', 'r')

text = file.read()

matrix = text.split('\n')

print(text)

gear_list = []

total = 0

for y in range(len(matrix)):
    current_num = ''
    symbol_near = None

    # print('------')
    for x in range(len(matrix[0])):
        # print('(',x,',',y,')', end=',')
        
        if(matrix[y][x].isdigit()):
            current_num = current_num + matrix[y][x]
            # print(current_num, f'({x},{y})')
        else:
            # print('not digit', matrix[y][x], f'({x},{y})', symbol_near)
            if(symbol_near != None and current_num != ''): 
                # print('-------------',current_num)
                # total = total + int(current_num)
                gear_list.append([int(current_num), symbol_near])
            symbol_near = None
            current_num = ''
            continue
        

        x_start = max([0, x-1])
        x_end = min([len(matrix[0])-1, x+1])
        y_start = max([0, y-1])
        y_end = min([len(matrix)-1, y+1])

        # print(f'cell: ({x},{y})')
        for yy in range(y_start, y_end+1):
            for xx in range(x_start, x_end+1):
                # print(f'({xx},{yy})', end= '')
                if(matrix[yy][xx] == '*'):
                    symbol_near = [xx,yy]
                    # print('found', end='')
                    break
            # print()

    if(symbol_near != None and current_num != ''):
        # print('2',current_num)
        # total = total + int(current_num)
        gear_list.append([int(current_num), symbol_near])
    symbol_near = None
    current_num = ''

already_counted = []
for i, gear_val in enumerate(gear_list):
    if(gear_val[1] in already_counted): continue
    already_counted.append(gear_val[1])
    count = 1
    gear_ratio = gear_val[0]
    for j, gear_val2 in enumerate(gear_list):
        if(j != i and gear_val2[1] == gear_val[1]):
            count += 1
            gear_ratio *= gear_val2[0]

    if(count == 2):
        total += gear_ratio

# print(already_counted)
# print(gear_list)
print('Answer: ',total)


file.close()
            