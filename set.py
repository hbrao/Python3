vowels = set('aeiou')
word = input('Provide a word to search for ovels: ')

found = vowels.intersection(set(word))

for k in sorted(found):
   print('Found {} vowel'.format(k))
