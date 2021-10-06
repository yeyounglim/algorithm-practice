n, m = 5,5 #map(int, input().split())
x, y, dir = 1,1,0#map(int, input().split())
d = [[0] * m for _ in range(n)]

arr = [[1,1,1,1, 1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1, 1]]#[]
#for _ in range(n):
	#arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def d_turn():
	global dir 
	dir -= 1
	if dir < 0: dir = 3

d[x][y] = 1
turn_cnt = 0
cnt = 1
while True :
	d_turn()
	nx = x + dx[dir]
	ny = y + dy[dir]
	print(cnt)
	if d[nx][ny] == 0 and arr[nx][ny] == 0:
		d[nx][ny] = 1
		dir -= 1
		x = nx
		y = ny
		cnt += 1
		turn_cnt = 0
		print(nx,ny)
		continue
	else :
		turn_cnt += 1	
	
	if turn_cnt == 4: 
		nx = x - dx[dir]
		ny = y - dy[dir]
		if arr[nx][ny] == 0:
			x= nx
			y=ny
		else: break
		turn_cnt = 0
print(cnt)
