import pprint

file = open('inputs/day5.txt', 'r')

lines = file.readlines()


current_label = lines[0].split(':')[0]
current_numbers = lines[0].split(':')[1].split()
translation_array = []


def get_translation(translation_arr, number):
    for translation in translation_arr:
        [dest_range,src_range,range_len] = translation

        if(number >= src_range and number < src_range+range_len):
            return dest_range+(number-src_range)

    return number

print(current_numbers)
index = 1
for line in lines[3:]:
    if(':' in line):
        # print(line.split(':')[0], 1)
        for i, num in enumerate(current_numbers):
            current_numbers[i] = get_translation(translation_array, int(num))
            
        # if(index >= 1): break
        # index+= 1
        # print(current_numbers)
        translation_array = []
        continue

    elif(line == '\n'):
        # print('empty line')
        continue

    translation_array.append([int(str_num) for str_num in line.split()])
    # [dest_range,src_range,range_len] = [int(str_num) for str_num in line.split()]
    # print(line, end='')
    # print(a,b,c)

    # for i in range(range_len):
    #     # print(src_range+i, dest_range+i)
    #     translation_dict[src_range+i] = dest_range+i

for i, num in enumerate(current_numbers):
    current_numbers[i] = get_translation(translation_array, int(num))
    
# pprint.pprint(translation_dict)
print(current_numbers)
print(min(current_numbers))

file.close()