import re

inst = input() # 'K1KA5CB7'
fstr = re.compile('[^0-9]')

num = re.findall(r'\d', inst)
num = sum(list(map(int, num)))
str1 = "".join(sorted(fstr.findall(inst)))

print(str1 + str(num))
