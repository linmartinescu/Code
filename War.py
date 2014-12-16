import random
from collections import deque

class War(object):

    def __init__(self):
        self.winner = 0              # initialize winner
        self.player1Wins  = 0         # initialize player 1 win battle counter
        self.player2Wins = 0         # initialize player 2 win battle counter
        self.totalWars = 0           # total number of wars
        self.allWars = [0,0,0,0,0,0] # intitialize histogram of wars, only 6 possible, set all counters to 0
        pass
    
    def shuffle_and_deal(self):
        cards = []          # create empty list to hold our deck of cards
        for i in range(1,5):    # loop through 4 possible suits
            for j in range(2,15):   # loop through cards 2 -> Ace (last number not used...)
                cards.append(j)     # add card to the deck
            
        random.shuffle(cards)   # shuffle the deck
        player1 = []            # player1's hand
        player2 = []            # player2's hand
        i = 0;                  # handy counter to figure out who gets the next card
        for card in cards:
            if (i % 2 == 0):    # check if counter is even or odd, and hand card to correct person
                player1.append(card)
            else:
                player2.append(card)
            i += 1              # increment our handy counter
        return (player1,player2)    # return each players hand
    
    def play(self, player1hand, player2hand):
        # use dequeue's here, so we have fast add/remove from both ends of the list of cards
        player1Cards = deque(player1hand)
        player2Cards = deque(player2hand)
        # play the game....continue until a player looses by running out of cards
        while True:
            # play a hand
            winningPlayer = self.__playHand__(player1Cards,player2Cards)
            #increment battle win count for correct player
            if (winningPlayer == 1):
                self.player1Wins += 1
            else:
                self.player2Wins += 1
            # check if game is over
            if (len(player1Cards) == 0 or len(player2Cards) == 0):
                break
        # note, we assume that last player to win a hand also wins the game, since it doesn't make sense otherwise
        return (winningPlayer,self.player1Wins+self.player2Wins,self.totalWars,self.allWars)
    
    def __playHand__(self, player1Hand, player2Hand, warCount=-1):
        localWinner = 0
        player1Card = player1Hand.pop()
        player2Card = player2Hand.pop()
        cardsToWin = [player1Card,player2Card]
        if (warCount == 0):
            self.totalWars += 1             # and increment totalWar count at start of new war chain...
                
        # check if player 1 or 2 wins outright, and if we were in a war, increment the correct sequence counter
        if (player1Card > player2Card):
            localWinner = 1
            if (warCount >= 0):
                self.allWars[warCount] += 1
        elif (player1Card < player2Card):
            localWinner = 2
            if (warCount >= 0):
                self.allWars[warCount] += 1
        else: # its WAR time
            # check to make sure players have enough cards, if they are short, they loose
            if (len(player1Hand) < 4 ):
                localWinner = 2
            elif (len (player2Hand) < 4):
                localWinner = 1
            else:
                for i in range(3):
                    cardsToWin.append(player1Hand.pop())
                for i in range(3):

                    cardsToWin.append(player2Hand.pop())
                # make a recursive call to play another hand, incrementing the warCounter
                localWinner = self.__playHand__(player1Hand,player2Hand,warCount+1)
        # at this point, we have determined who won the hand...    
        # now add cards to winner's hand
        random.shuffle(cardsToWin)              # shuffle the cards to be won
        if (localWinner == 1):
            player1Hand.appendleft(cardsToWin)
        else:
            player2Hand.appendleft(cardsToWin)
        return localWinner                      # return the winner of the hand



if __name__ == '__main__':

    #
    import time
    
    totalGames = 10000
    player1Wins = 0
    player2Wins = 0
    totalBattles = 0
    totalWars = 0
    warTuple = [0,0,0,0,0,0]
    startTime = time.time()
    for i in range(totalGames):
        game = War()
        (player1Hand,player2Hand) = game.shuffle_and_deal()
        (winner,battles,wars,warList) = game.play(player1Hand,player2Hand)
        if (winner == 1):
            player1Wins += 1
        else:
            player2Wins += 1
        totalBattles += battles
        totalWars += wars
        for i in range(6):
            warTuple[i] += warList[i]
    
    stopTime = time.time()
    print "Player 1 Wins = ", player1Wins
    print "Player 2 Wins = ", player2Wins
    print "Average battles/game = ", float(totalBattles)/float(totalGames)
    print "Average wars/game = ", float(totalWars)/float(totalGames)
    for i in range(6):
        print "Average ",i+1,"-war sequences/game = ", float(warTuple[i])/float(totalGames)
    print "The elapsed time to complete %d simulations was %.6f seconds" % (totalGames, stopTime-startTime)