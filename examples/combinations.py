nums = [i * i for i in range(10)]
# Following logic prints n ! / 2 ! * (n-2) ! combinations.
n = len(nums)
pairs = []
for i in range(n):
    for j in range(i+1, n):
        pairs.append((i, j))
print("n="+str(n)+";pairs="+str(len(pairs)))
