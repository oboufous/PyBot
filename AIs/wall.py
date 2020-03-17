# Template file to create an AI for the game PyRat
# http://formations.telecom-bretagne.eu/pyrat

###############################
# When the player is performing a move, it actually sends a character to the main program
# The four possibilities are defined here
MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'

###############################
# Please put your imports here


###############################
# Please put your global variables here
previousPlayerLocation = (0,0)
previousMove = MOVE_UP
###############################
# Preprocessing function
# The preprocessing function is called at the start of a game
# It can be used to perform intensive computations that can be
# used later to move the player in the maze.
###############################
# Arguments are:
# mazeMap : dict(pair(int, int), dict(pair(int, int), int))
# mazeWidth : int
# mazeHeight : int
# playerLocation : pair(int, int)
# opponentLocation : pair(int,int)
# piecesOfCheese : list(pair(int, int))
# timeAllowed : float
###############################
# This function is not expected to return anything
def preprocessing(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, piecesOfCheese, timeAllowed):
    pass
    # Example prints that appear in the shell only at the beginning of the game
    # Remove them when you write your own program
    #print("<b>[mazeMap]</b> " + repr(mazeMap))
    #print("<b>[mazeWidth]</b> " + repr(mazeWidth))
    #print("<b>[mazeHeight]</b> " + repr(mazeHeight))
    #print("<b>[playerLocation]</b> " + repr(playerLocation))
    #print("<b>[opponentLocation]</b> " + repr(opponentLocation))
    #print("<b>[piecesOfCheese]</b> " + repr(piecesOfCheese))
    #print("<b>[timeAllowed]</b> " + repr(timeAllowed))

###############################
# Turn function
# The turn function is called each time the game is waiting
# for the player to make a decision (a move).
###############################
# Arguments are:
# mazeMap : dict(pair(int, int), dict(pair(int, int), int))
# mazeWidth : int
# mazeHeight : int
# playerLocation : pair(int, int)
# opponentLocation : pair(int, int)
# playerScore : float
# opponentScore : float
# piecesOfCheese : list(pair(int, int))
# timeAllowed : float
###############################
# This function is expected to return a move
def turn(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, playerScore, opponentScore, piecesOfCheese, timeAllowed):
    global previousMove
    neighbors = mazeMap[playerLocation]

    if previousMove == MOVE_RIGHT:
        cellInFront = (playerLocation[0] + 1, playerLocation[1])
        cellToLeft = (playerLocation[0], playerLocation[1]+1)
        if cellToLeft in neighbors:
            wallToLeft = False
        else:
            wallToLeft = True
    elif previousMove == MOVE_DOWN:
        cellInFront = (playerLocation[0], playerLocation[1] - 1)
        cellToLeft = (playerLocation[0] + 1, playerLocation[1])
        if cellToLeft in neighbors:
            wallToLeft = False
        else:
            wallToLeft = True
    elif previousMove == MOVE_UP:
        cellInFront = (playerLocation[0], playerLocation[1] + 1)
        cellToLeft = (playerLocation[0] -1, playerLocation[1])
        if cellToLeft in neighbors:
            wallToLeft = False
        else:
            wallToLeft = True
    elif previousMove == MOVE_LEFT:
        cellInFront = (playerLocation[0] - 1, playerLocation[1])
        cellToLeft = (playerLocation[0], playerLocation[1]-1)
        if cellToLeft in neighbors:
            wallToLeft = False
        else:
            wallToLeft = True


    if wallToLeft == True:
            if previousMove == MOVE_RIGHT:
                if cellInFront in neighbors:
                    move = MOVE_RIGHT
                else:
                    move = MOVE_DOWN
            elif previousMove == MOVE_DOWN:
                if cellInFront in neighbors:
                    move = MOVE_DOWN
                else:
                    move = MOVE_LEFT
            elif previousMove == MOVE_UP:
                if cellInFront in neighbors:
                    move = MOVE_UP
                else:
                    move = MOVE_RIGHT
            elif previousMove == MOVE_LEFT:
                if cellInFront in neighbors:
                    move = MOVE_LEFT
                else:
                    move = MOVE_UP
    else:
        if previousMove == MOVE_RIGHT:
            move = MOVE_UP
        elif previousMove == MOVE_DOWN:
            move = MOVE_RIGHT
        elif previousMove == MOVE_UP:
            move = MOVE_LEFT
        elif previousMove == MOVE_LEFT:
            move = MOVE_DOWN
    previousMove = move
    return move





