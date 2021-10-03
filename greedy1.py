#그리디 - 거스름돈 최소 개수
n = 1260 #금액

cnt = 0
ct = [500, 100, 50, 10] #거스름돈 동전 단위

for coin in ct:
	cnt += n // coin
	n %= coin
	
print(cnt)
