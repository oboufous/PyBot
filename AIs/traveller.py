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
import queue
import sys
print('###################:' , sys.getrecursionlimit)
sys.setrecursionlimit(1500)
###############################
# Please put your global variables here
cheminPlusCourt=0
ListMoves=[]
listPos=[]
allPath=[]
mieux = 1000
meilleur_chemin = [] 
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

    # Example prints that appear in the shell only at the beginning of the game
    # Remove them when you write your own program
    #print("<b>[mazeMap]</b> " + repr(mazeMap))
    #print("<b>[mazeWidth]</b> " + repr(mazeWidth))
    #print("<b>[mazeHeight]</b> " + repr(mazeHeight))
    #print("<b>[playerLocation]</b> " + repr(playerLocation))
    #print("<b>[opponentLocation]</b> " + repr(opponentLocation))
    #print("<b>[piecesOfCheese]</b> " + repr(piecesOfCheese))
    #print("<b>[timeAllowed]</b> " + repr(timeAllowed))
    #print(mazeMap[(15,14)])
    global allPath 
    global meilleur_chemin
    meta=metaGraphe(mazeWidth, mazeHeight, mazeMap, timeAllowed, playerLocation, opponentLocation, piecesOfCheese)
    exhaustif(coins, playerLocation, [playerLocation], 0,meta)
    for i in range (len(meilleur_chemin)-1) :
        allPath=allPath+meta[meilleur_chemin[i],meilleur_chemin[i+1]][1]
    allPath=PositionToMove(allPath)


def priorityQueue() :
    return []

def replace(queue,element):
    lbl=1000
    indice=-1
    ponderation=element[1]
    if queue ==[]:
        return([element])
    while ponderation < lbl and indice <len(queue) -1 :
        indice = indice + 1
        lbl = queue[indice][1]
        if queue[indice][0]==element and queue!=[]:
            queue[indice]=[element]
            return (queue)
    return(queue[:indice]+[element]+queue[indice:])

def get(queue):
    return(queue[0],queue[1:])

def emptyQueue(queue):
    return(queue==[])

def metaGraphe(mazeWidth, mazeHeight, mazeMap, timeAllowed, playerLocation, opponentLocation, piecesOfCheese):
    distance_chemin={} 
    listCoins=[playerLocation]+piecesOfCheese
    noeudInitial=playerLocation
    for i in listCoins:
        noeudInitial=i
        cheminPlusCourt,dist=breadthFirstSearch (mazeMap,noeudInitial, mazeWidth, mazeHeight)
        distanceMin=1000
        for piece in listCoins:
                if piece !=noeudInitial:
                    intermediaire=listPositions(cheminPlusCourt,piece,noeudInitial)
                    distance_chemin[noeudInitial,piece]=[dist[piece],intermediaire]        
    return(distance_chemin)


def exhaustif(restants, noeud, chemin, poids, graphe):
    global meilleur_chemin
    global mieux
  # si nous avons visité tous les noeuds, alors il reste à vérifier si le chemin
  # emprunté est mieux que ce que nous avions auparavant
    if restants == []:
        if poids < mieux:
            mieux = poids
            meilleur_chemin = chemin
 # sinon il faut tester toutes les possibilités
    else:
        for i in range(len(restants)):
            rest=restants[:i]+restants[i+1:]
            nextNode=restants[i]
            if noeud!=nextNode :
                exhaustif(rest, nextNode, chemin+[nextNode], poids+graphe[noeud,nextNode][0], graphe)



# def breadthFirstSearch (graph,sourceNode) :
#     global distances
#     global chemin
#     # First we initialize the queue
#     # We insert the sourceNode and a shortest path to it
#     ourQueue = priorityQueue()
#     ourQueue = [[sourceNode,0]]
#     # Then we initialize the list of visited nodes
#     distances[sourceNode],chemin[sourceNode]=0,[sourceNode]
#     # We then explore the graph
#     while not emptyQueue(ourQueue) :
#         # We look at the current node
#         [currentNode,distance],ourQueue=get(ourQueue)
#         # We add all neighbors of currentNode not already visited
#         #print('####### currentNode :', currentNode)
#         #print('####### graph[currentNode] :', graph[currentNode])
#         for neighbor in graph[currentNode] :
#             #print('################ neighbor : ', neighbor)
#             #print('################ graph[currentNode] : ', graph[currentNode])
#             #print('################ graph[currentNode][neighbor] : ', graph[currentNode][neighbor])
#             distByCurrent = distance + graph[currentNode][neighbor]
#             if distances[neighbor] > distByCurrent:
#                 distances[neighbor] = distByCurrent
#                 ourQueue=replace(ourQueue,[neighbor,distance+graph[currentNode][neighbor]])
#                 chemin[neighbor]=[currentNode]
#     return(chemin,distances)

def breadthFirstSearch(graph,sourceNode, mazeWidth, mazeHeight):
    distances={}
    chemin={}
    for x in range (mazeHeight):
        for y in range (mazeWidth):
            distances[(x,y)]=1000
            chemin[(x,y)]=[]
    # First we initialize the queue
    # We insert the sourceNode and a shortest path to it
    ourQueue = priorityQueue()
    ourQueue = [[sourceNode,0]]
    # Then we initialize the list of visited nodes
    distances[sourceNode],chemin[sourceNode]=0,[sourceNode]
    # We then explore the graph
    while not emptyQueue(ourQueue) :
        # We look at the current node
        [currentNode,distance],ourQueue=get(ourQueue)
        # We add all neighbors of currentNode not already visited
        for neighbor in graph[currentNode] :
            distByCurrent = distance + graph[currentNode][neighbor]
           
            if distances[neighbor] > distByCurrent:
                distances[neighbor] = distByCurrent
                ourQueue=replace(ourQueue,[neighbor,distance+distance+graph[currentNode][neighbor]])
                chemin[neighbor]=[currentNode]
    return(chemin,distances)

def listPosition(chemin,noeudFinal,noeudInitial):
    if noeudFinal==noeudInitial:
        return []
    else: ##sourceNode
        print('==============> noeudInitial : ', noeudInitial)
        print('==============> noeudFinal : ', noeudFinal)
        print('==============> chemin : ', chemin)
        print('==============> chemin[noeudFinal] : ', chemin[noeudFinal])
        return chemin[noeudFinal]+listPosition(chemin,chemin[noeudFinal][0],noeudInitial)

def listPositions(chemin,noeudFinal,noeudInitial):
    listPos=listPosition(chemin,noeudFinal,noeudInitial)
    listPos.reverse()
    return(listPos+[noeudFinal])

def PositionToMove(Positions):
    directions=['L',0,'R','U',0,'D']
    listMove=[]
    for i in range (len(Positions)-1):
        x=Positions[i+1][1]-Positions[i][1]
        if x!=0:
            listMove.append(directions[(x+1)%6])
        else:            
            y=Positions[i+1][0]-Positions[i][0]
            if y!=0:
                listMove.append(directions[(y+4)%6])
    return listMove


def determineNextMove (mazeWidth, mazeHeight, mazeMap, timeAllowed, playerLocation, opponentLocation, piecesOfCheese) :
    global allPath
    return(allPath.pop(0))

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
    global allPath
    preprocessing(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, piecesOfCheese, timeAllowed)
    move = determineNextMove(mazeWidth, mazeHeight, mazeMap, timeAllowed, playerLocation, opponentLocation, piecesOfCheese)

    return allPath.pop(0)





