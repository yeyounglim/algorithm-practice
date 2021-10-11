n = int(input())#2

a = [] #[('홍길동',95),('이순신',77)]
for i in range(n):
	id = input().split()
	a.append((id[0], int(id[1])))

a = sorted(a, key=lambda s: s[1])

for s in a:
	print(s[0], end = ' ')
