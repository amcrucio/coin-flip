import random 

#generating random number between 0 and 1
def flip_coin():
    result = random.random() 
    if result < 0.5:
        return "H"
    else: 
        return "T"
    
#desired sequence: Heads, Heads, Tails
desired_sequence = ["H", "T", "H", "T", "H", "H", "T", "T"]

#keep flipping the coin until the desired sequence is obtained
outcomes_list = []
while outcomes_list[-8:] != desired_sequence: #the last eight outcomes don't match the desired sequence, the loop continues.
    outcome = flip_coin()
    outcomes_list.append(outcome) #store outcomes 
    
#print all the outcomes
for outcome in outcomes_list:
    print(outcome)
    
#recording the amount of times the computer flipped the coin before it got the desired sequence
flip_count = len(outcomes_list) - 8 
print ("It took", flip_count, 'flips before obtaining the desired sequence "H, T, H, T, H, H, T, T."')
