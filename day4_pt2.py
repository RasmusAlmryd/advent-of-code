
file = open('inputs/day4.txt', 'r')

lines = file.readlines()

cards = {}

total = 0
i = 0

for line in lines:
    name = line.split(':')[0].split()
    print(name)
    temp = line.split(':')[1].split('|')
    winners = temp[0].split()
    picked = temp[1].split()

    cards[f'{name[0]} {name[1]}'] = {'winners': winners, 'picked': picked, 'copies': 0}

    
for card in cards:
    winners = cards[card]['winners']
    picked = cards[card]['picked']
    copies = cards[card]['copies']
    count = 0
    for number in picked:
        for winner in winners:
            if(number == winner):
                count += 1 
                break

    card_num = int(card.split()[1])

    for i in range(card_num+1, card_num+count+1):
        cards[f'Card {i}']['copies'] += copies + 1
    
    total += 1 + copies

print('Answer: ',total)