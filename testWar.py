if __name__ == '__main__':

    from game.War import War
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
    
        