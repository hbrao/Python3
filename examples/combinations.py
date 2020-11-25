nums = [i * i for i in range(10)]
# Following logic prints n ! / k ! * (n-k) ! combinations where k=2.
n = len(nums)
pairs = []
for i in range(n):
    for j in range(i+1, n):
        pairs.append((i, j))
print("n="+str(n)+";pairs="+str(len(pairs)))
