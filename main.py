import words
words_database = words.words()

green_letters = []
yellow_letters = []

defaults = ["BRICK","JUMPY","VOZHD","GLENT","WAQFS"]
fixed_letters = {}

for i in range(5):
    
    print(f'---> Use {defaults[i]} as input {i+1}')

    g = input('[ ] Enter green letters: ')
    y = input('[ ] Enter yellow letters: ')
    print()
    
    if len(g) > 0:
        for i in range(5):
            if g[i] != '_':
                fixed_letters[i] = g[i]

    if len(y) != 0:
        if len(y) > 1:
            z = y.split()
            for i in y:
                yellow_letters.append(i)
        else:
            yellow_letters.append(y)

positions = []
for keys in fixed_letters.keys():
    positions.append(keys)

temp = []
temp_2 = []
final_word = ['_','_','_','_','_']

for wrd in words_database:
    wrd = wrd.strip()

    if len(fixed_letters) == 1:
        if wrd[positions[0]] == fixed_letters[positions[0]]:
            temp.append(wrd)
            final_word[positions[0]] = wrd[positions[0]]
    
    if len(fixed_letters) == 2:
        if wrd[positions[0]] == fixed_letters[positions[0]] and wrd[positions[1]] == fixed_letters[positions[1]]:
            temp.append(wrd)
            final_word[positions[0]] = wrd[positions[0]]
            final_word[positions[1]] = wrd[positions[1]]
    
    if len(fixed_letters) == 3:
        if wrd[positions[0]] == fixed_letters[positions[0]] and wrd[positions[1]] == fixed_letters[positions[1]] and wrd[positions[2]] == fixed_letters[positions[2]]:
            temp.append(wrd)
            final_word[positions[0]] = wrd[positions[0]]
            final_word[positions[1]] = wrd[positions[1]]
            final_word[positions[2]] = wrd[positions[2]]
    
    if len(fixed_letters) == 4:
        if wrd[positions[0]] == fixed_letters[positions[0]] and wrd[positions[1]] == fixed_letters[positions[1]] and wrd[positions[2]] == fixed_letters[positions[2]] and wrd[positions[3]] == fixed_letters[positions[3]]:
            temp.append(wrd)
            final_word[positions[0]] = wrd[positions[0]]
            final_word[positions[1]] = wrd[positions[1]]
            final_word[positions[2]] = wrd[positions[2]]
            final_word[positions[3]] = wrd[positions[3]]
    
    if len(fixed_letters) == 5:
        if wrd[positions[0]] == fixed_letters[positions[0]] and wrd[positions[1]] == fixed_letters[positions[1]] and wrd[positions[2]] == fixed_letters[positions[2]] and wrd[positions[3]] == fixed_letters[positions[3]] and wrd[positions[4]] == fixed_letters[positions[4]]:
            temp.append(wrd)
            final_word[positions[0]] = wrd[positions[0]]
            final_word[positions[1]] = wrd[positions[1]]
            final_word[positions[2]] = wrd[positions[2]]
            final_word[positions[3]] = wrd[positions[3]]
            final_word[positions[4]] = wrd[positions[4]]


print('Total words:',len(temp))
# print('Words:', temp)
print('Fixed:', fixed_letters)
print('Yellow:', yellow_letters)
print('Final:', final_word)

# for x in temp:
#     wrds = list(x)
#     for j in wrds:
#         if j in yellow_letters:
#             print('Found')
#         else:
#             print('Not found')
    
last_filter = []

count = len(yellow_letters)

for w in temp:
    w = list(w)
    n = 0
    for i in w:
        if i in yellow_letters:
            n += 1

    if n == count:
        last_filter.append(w)

print(last_filter)