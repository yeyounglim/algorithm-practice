n = int(input())
#3
a = []
#[15, 27, 12] 
for _ in range(n):
	a.append(int(input()))

a = sorted(a, reverse=True)

for i in range(n):
	print(a[i], end=' ')
