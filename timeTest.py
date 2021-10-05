hour = int(input())
min = 60
sec = 60
cnt = 0

for h in range(hour + 1):
	for m in range(min):
		for s in range(sec):
			time = str(h) + str(m) + str(s)
			
			if '3' in time:
				cnt += 1
print(cnt)
