n, m = map(int, input().split()) 
# 3, 3

a = []
for _ in range(n):
	a.append(list(map(int, input().split())))
	
#[[0,0,1],[0,1,0],[1,0,1]]

def dfs(x, y):
	if x < 0 or x >= n or y < 0 or y >= m:
		return False
	#print(x,y)
	if a[x][y] == 0:
		a[x][y] = 1
		dfs(x - 1, y)
		dfs(x, y - 1)
		dfs(x + 1, y)
		dfs(x, y + 1)
		return True
	else:
		return False

result = 0
for i in range(n):
	for j in range(m):
		if dfs(i, j) == True:
			result += 1
	
print(result)
