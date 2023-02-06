import re

dct_lat = {
    'AEIOULNSTR': 1, 'DG': 2, 'BCMP': 3,
    'FHVWY': 4, 'K': 5, 'JX': 8, 'QZ': 10
}
dct_rus = {
    'АВЕИНОРСТ': 1, 'ДКЛМПУ': 2,
    'БГЁЬЯ': 3, 'ЙЫ': 4, 'ЖЗХЦЧ': 5,
    'ШЭЮ': 8, 'ФЩЪ': 10}

word = input('Enter a word: ').upper()
if bool(re.search('[а-яА-Я]', word)):
    dct = dct_rus
else:
    dct = dct_lat

result = 0
for curr_symbol in word:
    for key in dct:
        if curr_symbol in key:
            result += dct.get(key)

print(f'Cost of word: {result}')