import random
import matplotlib.pyplot as plt
def multi(t, w):
	ans = 0
	for i in range(5):
		ans += t[i] * w[i]
	return ans

txt = open("hw1_6_train.txt", 'r')
data = txt.readlines()
tset = []
n = 0
for line in data:
	tmp = []
	tmp.append(float(1))
	for i in line.split():
		tmp.append(float(i))
	tset.append(tmp)
	n += 1

fans = []
cnt = 0
ave = 0
while(cnt < 1126):
	random.shuffle(tset)
	step = 0
	data = txt.readlines()
	w = [0, 0, 0, 0, 0]

	correct = 0
	now  = 0
	while(correct != n):
		tmp = multi(tset[now], w)
		if tset[now][5] * tmp > 0:
			correct += 1
		else:
			for i in range(5):
				w[i] += tset[now][5] * tset[now][i]
			step += 1
			correct = 0
		now = (now + 1) % n
	
	ave += step
	fans.append(step)
	cnt += 1
ave /= 1126
print(ave)
plt.title('PLA')
plt.xlabel('number of updates')
plt.ylabel(' frequency of the number')
plt.hist(fans, bins = 100, color = 'steelblue', width = .8)
plt.savefig("p6.png")
