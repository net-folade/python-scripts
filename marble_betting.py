import random 

#create a bag with 10 marbles
#starting amount of money
# current money amount
#result of last round
#how many rounds
#last marble
# welcome user to game
# loop drawing marbles
    #how much was bet
    #draw marble
    # win or loss
    #calc win or loss/ result and new amount/purse
    #lose game if lose half of money
    #print results
# print final results


bag = ('green','green','green','green','green','black','red','red','white','red')

start_purse = 1000 

purse = start_purse 

result = 0 

rounds = 3

marble = 'none'

print(f'You start the game with {start_purse} gold pieces')

for draw in range (1,rounds+1):
    bet = int(input(f'Current Purse: {purse} \n Last draw: {marble} \nRound {draw} - How much do you want to bet?: '))
    
    marble = random.choice(bag)
    
    if marble == 'green':
        result = bet
    elif marble =='black':
        result = 10 * bet
    elif marble =='white':
        result = -5 * bet
    
    else: 
        result =- bet 
        
    purse += result
    
    if purse < 0.5 * start_purse:
        print(f'Game over! You lost to much gold!!!')
        break
    
    print(f'purse: {purse}, last result: ({marble}): {result}\n')


print('starting/ ending purse: ', start_purse, '/',purse)
print('gain/loss: ', ((purse-start_purse)/start_purse *100),'%')











































