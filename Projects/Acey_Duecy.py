
import random





class Card:
    
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    
    def print_card(self):
        print('{}{}'.format(self.value,self.suit))





class Deck:
    
    
    def __init__(self):
        
        suit = ['C','D','H','S']
        value = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        
        self.deck = []
       
        
        
        for i in suit:
            for j in value:
                
                self.deck.append(Card(i,j))
                

                
    def show_deck(self):
        
        for i in self.deck:
            i.print_card()
            
    def deal(self):
        return self.deck.pop(0)
        
    
    def shuffle(self):
        
        if self.deck != 1:

            for i in range(len(self.deck)-1,0,-1):
                rand = random.randint(0,i)
                self.deck[i] ,self.deck[rand] = self.deck[rand] ,self.deck[i]


    def face_card(self):
        
        for i in range(len(self.deck)):
            
            if self.deck[i].value == 'J':
                self.deck[i].value = '11'
           
            elif self.deck[i].value == 'Q':
                self.deck[i].value = '12'
            
            elif self.deck[i].value == 'K':
                self.deck[i].value = '13'
            
            elif self.deck[i].value == 'A':
                self.deck[i].value = '14'
                
     
def game():
    
    deck = Deck()
    deck.shuffle()
    deck.face_card()
    
    
    x = int(input('Enter intial amount: '))
    print('Intial amount for bank: ', x)
    print('Game will stop when money is less than 0')
    y = x
    play = 0
    
    
    for i in range(17):
            
        if (play == 1) or (x <0):
            break
            

        print('Round ' + str(i+1))

        x_deal_1 = int(deck.deal().value) 
        x_deal_2 = int(deck.deal().value)
        x_deal_3 = int(deck.deal().value)


        print('The first two cards are: ',x_deal_1,',', x_deal_2)
        x_2nd_bet = int(input('Enter new bet player 1: '))


        def comparison():
            if (x_deal_1 < x_deal_2) and (x_deal_1 != x_deal_3) and (x_deal_2 != x_deal_3) and (x_deal_1 != 14):
                return 'L'

            elif (x_deal_1 > x_deal_2) and (x_deal_1 != x_deal_3) and (x_deal_2 != x_deal_3) and (x_deal_1 != 14):
                return 'G'

            elif (x_deal_1 == x_deal_2) and (x_deal_1 != 14):
                return 'E'

            elif (x_deal_1 == x_deal_3) and (x_deal_1 != 14):
                return 'LE'

            elif (x_deal_2 == x_deal_3) and (x_deal_1 != 14):
                return 'RE'
            
            elif (x_deal_1 == 14):
                return 'Ace'

        if comparison() == 'L':

            if x_deal_1 < x_deal_3 < x_deal_2:

                print('You won the round!')
                y = y - x_2nd_bet
                x = x + x_2nd_bet

            else:
                print('You lost the round!')
                y = y + x_2nd_bet
                x = x  -  x_2nd_bet

        elif comparison() == 'G': 

            if x_deal_2 < x_deal_3 < x_deal_1:

                print('You won the round!')
                y = y - x_2nd_bet
                x = x + x_2nd_bet

            else:
                print('You lost the round!')
                y = y + x_2nd_bet
                x = x  -  x_2nd_bet


        elif comparison() == 'E':

            answer = str(input('Decide if third card is high or low: ' )) #enter high or low

            if answer == 'high':    
                if (x_deal_1 < x_deal_3) and (x_deal_1 != x_deal_3) and (x_deal_3 != 14):

                    print('You won that round!')
                    y = y - x_2nd_bet
                    x = x + x_2nd_bet

                elif (x_deal_1 > x_deal_3) and (x_deal_1 != x_deal_3) and (x_deal_3 != 14):
                    print('You lost that round!')
                    y = y + x_2nd_bet
                    x = x - x_2nd_bet

                elif (x_deal_3 == 14):
                    print('You lost that round!')
                    y = y + 3*x_2nd_bet
                    x = x - 3*x_2nd_bet


            else:
                if (x_deal_1 > x_deal_3) and (x_deal_1 != x_deal_3) and (x_deal_3 != 14):
                    print('You won that round!')
                    y = y - x_2nd_bet
                    x = x  +  x_2nd_bet

                elif (x_deal_1 < x_deal_3) and (x_deal_1 != x_deal_3) and (x_deal_3 != 14):
                    print('You lost that round!')
                    y = y + x_2nd_bet
                    x = x - x_2nd_bet


                elif (x_deal_3 == 14):
                    print('You lost that round!')
                    y = y + 3*x_2nd_bet
                    x = x - 3*x_2nd_bet

        elif comparison() == 'LE':

            print('You lost that round!')
            y = y + 2*x_2nd_bet
            x = x - 2*x_2nd_bet

        elif comparison() == 'RE':

            print('You lost that round!')
            y = y + 2*x_2nd_bet
            x = x - 2*x_2nd_bet
            
        elif comparison() == 'Ace':
            
            choice = str(input('Decide if Ace will be high or low: '))
            if choice == 'high':
                x_deal_1 = 14
                
                
                if (x_deal_2 < x_deal_3 < x_deal_1) and (x_deal_3 != 14):
                    print('You won that round!')
                    y = y - x_2nd_bet
                    x = x + x_2nd_bet
                    
                    
                elif (x_deal_3 < x_deal_2 < x_deal_1) and (x_deal_3 != 14):
                    print('You lost that round!')
                    y = y + x_2nd_bet
                    x = x - x_2nd_bet
                     
                elif (x_deal_3 == 14) and (x_deal_2 != 14):
                    print('You lost that round!')
                    y = y + 2*x_2nd_bet
                    x = x - 2*x_2nd_bet
                    
                elif (x_deal_3 == x_deal_2):
                    print('You lost that round!')
                    y = y + 4*x_2nd_bet
                    x = x - 4*x_2nd_bet
                
                
            elif choice == 'low':
                x_deal_1 = 1
                
                if (x_deal_1 < x_deal_3 < x_deal_2) and (x_deal_3 != 14):
                    print('You won that round!')
                    y = y - x_2nd_bet
                    x = x + x_2nd_bet
                    
                    
                elif (x_deal_1 < x_deal_2 < x_deal_3) and (x_deal_3 != 14):
                    print('You lost that round!')
                    y = y + x_2nd_bet
                    x = x - x_2nd_bet
                    
                elif (x_deal_3 == 14) and (x_deal_2 != 14):
                    print('You lost that round!')
                    y = y + 2*x_2nd_bet
                    x = x - 2*x_2nd_bet
                    
                elif (x_deal_3 == x_deal_2):
                    print('You lost that round!')
                    y = y + 4*x_2nd_bet
                    x = x - 4*x_2nd_bet
                
                
                

        print('The third card is: ', x_deal_3)
        print('You know have: ', x)
        print('Bank has: ', y)
        print('-----------------------------------------------')
        play = int(input('Enter 0 to continue or 1 to stop: '))
        



game()

