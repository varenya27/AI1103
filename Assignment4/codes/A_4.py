import random

#function that calculates the probability using 'n' samples
def get_prob(n):
    s=0
    for i in range(n):
        r1 = random.randint(1,6)    #first throw
        r2 = random.randint(1,6)    #second throw
        if r1%2==0:                 #first number should be even
            if r2%2 != 0:           #second number should be odd
                s+=1
    return s/n
num_samples = 10000
num=10
p=0
#taking mean of 'num' probabilities
for i in range(num):
    p+=get_prob(num_samples)
    # print(p)
prob = p/num

print('Required probability: ', prob)