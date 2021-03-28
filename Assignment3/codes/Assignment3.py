import random 
import numpy as np
from matplotlib import pyplot as plt

#a function that calculates the probability for a random m value
def get_probability(num_samples, r):
    i=0
    t=0

    m = (1 if random.random() > 0.5 else -1) * random.randint(-10000,10000)
    while i<num_samples:
        mult = 1 if random.random() > 0.5 else -1
        X = random.random()*r*mult
        Y = random.random()*r*mult
        if Y>=m*X:
            t=t+1
        i=i+1
    return t/num_samples

su_ = 0
num_samples = 10000
ite = 10

#calculating the probability 'ite' times by generating 'num_samples' points (X,Y)
for i in range(ite):
    cur = get_probability(num_samples, 10)
    su_ += cur
prob = su_/ite
print('probability: ',prob)

#plotting the graphs 
prob_plot = []
prob_cal = []
for x in range(5):
    prob_plot.append(get_probability(num_samples, 10))
    prob_cal.append(1/2)

labels = [1, 2, 3, 4, 5]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, prob_plot, width)
rects2 = ax.bar(x + width/2, prob_cal, width)
plt.ylim(0,0.75)
ax.set_ylabel('Probability')
ax.set_title('Simulation vs Theoretical')
# ax.set_xticks(x)
# ax.set_xticklabels(labels)
ax.legend(labels=['Simulated', 'Calculated'])


plt.show()
