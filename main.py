import words
words_database = words.words()

green_letters = []
yellow_letters = []

# all alphabet letters
my_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

defaults = ["BRICK","JUMPY","VOZHD","GLENT","WAQFS"]
defaults_2 = [['b','r','i','c','k'],['j','u','m','p','y'],['v','o','z','h','d'],['g','l','e','n','t'],['w','a','q','f','s']]
fixed_letters = {}

valid_letters = ['x']

def remove_elements(x, y):
    for i in y:
        if i in x:
            x.remove(i)
    return x

expected_word = ['_','_','_','_','_']
it = 0
for i in defaults_2:
    print(f'---> Use {defaults[it]} as input {it+1}')
    g = list(input('[ ] Enter green letters: ').split())
    for j in g:
        if j in i:
            valid_letters.append(j)
    for k in range(len(g)):
        if g[k] in i:
            fixed_letters[k] = g[k]
            expected_word[k] = g[k]
    it += 1

    y = list(input('[ ] Enter yellow letters: ').split())
    for j in y:
        if j in i:
            valid_letters.append(j)
            yellow_letters.append(j)

    
print(expected_word)
print(valid_letters)
print('Yellow:',yellow_letters)
print('Fixed',fixed_letters)

final_word = []
temp = []

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


# print('Total words:',len(temp))
# print('Fixed:', fixed_letters)
# print('Yellow:', yellow_letters)
# print('Final:', final_word)
    
# last_filter = []

# temp = sorted(temp)


# print(temp)
# print(r_letters)

# count = len(yellow_letters)
# for w in temp:
#     n = 0
#     for i in w:
#         if i in yellow_letters:
#             n += 1
#     if n == count:
#         last_filter.append(w)

# print(last_filter)
# print('Total words:',len(last_filter))