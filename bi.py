def bis(a, target, s, e):
	
	if s > e:
		return None
	
	m = (s + e) // 2
	
	if a[m] == target :
		return m
	elif a[m] > target :
		return bis(a, target, s, m - 1)
		
	else :
		return bis(a, target, m + 1, e)

n ,target = list(map(int,input().split()))
a = list(map(int,input().split()))

result = bis(a, target, 0, n - 1)

if result == None : 
	print("원소없음")
else :
	print(result + 1)
