import random

i=0
ace=0   #number of aces
other=0 #number of non-aces
n= 10000    #number of times the experiment is conducted
while i<n:
    card = random.randint(1,52) #drawing a card out of a deck
    if card<=4: #let 1-4 denote aces
        ace = ace+1
    else:   #let 5-52 denote otherwise
        other=other+1 
    i=i+1
prob_ace = ace/n    #probability of getting an ace
prob_other = other/n    #probability of not getting an ace
print('probability that the card is an ace: ',prob_ace)
print('probability that the card is not an ace: ',prob_other) 