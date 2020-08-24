import numpy as np
import random
import matplotlib.pyplot as plt

def generate_data(size, flips_rate):
    x = np.random.uniform(-1,1,size)
    y = np.sign(np.random.rand(size) - flips_rate) * np.sign(x)
    return x, y 
    
def compute_eout(lamda, mu):
    return lamda * mu + (1 - lamda) * (1 - mu)
    
def decision_stump(x , y):
    size = x.size   
    sorted_x = np.sort(x)
    p_err = float(1)
    for i in range(size - 2):
        s = 1
        theta = float((sorted_x[i] + sorted_x[i + 1]) / 2)
        y_predict = np.sign(x - theta)
        err = float(np.sum(y != y_predict) / size)
        if err > .5:
            err = 1 - err
            s = -1
        if err < p_err or (err == p_err and random.random() > .5):
            p_s = s
            p_theta = theta
            p_err = float(err)
    return p_s, p_theta, float(p_err)

lamda = .8
size = 2000
T = 1000
all_e_in = []
all_e_out = []
e_in_out = []
for i in range(T):
    x, y = generate_data(size, .2)
    s, theta, e_in = decision_stump(x, y)
    mu = .5 + .5 * s * (abs(theta) - 1)
    e_out = compute_eout(lamda, mu)
    e_in_out.append(float(e_in) - e_out)
    all_e_in.append(float(e_in))
    all_e_out.append(float(e_out))
print('E_in average', np.average(all_e_in))
print('E_out average', np.average(all_e_out))
plt.figure()
plt.hist(e_in_out, bins = 80)
plt.savefig("p8.png")

