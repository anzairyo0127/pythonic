'''

names = ['Cecilia', 'Lise', 'Marie',
         'TobbyFox', 'Dragoninstall', 'hogepiyoman']

letters = [len(le) for le in names]
print(names)
print(letters)

'''

names = ['Cecilia', 'Lise', 'Marie']
letters = [len(le) for le in names]


longest_name = None
max_letters = 0

names.append('Rosalind')

for count, name in zip(letters, names):
    print(name, count)
print(names)
