n = int(input())

mv = list(map(str, input().split()))

i, j = 1, 1

for k in range(len(mv)):
	if mv[k] == "L":
		if j > 1:
			j -= 1
	if mv[k] == "R":
		if j < n:
			j += 1
	if mv[k] == "U":
		if i > 1:
			i -= 1
	if mv[k] == "D":
		if i < n:
			i += 1
print(i, j)
