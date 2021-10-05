input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1 #아스키코드값으로 숫자표현
cnt = 0

steps = [(-1,-2),(-2,-1),(1,2),(2,1),(-1,2),(1,-2),(-2,1),(2,-1)]

for step in steps:
	r = row + step[0]
	c = col + step[1]
	if r > 0 and c > 0 and r <= 8 and c <= 8:
		cnt += 1
print(cnt)
