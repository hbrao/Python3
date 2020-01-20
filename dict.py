vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Provide a word to search for ovals: ')

found = {}
for c in list(word):
    if c in vowels:
        found.setdefault(c, 0)
        found[c] += 1

for k, v in sorted(found.items()):
    print('Found {} vowel {} times'.format(k, v))
