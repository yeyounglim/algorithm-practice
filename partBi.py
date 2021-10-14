n = int(input())
a = list(map(int, input().split()))
#[8, 3, 7, 9, 2]
k = int(input())
b = list(map(int, input().split()))
#[5, 7, 9]

a.sort()

def bis(a, target, s, e):
	m = (s + e) // 2
	
	if s > e :
		return None
	if a[m] == target : 
		return True
	elif a[m] > target :
		return bis(a, target, s, m - 1)
	else :
		return bis(a, target, m + 1, e)

for i in range(k):
	result = bis(a, b[i], 0, n - 1)
	if result == True :
		print("yes", end=' ')
	elif result == None:
		print("no", end=' ')
