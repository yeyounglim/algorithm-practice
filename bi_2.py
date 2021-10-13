n, target = list(map(int, input().split()))

a = list(map(int, input().split()))

#[1,3,5,7,9,11,13,15,17,19]

def bis(a, target, s, e):
	
	while s <= e :
		
		m = (s + e) // 2
		#print (s,m,e)
		if a[m] == target:
			return m
		elif a[m] > target:
			e = m - 1
			continue
		else : 
			s = m + 1
			continue
	return None

result = bis(a, target, 0, n - 1)

if result == None :
	print("결과없음")
else :
	print (result + 1)
