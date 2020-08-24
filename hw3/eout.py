import numpy as np
import matplotlib.pyplot as plt

training_set = []
testing_set = []

f = open("hw3_train.dat",'r')
lines = f.readlines()
for line in lines:
    tmp = []
    tmp.append( float(1) )
    for i in range(21):
        tmp.append( float(line.split()[i]) )
    training_set.append(tmp)
    
f = open("hw3_test.dat",'r')
lines = f.readlines()
for line in lines:
    tmp = []
    tmp.append( float(1) )
    for i in range(21):
        tmp.append( float(line.split()[i]) )
    testing_set.append(tmp)
        
train = np.array(training_set)
test = np.array(testing_set)

def sig(x):
    return 1/(1+np.exp(-x))

def cal(y, w, x):
    a = y*w.dot(x)
    b = sig(-a)
    ans = (-y*x)*b
    return ans

def error(data, w):
    s = data[:,:21].dot(w)
    result = np.sign(s)
    N = data[:,21].size
    err = 0
    for i in range(N):
        if(result[i] != data[:,21][i]):
            err += 1
    
    return err/data.shape[0]

dimension = train.shape[1] - 1
n = train.shape[0]


w = np.zeros(dimension)
ita = 0.01

graph1_e_out = []
graph2_e_out = []

for i in range(20000):
    s = np.zeros(dimension)
    for j in range(n):
        s += cal(train[j][21], w, train[j][:21])
    s = s / n
    w -= ita * s
    e_out = error(test, w)
    graph1_e_out.append(e_out)

w = np.zeros(dimension)
ita = 0.001

for i in range(20000):
    j = i % n
    s = cal(train[j][21], w, train[j][:21])
    w -= ita * s
    e_out = error(test, w)
    graph2_e_out.append(e_out)

plt.xlabel('t')
plt.ylabel('E_out')
plt.plot(graph1_e_out, 'r')
plt.plot(graph2_e_out, 'b')
my_y_ticks = np.arange(0.15, 0.6, 0.05)
plt.yticks(my_y_ticks)
plt.savefig("p8_2.png")

