import random
import matplotlib.pyplot as plt

def multi(t, w):
	ans = 0
	for i in range(5):
		ans += t[i] * w[i]
	return ans

def errorRate(t, w, n):
	eR = .0
	for i in range(n):
		tmp = multi(t[i], w)
		if not tmp * t[i][5] > 0:
			eR += 1
	return eR / n

txt = open("hw1_7_train.txt", 'r')
data = txt.readlines()
trset = []
n = 0
for line in data:
	tmp = []
	tmp.append(float(1))
	for i in line.split():
		tmp.append(float(i))
	trset.append(tmp)
	n += 1

m = 0
txt = open("hw1_7_test.txt", 'r')
data = txt.readlines()
tset = []
for line in data:
	tmp = []
	tmp.append(float(1))
	for i in line.split():
		tmp.append(float(i))
	tset.append(tmp)
	m += 1

fans = []
cnt = 0
ave = .0
while(cnt < 1126):
	random.shuffle(trset)
	w = [.0, .0, .0, .0, .0]
	pocket = [.0, .0, .0, .0 , .0]

	time = 0
	now  = 0
	while(time < 100):
		tmp = multi(trset[now], w)
		if not trset[now][5] * tmp > 0:
			for i in range(5):
				w[i] += trset[now][5] * trset[now][i]
			if errorRate(trset, w, n) < errorRate(trset, pocket, n):
				for i in range(5):
					pocket[i] = w[i]
			time += 1
		now = (now + 1) % n
	tError = errorRate(tset, pocket, m)
	fans.append(tError)
	ave += tError
	cnt += 1
ave /= 1126
print(ave)
plt.title('Pocket P7')
plt.xlabel('error rate')
plt.ylabel(' frequency of the number')
plt.hist(fans, bins = 100, color = 'steelblue')
plt.savefig("p7.png")
