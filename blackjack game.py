#BLACKJACK GAME BETWEEN PLAYER AND THE DEALER


#to get random values from given list
import random
#to get dealer cards and the player cards
dealer_cards=[]
player_cards=[]
#taking card from another list
my_list=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']*4
#taking dictionary values to get the string values
dict_values={'1':1,'2':2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,
             "Q":10,"K":10,"A":1}

#for dealer cards
while len(dealer_cards) < 2:
    my_card=random.choice(list(dict_values.values()))
    dealer_cards.append(my_card)
    my_list.remove(my_card)
    if len(dealer_cards)==2:
        print("dealer has",['X',dealer_cards[1]])

#for player cards
while len(player_cards) < 2:
    my_card = random.choice(list(dict_values.values()))
    player_cards.append(my_card)
    my_list.remove(my_card)
    if len(player_cards) == 2:
        print("player has", player_cards)

#asking player to hit or stand for further game result
for_player=str(input("do you want to HIT then press y or any other key to stand: "))
if for_player=='y':
    my_card = random.choice(list(dict_values.values()))
    player_cards.append(my_card)
    my_list.remove(my_card)
    print("now player after hitting has",player_cards)
    print("and dealer has", dealer_cards)
    print("the total sum of player's cards are:",sum(player_cards))
    print("the total sum of dealer's cards are:", sum(dealer_cards))
    if sum(player_cards)==sum(dealer_cards):
        print("Ohhh...its a tie,nobody wins!")
    elif sum(player_cards)<21 or sum(dealer_cards)>21:
        print("player won by sum of",sum(player_cards))
    elif sum(player_cards) > 21 or sum(dealer_cards) == 21:
        print("player is busted by sum of", sum(player_cards))



else:
    print("now player after standing has", player_cards)
    print("now dealer after hitting has", dealer_cards)
    print("the total sum of dealer's cards are:", sum(dealer_cards))
    print("the total sum of player's cards are:", sum(player_cards))
    if sum(dealer_cards)>sum(player_cards):
        print("dealer won")
    else:
        print("player won")
