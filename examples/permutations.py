nums = [i * i for i in range(10)]
# Following logic prints n ! / (n-2) ! permutations.
n = len(nums)
pairs = []
for i in range(n):
    for j in range(i+1, n):
        pairs.append((i, j))
        pairs.append((j, i))
print("n="+str(n)+";pairs="+str(len(pairs)))
