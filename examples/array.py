from copy import copy, deepcopy

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(4):
    plist.pop()
plist.pop(0)

plist.extend([plist.pop(), plist.pop()])

plist.remove('\'')

plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

a = [1, 2, 3]
c = a
b = copy(a)
a.append(4)
print(b)
print(c)

nums = [i for i in range(10)]
k = 3
n = len(nums)
prev = nums[0]
for i in range(0, n * k, k):
    pos = (i + k) % n
    print("Replacing " + str(nums[pos]) + " with " + str(prev))
    prev, nums[pos] = nums[pos], prev
print(nums)
