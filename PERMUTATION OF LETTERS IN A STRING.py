from itertools import permutations
word = input()
ans = permutations(word)
for i in list(ans):
	print(' '.join(i))