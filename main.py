import words
words_database = words.words()

green_letters = []
yellow_letters = ['d','g','e']

defaults = ["BRICK","JUMPY","VOZHD","GLENT","WAQFS"]
fixed_letters = {1:'o'}

# for i in range(5):
    
#     print(f'---> Use {defaults[i]} as input {i+1}')

#     g = input('[ ] Enter green letters: ')
#     y = input('[ ] Enter yellow letters: ')
#     print()
    
#     if len(g) > 0:
#         for i in range(5):
#             if g[i] != '_':
#                 res[i] = g[i]

#     if len(y) != 0:
#         if len(y) > 1:
#             z = y.split()
#             for i in y:
#                 yellow_letters.append(i)
#         else:
#             yellow_letters.append(y)

# print('Answer: ')
# print(green_letters)
# print(yellow_letters)

temp = []

for wrd in words_database:
    
    wrd = wrd.strip()
    
    if len(fixed_letters) == 1:
        if wrd[0] == '':
            pass
    if len(fixed_letters) == 2:
        if wrd[0] == '' and wrd[1] == '':
            pass
    if len(fixed_letters) == 3:
        if wrd[0] == '' and wrd[1] == '' and wrd[2] == '':
            pass
    if len(fixed_letters) == 4:
        if wrd[0] == '' and wrd[1] == '' and wrd[2] == '' and wrd[3] == '':
            pass
    if len(fixed_letters) == 5:
        if wrd[0] == '' and wrd[1] == '' and wrd[2] == '' and wrd[3] == '' and wrd[4] == '':
            pass

print(len(temp))

for x in temp:
    wrds = list(x)
    print(wrds)

    for j in wrds:
        if j in yellow_letters:
            print('Found')
        else:
            print('Not found')

print('Yellow',yellow_letters)
