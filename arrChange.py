n, k = map(int, input().split())
#5, 3
a = list(map(int, input().split())) #[1, 2, 5, 4, 3]
b = list(map(int, input().split())) #[5, 5, 6, 6, 5]

a.sort()
b.sort(reverse=True)

for i in range(k):
	if a[i] < b[i]:
		a[i], b[i] = b[i], a[i]
	else : break

print(sum(a))
