file = open('inputs/day2.txt', 'r')

lines = file.readlines()
# lines = lines[0:1]

total_ids = 0
for i, line in enumerate(lines):
    max_red = 0
    max_blue = 0
    max_green = 0
    
    
    cube_sets = line.split(':')[1]
    cube_sets = cube_sets.split(';')

    for cube_set in cube_sets:
        cube_vals = cube_set.split(',')
        for cube_val in cube_vals:
            value, color = cube_val.split()

            if(color == 'red'):
                max_red = max([max_red, int(value)])
            elif(color == 'blue' ):
                max_blue = max([max_blue, int(value)])
            elif(color == 'green'):
                max_green = max([max_green, int(value)])
        
    if(max_red <=12 and max_green <=13 and max_blue <= 14):
        total_ids = total_ids + i + 1

print('Answer: ',total_ids)
file.close()