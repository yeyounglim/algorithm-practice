n, k = map(int, input().split()) # 4, 6
a = list(map(int, input().split()))
#[19, 15, 10, 17]  


def bis(a, target, s, e):
	
	while True :
		cut = 0
		m = (s + e) // 2
		
		for i in range(n):
			if a[i] >= m:
				cut += a[i] - m
		if s > e :
			return None
		if cut == target :
			break
		elif cut < target :
			e = m - 1 
		else :
			s = m + 1
	return m

result = bis(a, k , 0, max(a) - 1)
if result == None:
	print("none")
else: 
	print(result)
