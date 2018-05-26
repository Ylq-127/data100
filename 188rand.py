        food = max([manhattanDistance(newPos,foodPos) for foodPos in successorGameState.getFood().asList()])
        moveWeight = -float('inf') if successorGameState.getPacmanPosition() == currentGameState.getPacmanPosition() else 0
        foodsWeight = food
        ghostsWeight = -manhattanDistance(newPos,newGhostStates[0].getPosition()) if manhattanDistance(newPos,newGhostStates[0].getPosition()) > food else 100
        succScoreWeight = successorGameState.getScore()
        pelletWeight = manhattanDistance(newPos,successorGameState.getCapsules()[0]) if successorGameState.getCapsules() else 0
        # visitWeight = -100 if successorGameState.getPacmanPosition() in self.visitedSpots else 100
        if any(newScaredTimes):
            ghostsWeight = -float('inf')
            foodsWeight = float('inf')
        retval = moveWeight+1/foodsWeight+ghostsWeight+succScoreWeight+pelletWeight
        print(moveWeight,foodsWeight,ghostsWeight,succScoreWeight,pelletWeight,retval)
        return retval
