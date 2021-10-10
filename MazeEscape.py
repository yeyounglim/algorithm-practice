from collections import deque
n, m = map(int, input().split())
3, 3
a = []
for _ in range(n):
	a.append(list(map(int, input().split())))
#[[1,1,0],[0,1,0],[0,1,1]]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y):
	queue = deque() 
	queue.append((x, y))
	
	while queue:
		x, y = queue.popleft()
		#print(x, y)
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or nx >= n or ny < 0 or ny >= m:
				continue
			if a[nx][ny] == 0:
				continue
			if a[nx][ny] == 1:
				a[nx][ny] = a[x][y] + 1
				queue.append((nx, ny))
	return a[n-1][m-1]
print(bfs(0, 0))
