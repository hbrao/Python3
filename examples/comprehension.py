data = [1, 2, 3, 4, 5, 6, 7]

except3 = [ val for i,val in enumerate(data) if i != 3 ]
print(except3)

odds = [val for val in data if not val % 2 == 0]
print(odds)

data = [1, 'one', 2, 'two', 3, 'three', 4, 'four']
data = [val for val in data if isinstance(val, str)]
print(data)

data = 'So long and thanks for all the fish'.split()
data = [val.title() for val in data]
print(data)
