from itertools import permutations
s, n = input().split()
for j in permutations(sorted(s),int(n)):
    print(''.join(j))
