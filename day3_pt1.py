file = open('inputs/day3.txt', 'r')

text = file.read()

matrix = text.split('\n')

print(text)

total = 0

for y in range(len(matrix)):
    current_num = ''
    symbol_near = False

    # print('------')
    for x in range(len(matrix[0])):
        # print('(',x,',',y,')', end=',')
        
        if(matrix[y][x].isdigit()):
            current_num = current_num + matrix[y][x]
            # print(current_num, f'({x},{y})')
        else:
            # print('not digit', matrix[y][x], f'({x},{y})', symbol_near)
            if(symbol_near and current_num != ''): 
                # print('-------------',current_num)
                total = total + int(current_num)

            symbol_near = False
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
                if(not matrix[yy][xx].isalpha() and not matrix[yy][xx].isdigit() and matrix[yy][xx] != '.'):
                    symbol_near = True
                    # print('found', end='')
                    break
            # print()

    if(symbol_near and current_num != ''):
        print('2',current_num)
        total = total + int(current_num)
    symbol_near = False
    current_num = ''

print('Answer: ',total)


file.close()