from graphics import *

'''
4) Red team cannot get kinged
5) Jumping is not available for red even rows
6) Black can go under red if there is a black and red adjacent to it
8) Only one black piece can be a king
10) Black Kings get locked
'''

class Spot:
    #hasCheck = False
    
    def __init__(self ,x1 ,y1 ,x2 ,y2 ,i ):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.index = i
        self.height = 50
        self.width = 50
        self.hasCheck = True

class King:
    def __init__(self, k_val, realPieces, validSpots):
        self.imageOfCrown = Image(Point(validSpots[realPieces[k_val].currentPosition].x1 +25, validSpots[realPieces[k_val].currentPosition].y2 + 25), "purpleKing.png")
        self.attachedTo = k_val
    


class RedTeam:
    radius = 20
    numberAlive = 12 #starting from zero there will be eleven beginning pieces
    positions = []
    realEnemies = [] # an array of actual moveable enemy pieces
    def __init__(self):
        numberAlive = 12
        numberDead = 0
        
        
    
    def initTeam(self,spot_instance, win):
        #positions = []
        #spot_instance
        #c = Circle(Point(spot_instance.x1 + spot_instance.width/2, 
        #                 spot_instance.y1 - spot_instance.width/2), self.radius)
        #c.setFill("Red")
        #c.draw(win)
        self.positions.append(spot_instance)
        #print(self.positions)
        
        i = 20
        
        row = 5
        
        c2 = Checker(spot_instance.x1, spot_instance.y1, win,i,row, red = True)
        self.realEnemies.append(c2)
        
    
    
class Checker:
    def __init__(self,x, y, win,i,row, red = False):
        if(red == False):
            self.currentPosition = i
            self.radius = 20
            self.width = 25
            self.color = "Black"
            self.circ = Circle(Point(x + self.width, 
                             y - self.width), self.radius)  
            self.circ.setFill("Black")
            self.circ.draw(win)
            self.row = row
            self.isKing = False
            
            self.x_coordinate = x
            self.y_cooridinate = y
            
            #self.crown = Image(self.circ.getCenter(),"purpleKing.png")
        else:
            self.currentPosition = i
            self.radius = 20
            self.width = 25
            self.color = "Red"
            self.circ = Circle(Point(x + self.width, 
                             y - self.width), self.radius)  
            self.circ.setFill("Red")
            self.circ.draw(win)
            self.row = row
            self.isKing = False
            
            self.x_coordinate = x
            self.y_cooridinate = y            
    
    
    
         

class BlackTeam:
    radius = 20
    numberAlive = 12 #starting from zero there will be eleven beginning pieces
    positions = []
    def __init__(self):
        numberAlive = 12
        numberDead = 0
        
        
    
    def initTeam(self,spot_instance, win, realPieces, i):
        #positions = []
        #spot_instance
        #c = Circle(Point(spot_instance.x1 + spot_instance.width/2, 
                         #spot_instance.y1 - spot_instance.width/2), self.radius)
        #c.setFill("Black")
        #c.draw(win)
        if (i in (0,1,2,3)):
            row = 0
        elif(i in (4,5,6,7)):
            row = 1
        elif(i in (8,9,10,11)):
            row = 2
        
        c = Checker(spot_instance.x1, spot_instance.y1, win,i,row)
        self.positions.append(spot_instance)
        realPieces.append(c)
        #print(self.positions)
        
        


def printBoard(win, validSpots, spotsWithChecks, realPieces):
    board = Rectangle(Point(50,300), Point(450,700))
    board.setFill("Khaki")
    board.draw(win)
    
    
    initVals = [50,700,100,650]
    x1 = initVals[0]
    y1 = initVals[1]
    x2 = initVals[2]
    y2 = initVals[3]
    
    rows = 0
    
    for i in range (32):
        if(i % 4 == 0 and i != 0):
            rows = rows + 1
            if(rows%2 == 1):
                x1 = initVals[0] + 50
            elif(rows%2 == 0):
                x1 = initVals[0]
            y1 = initVals[1] - (50*rows)
            x2 = x1 + 50
            y2 = initVals[3] - (50*rows)
            
        sq = Rectangle(Point(x1,y1),Point(x2,y2))
        sq.setFill("Peru")
        sq.draw(win)
        #print(x1, y1, x2, y2)
        validSpots.append(Spot(x1,y1,x2,y2, i))
        x1 = x1 + 100
        x2 = x2 + 100
        
        
    
def initTeams(validSpots, win, spotsWithChecks, realPieces):
    #init the black team
    black_team = BlackTeam()
    
    for i in range(black_team.numberAlive):
        black_team.initTeam(validSpots[i], win, realPieces, i)
        spotsWithChecks.append(validSpots[i].index)
        if(i == 11):
            for i in range(12):
                continue
                #print("Black Position: ",black_team.positions[i].index)

           
    #init the red team
    red_team = RedTeam()
    #for i in range(31, 19, -1):
        #red_team.initTeam(validSpots[i], win)
        #spotsWithChecks.append(validSpots[i].index)
        #if(i == 20):
            #for i in range(12):
                #continue
                #print("Red Position: ",red_team.positions[i].index)
        #print(i)
    
    return black_team, red_team;
    

def pickAValidSpot(validSpots, activeSpots, win):
    j_val = 100
    spotIsValid = False
    
    
    #button = Rectangle(Point(500, 50), Point(600,100))
    
    
    while(spotIsValid == False):
        #get mouse click
        mouseClick = win.getMouse()     # get a mouse click and coordinates
        x = mouseClick.getX()
        y = mouseClick.getY()
        
            
        for j in range(len(validSpots)):
            if(x > validSpots[j].x1 and x < validSpots[j].x2 ):                    #if your mouse click is in a valid spot
                if( y < validSpots[j].y1 and y > validSpots[j].y2):                
                    j_val = j  
                if((j_val in activeSpots) and ((j_val+5 not in activeSpots) or (j_val + 4 not in activeSpots))):
                    if(j_val != 7):
                        initMessageBox(win,"VALID")
                        spotIsValid = True
                        return j_val,x,y
                    elif(j_val == 7 and ( 11 not in activeSpots) ):
                        initMessageBox(win,"VALID")
                        spotIsValid = True
                        return j_val,x,y                        
                        
                
                else:
                    if(j_val in (4,5,6,7)):
                        initMessageBox(win, "INVALID: LOCKED IN")
                        #j_val, x, y = pickAValidSpot(validSpots, activeSpots, win)
                    else:
                        initMessageBox(win,"INVALID ")
                        #j_val, x, y = pickAValidSpot(validSpots, activeSpots, win)
                        
                        

def pickAValidDestination(validSpots, activeSpots, win, j_val):
    validDestination = False
    m_val = 100
    
        
    
    while(validDestination == False):
        mouseClick = win.getMouse()     # get a new mouse click and coordinates
        x_val = mouseClick.getX()
        y_val = mouseClick.getY()          
        for m in range(len(validSpots)):
            if(x_val > validSpots[m].x1 and x_val < validSpots[m].x2 ):                    #if your mouse click is in a valid spot
                if( y_val < validSpots[m].y1 and y_val > validSpots[m].y2): 
                    #for e in range(len(realPieces)):
                    #    if(m == realPieces[e].currentPosition
                    
                    m_val = m
                    
                    diff = m_val - j_val
                    if(diff > 5):
                        initMessageBox(win, "SERIOUS PROBLEM")
                        #pickAValidDestination(validSpots, activeSpots, win)
                        #gameOver = True
                        #return gameOver
                    elif(diff < 3):
                        initMessageBox(win, "THAT PIECE IS NOT A KING")
                    
                    elif(m_val in activeSpots):
                        initMessageBox(win, "THERE IS A PIECE ALREADY THERE")
                    
                        
                    else:
                        validDestination = True
                        initMessageBox(win, "VALID")
                        return m_val, x_val, y_val
                
            if(y_val < 300 or x_val > 450):
                goAhead = False    
    
def getRow(j_val):
    if(j_val in (0,1,2,3)):
        row = 0
    elif(j_val in (4,5,6,7)):
        row = 1
    elif(j_val in (8,9,10,11)):
        row = 2
    elif(j_val in (12,13,14,15)):
        row = 3
    elif(j_val in (16,17,18,19)):
        row = 4    
    elif(j_val in (20,21,22,23)):
        row = 5  
    elif(j_val in (24,25,26,27)):
        row = 6  
    elif(j_val in (28,29,30,31)):
        row = 7
    else:
        row = 10
        
    return row
    

def checkSpot(validSpots, win, enemy = False):
    
    mouseClick = win.getMouse()     # get a mouse click and coordinates
    x = mouseClick.getX()
    y = mouseClick.getY()   
    
    isExit = False
    if(x >= 500 and x <= 600):
        if( y>= 50 and y <= 100):
            isExit = True
    
    #if j_val remains 1000 it means that the spot is invalid
    j_val = 1000
    
    for j in range(len(validSpots)):
        if(x > validSpots[j].x1 and x < validSpots[j].x2 ):                    #if your mouse click is in a valid spot
            if( y < validSpots[j].y1 and y > validSpots[j].y2):                
                j_val = j
                
    if(enemy == True):
        if(j_val == 1000):
            initMessageBox(win, "INVALID")
            return False, x, y , isExit, j_val
        else:
            return True, x, y , isExit, j_val        
        
        
        
        
        
    if(j_val == 1000):
        initMessageBox(win, "INVALID")
        return False, x, y , isExit
    else:
        return True, x, y , isExit
   

def getKingDestination(m_val, validSpots, activeSpots, win):
    
    validMValue = False
    
    initMessageBox(win, "THERE IS A PIECE THERE")
    
     
    
    while(validMValue == False):
        mouseClick = win.getMouse()     # get another mouse click and coordinates
        x_val = mouseClick.getX()
        y_val = mouseClick.getY()              
        for m in range(len(validSpots)):
            if(x_val > validSpots[m].x1 and x_val < validSpots[m].x2 ): 
                if( y_val < validSpots[m].y1 and y_val > validSpots[m].y2): 
                    m_val = m
                    if(m_val not in activeSpots):
                        validMValue = True
                        return m_val
                    else:
                        initMessageBox(win, "THERE IS A PIECE THERE AGAIN")
            
        
        
    
    

def goKing(win, gameOver, j_val, k_val, validSpots, activeSpots, realPieces, kingPins, kingCrowns ):
    initMessageBox(win, "goKing()")
    
    
    
    
    
    mouseClick = win.getMouse()     # get another mouse click and coordinates
    x_val = mouseClick.getX()
    y_val = mouseClick.getY()    
    
    gameOver = False
    
    for e in range(len(kingCrowns)):
        if (kingCrowns[e].attachedTo == k_val):
            e_val = e
            
    
    e_val = 0
    
    
    for m in range(len(validSpots)):
        if(x_val > validSpots[m].x1 and x_val < validSpots[m].x2 ):                    #if your mouse click is in a valid spot
            if( y_val < validSpots[m].y1 and y_val > validSpots[m].y2): 
                #for e in range(len(realPieces)):
                #    if(m == realPieces[e].currentPosition
                    
                m_val = m
                
                if(m_val in activeSpots):
                    m_val = getKingDestination(m_val, validSpots, activeSpots, win)
                    
                
                initMessageBox(win, m_val)
                
                
                diff = m_val - j_val
                
                initMessageBox(win, diff)
                
                
                row = getRow(j_val)
                
                initMessageBox(win, row)
                
                
                #m_val is the destination
                
                
                if(row % 2 == 1):
                    if( diff == -4):
                        #down and right
                        realPieces[k_val].circ.move(-50,50)
                        kingCrowns[e_val].imageOfCrown.move(-50,50)
                    elif( diff == -3 ):
                        #down and left
                        realPieces[k_val].circ.move(50, 50)
                        kingCrowns[e_val].imageOfCrown.move(50,50)
                    elif( diff == 5):
                        #up and right
                        realPieces[k_val].circ.move(50, -50)
                        kingCrowns[e_val].imageOfCrown.move(50,-50)  
                    elif ( diff == 4):
                        #up and left
                        realPieces[k_val].circ.move(-50, -50)
                        kingCrowns[e_val].imageOfCrown.move(-50,-50)                         
                        
                        
                        
                elif(row % 2 == 0):
                    if( diff == -5):
                        #down and right
                        realPieces[k_val].circ.move(-50,50)
                        kingCrowns[e_val].imageOfCrown.move(-50,50)
                    elif( diff == -4):
                        #down and left
                        realPieces[k_val].circ.move(50,50) 
                        kingCrowns[e_val].imageOfCrown.move(50,50)
                        
                    elif ( diff == 4):
                        #up and right
                        realPieces[k_val].circ.move(50, -50)
                        kingCrowns[e_val].imageOfCrown.move(50,-50)
                        
                    elif ( diff == 3):
                        #up and left
                        realPieces[k_val].circ.move(-50, -50)
                        kingCrowns[e_val].imageOfCrown.move(-50,-50)                    
                
                        
                
                realPieces[k_val].currentPosition = m_val
                    
                        
                        
                    
                
        if(y_val < 300 or x_val > 450):
            goAhead = False
    
                
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return gameOver
    
    
    
def go(win, validSpots, spotsWithChecks, realPieces, turns, pieceHistory, gameOver, kingCrowns, realKings, red_team):
    
    rp = []
    bp = []
    
    for i in range(len(red_team.realEnemies)):
        rp.append(red_team.realEnemies[i].currentPosition)
        
    for j in range(len(realPieces)):
        bp.append(realPieces[j].currentPosition)
    
    spotIsValid = False
    
    drawAKing = False
    
    finalRow = 7
    
    
    goAhead = True
    
    isExit = False
    
    while (spotIsValid == False):
        
        rowNumber = 10
        hmr = 0
        while(rowNumber > 7):
            if(hmr > 1):
                initMessageBox(win, "ERROR: CLICKED OUTSIDE BOARD")
            spotIsValid, x, y, isExit, sn = checkSpot(validSpots, win, enemy = True)
            if(isExit == True):
                gameOver = True
                return gameOver
        
            rowNumber = getRow(sn)
            hmr += 1
        
            
        if(rowNumber % 2 == 0):
            if(sn+3 in rp and sn+4 in rp):
                spotIsValid = False
                initMessageBox(win, "ERROR: LOCKED IN")
            if(sn +3 in rp and sn+4 in bp):
                spotIsValid = False
                initMessageBox(win, "ERROR: LOCKED IN")   
            if(sn +4 in rp and sn+3 in bp):
                spotIsValid = False
                initMessageBox(win, "ERROR: LOCKED IN")              
        else:
            if(sn+4 in rp and sn+5 in rp):
                spotIsValid = False
                initMessageBox(win, "ERROR: LOCKED IN") 
            if(sn +4 in rp and sn+5 in bp):
                spotIsValid = False
                initMessageBox(win, "ERROR: LOCKED IN")   
            if(sn +5 in rp and sn+4 in bp):
                spotIsValid = False
                initMessageBox(win, "ERROR: LOCKED IN")
            if(sn in {7,15,23} and sn+4 in rp):
                spotIsValid = False
                initMessageBox(win, "ERROR: LOCKED IN")                
            
            
        
        
    
    
    m_val = 0
    j_val = 0
    
    
    activeSpots = []
    kingPins    = []
    for e in range(len(realPieces)):
        activeSpots.append(realPieces[e].currentPosition)
        if(realPieces[e].isKing == True):
            kingPins.append(e)
    
    
    #for tomorrow Tam
    # if the turn is even then the update will be plus four
    # if the turn is odd then the update will be plus five
    
    theSpotYouPressed = 0
    
    for j in range(len(validSpots)):
        if(x > validSpots[j].x1 and x < validSpots[j].x2 ):                    #if your mouse click is in a valid spot
            if( y < validSpots[j].y1 and y > validSpots[j].y2):                
                j_val = j
                row = getRow(j_val)
            
                
                    
                initMessageBox(win, row)
                
             
    if(row % 2 == 1 ):   
        if(j_val == 7 and (11 in activeSpots) or (j_val == 15 and (19 in activeSpots))  or (j_val == 23 and (27 in activeSpots))):
            initMessageBox(win, "INVALID: LOCKED IN")
            j_val, x, y = pickAValidSpot(validSpots, activeSpots, win)                
                
        elif((j_val in activeSpots) and ((j_val+5 not in activeSpots) or (j_val + 4 not in activeSpots))):
            initMessageBox(win,"VALID")        
        else:
            if(j_val in (4,5,6,7) or j_val in (12,13,14,16) or j_val in (20,21,22,23)):
                initMessageBox(win, "INVALID: LOCKED IN")
                j_val, x, y = pickAValidSpot(validSpots, activeSpots, win)
            else:
                initMessageBox(win,"INVALID ")
                j_val, x, y = pickAValidSpot(validSpots, activeSpots, win)
    elif(row % 2 == 0):
        if(j_val == 8 and (12 in activeSpots)):
            initMessageBox(win, "INVALID")
            j_val, x, y = pickAValidSpot(validSpots, activeSpots, win)
        else:
            initMessageBox(win, "VALID")
            
    
    
    
        
    else:
        if(j_val in activeSpots):
            initMessageBox(win, "VALID")
        else:
            initMessageBox(win,"INVALID ")
            j_val, x, y = pickAValidSpot(validSpots, activeSpots, win)            
        
        
        
    #
    k_val = 1000
    for k in range(len(realPieces)):
        if(j_val == realPieces[k].currentPosition):
            k_val = k
            
    if(k_val == 1000):
        return gameOver
    
    if(realPieces[k_val].isKing == True):
        gameOver = goKing(win, gameOver, j_val, k_val, validSpots, activeSpots, realPieces, kingPins,kingCrowns)
        if(gameOver == True):
            return gameOver
        
    elif(realPieces[k_val].isKing == False):
        mouseClick = win.getMouse()     # get another mouse click and coordinates
        x_val = mouseClick.getX()
        y_val = mouseClick.getY()  
    
        for m in range(len(validSpots)):
            if(x_val > validSpots[m].x1 and x_val < validSpots[m].x2 ):                    #if your mouse click is in a valid spot
                if( y_val < validSpots[m].y1 and y_val > validSpots[m].y2): 
                    #for e in range(len(realPieces)):
                    #    if(m == realPieces[e].currentPosition
                    
                    m_val = m
                    diff = m_val - j_val
                    if(m_val in (28,29,30,31)):
                        initMessageBox(win,"THAT PIECE IS A KING") 
                        realPieces[k_val].isKing = True 
                        #crown = Image(realPieces[k_val].circ.getCenter(), "purpleKing.png")
                        #crown.draw(win)     
                        drawAKing = True
                    
                
                    if(diff > 5):
                        initMessageBox(win, "SERIOUS PROBLEM")
                        m_val, x_val, y_val = pickAValidDestination(validSpots, activeSpots, win, j_val)
                        #gameOver = True
                        #return gameOver
                    elif(diff < 3):
                        initMessageBox(win, "THAT PIECE IS NOT A KING")
                        m_val, x_val, y_val = pickAValidDestination(validSpots, activeSpots, win, j_val) 
                    elif(m_val in activeSpots):
                        initMessageBox(win, "THERE IS A PIECE ALREADY THERE")
                        m_val, x_val, y_val = pickAValidDestination(validSpots, activeSpots, win, j_val)
                    
                
                    
                                
                    
                
            if(y_val < 300 or x_val > 450):
                goAhead = False
    
                
                
        
                
    
        if(realPieces[k].currentPosition < len(validSpots)):
            if(x > validSpots[realPieces[k_val].currentPosition].x1 and x < validSpots[realPieces[k_val].currentPosition].x2 ):                    #if your mouse click is in a valid spot
                if( y < validSpots[realPieces[k_val].currentPosition].y1 and y > validSpots[realPieces[k_val].currentPosition].y2):
                    #
                    #print("YOUR CLICK IS IN A VALID SPOT 8!")
                    if(x_val > x):
                        if(goAhead == True):
                            #move the checker to the right
                            realPieces[k_val].circ.move(50,-50)
                            #update the new position of the checker
                            realPieces[k_val].currentPosition = m_val
                        else:
                            initMessageBox(win,"ERROR DONT GO OFF THE BOARD")
                    else:
                        if(goAhead == True):
                            #move the checker to the left
                            realPieces[k_val].circ.move(-50,-50)
                            #update the new position of the checker
                            realPieces[k_val].currentPosition = m_val
                        else:
                            initMessageBox(win,"ERROR DONT GO OFF THE BOARD") 
                        
    
    if(row == (finalRow-1) or drawAKing == True):
        initMessageBox(win,"THAT PIECE IS A KING") 
        realPieces[k_val].isKing = True
        #realPieces[k_val].crown.draw(win)
        #crown = Image(Point(validSpots[realPieces[k_val].currentPosition].x1 +25, validSpots[realPieces[k_val].currentPosition].y2 + 25), "purpleKing.png")
        crown = King(k_val, realPieces, validSpots)
        if(drawAKing == True):
            crown.imageOfCrown.draw(win)
        kingCrowns.append(crown)
                        
                        
    return gameOver
                    
                        
                    
                    
                    
    
    
    
    #increment the place of the checker
    #if(turns == 0 or turns == 2):
    #    checker_place = checker_place + 4
    #elif(turns == 1):
    #    checker_place = checker_place + 5
        
    #print("UPDATE: ", checker_place)
                                
                                
                            
                            
                
     

def initMessageBox(win, strInput):
    board = Rectangle(Point(0,50), Point(500,200))
    board.setFill("white")
    board.draw(win)    
    message = Text(board.getCenter(), strInput)
    message.draw(win)
    
    
def drawExit(win):
    button = Rectangle(Point(500, 50), Point(600,100))
    button.setFill("lightblue")
    button.draw(win)   
    message = Text(button.getCenter(), "Exit")
    message.draw(win)    


def checkJumpR(win, validSpots, spotsWithChecks, realPieces,turns, pieceHistory, gameOver, kingCrowns, realKings, genesis , red_team, blackSpots,sn, pieceIndex,x,y):
    print("\nHELLO")
    
    print(blackSpots)
    
    print("SPOT NUMBER: ",sn)
    
    di = 1000
    dk = 1000
        
    
    r = getRow(sn)
    
    print("ROW: ", r)
    
    
    if(r % 2 == 1 ):
        j = sn - 3
        k = sn - 4
        
        for i in range(len(realPieces)):
            if(realPieces[i].currentPosition == j):
                di = i   
        
        for i in range(len(realPieces)):
            if(realPieces[i].currentPosition == k):
                dk = i        
        
        if(j in blackSpots or k in blackSpots):
            print("JUMP AVAILABLE")
            access = False
            
            if(sn - 7 not in red_team.realEnemies and sn-7 not in blackSpots or (sn - 9 not in red_team.realEnemies and sn-9 not in blackSpots)):
                access = True
            
            if(access == True):
                print("X: ", x)
                
                mc = win.getMouse()
                x1 = mc.getX() 
                print("x1: ", x1)
                
                
                
                delta = x1 - x
                if(delta > 75):
                    print("Proceeding with Jump")
                    if(j not in blackSpots):
                        return False, x1                    
                    
                    red_team.realEnemies[pieceIndex].circ.move(100,100) 
                    red_team.realEnemies[pieceIndex].currentPosition -= 7
                    red_team.realEnemies[pieceIndex].row -= 2
                    
                    if(realPieces[di].isKing == True):
                        save = 1000
                        for e in range(len(kingCrowns)):
                            print(kingCrowns[e].attachedTo, end = " " )
                            if(kingCrowns[e].attachedTo == di):
                                save = e
                                
                            print("\nj:",j)
                            print("di: ",di)
                            print("save: " ,save)
                            #if(kingCrowns[e].attachedTo == j):
                            #    e_val = e                        
                        
                        kingCrowns[save].imageOfCrown.undraw()
                        print("DEATH TO THE KING")
                        #return True,x1
                        #realPieces[di].imageOfCrown.undraw()
                        
                    realPieces[di].circ.undraw()
                    realPieces = realPieces.pop(di)
                    blackSpots.remove(j)
                    initMessageBox(win, "Black's Turn")
                    return True,x1 
                
                elif(delta < -75):
                    print("LEFT JUMP")
                    
                    if(k not in blackSpots):
                        return False, x1    
                    
                    print("DK: ", dk)
                    
                    red_team.realEnemies[pieceIndex].circ.move(-100,100) 
                    red_team.realEnemies[pieceIndex].currentPosition -= 9
                    red_team.realEnemies[pieceIndex].row -= 2
                
                    realPieces[dk].circ.undraw()
                    realPieces = realPieces.pop(dk)
                    blackSpots.remove(k)
                    initMessageBox(win, "Black's Turn")
                    return True,x1 
                
                else:
                    initMessageBox(win, "Black's Turn")
                    return False,x1
                
                
                
            
        
    
    mc = win.getMouse()
    x1 = mc.getX()
    
    initMessageBox(win, "Black's Turn")
    return False,x1




def getPieceCenter(position, win):
    #board dimensions
    #board = Rectangle(Point(50,300), Point(450,700))
    
    j_val = position
    if(j_val in (0,1,2,3)):
        row = 0
    elif(j_val in (4,5,6,7)):
        row = 1
    elif(j_val in (8,9,10,11)):
        row = 6
    elif(j_val in (12,13,14,15)):
        row = 5
    elif(j_val in (16,17,18,19)):
        row = 4    
    elif(j_val in (20,21,22,23)):
        row = 5  
    elif(j_val in (24,25,26,27)):
        row = 6  
    elif(j_val in (28,29,30,31)):
        row = 7
    else:
        row = 10    
    
    
    
    
    ycent = (row-1) * 50 + 325
    #ycent = 475
    pt = Point(75, ycent)
        
    cir = Circle(pt, 10)
    cir.draw(win)   
    cir.setOutline('red')
    cir.setFill('blue')        
    
    coor = str(position) + " " + str(row) + " " + str(ycent)
    initMessageBox(win, coor)
    win.getMouse()    
    





def drawSim(win, validSpots, spotsWithChecks, realPieces,turns, pieceHistory, gameOver, kingCrowns, realKings, genesis , red_team, x, y, pieceIndex):
    print("Welcome to drawsim")
    pt = Point(100, 300)
    cir = Circle(pt, 10)
    #cir.draw(win)
    cir.setOutline('black')
    cir.setFill('aquamarine')    
    
    poly_points = [Point(470, 210), Point(470, 200), Point(480,205), Point(490, 200), Point(500,205), Point(510, 200), Point(510,210)]
    
    p = Polygon(poly_points)
    p.setFill('aquamarine')
    p.draw(win)
    
    crownPoints = [Point(400, 210), Point(400, 200), Point(405,205), Point(410,200), Point(415,205), Point(420,200), Point(425,205), Point(430, 200), Point(430, 210) ] 
    crown = Polygon(crownPoints)
    crown.setFill('lightgreen')
    crown.draw(win)    
    #mc = win.getMouse()
    #p.move(10, 0)
    #red_team.realEnemies[pieceIndex].currentPosition
    
    
    getPieceCenter(red_team.realEnemies[pieceIndex].currentPosition, win)
    
    
    #c = Circle(Point(50,50), 10)
    #c.setFill('blue')
    #c.draw(win)    
    

def goRed(win, validSpots, spotsWithChecks, realPieces,turns, pieceHistory, gameOver, kingCrowns, realKings, genesis , red_team):
    
    
    
    
        
    
    enemyPieces = [] # validSpots
    enemyCheckers = [] # spotsWithChecks
    
    
    enemyPieces = [20,21,22,23,24,25,26,27,28,29,30,31]
    
    
    
    if(genesis == True):
        #init the red team
        
        hmr = 0
        for i in range(31, 19, -1):
            red_team.initTeam(validSpots[i], win)
            enemyCheckers.append(validSpots[i].index)
            hmr += 1
            
        offset = 11
        for i in range(len(red_team.realEnemies)):
            red_team.realEnemies[i].currentPosition  = 20 + offset
            if( red_team.realEnemies[i].currentPosition in {31,30,29,28}):
                red_team.realEnemies[i].row = 7
            elif( red_team.realEnemies[i].currentPosition in {24,25,26,27}):
                red_team.realEnemies[i].row = 6
            elif( red_team.realEnemies[i].currentPosition in {20,21,22,23}):
                red_team.realEnemies[i].row = 5        
                
                
            offset = offset - 1   
            
        return False
        
    
    
    #realPieces[k_val].circ.move(-50,50)
    
    
    #win.getMouse()
    initMessageBox(win,"Red's Turn") 
    
    #mc = win.getMouse()
    #x = mc.getX()
    #y = mc.getY()
    exit = False
    valid = False
    
    
    blackSpots = []
    for i in range(len(realPieces)):
        blackSpots.append(realPieces[i].currentPosition)
    
    
    
    
            
            
    goodClick = False
    valid = False
    
    #Point(50,300), Point(450,700)
    jump = False
    
    
    
    while(goodClick == False ):
        
        
        
        x = 60
        y = 500
        valid = False
        while( valid == False):
            rp = []
            valid, x , y, exit,sn = checkSpot(validSpots, win, enemy = True)
            pieceIndex = 0
            for i in range(len(red_team.realEnemies)):
                if(sn == red_team.realEnemies[i].currentPosition):
                    pieceIndex = i
                rp.append(red_team.realEnemies[i].currentPosition)
                
        # we have a valid click
        jump, x1 = checkJumpR(win, validSpots, spotsWithChecks, realPieces,turns, pieceHistory, gameOver, kingCrowns, realKings, genesis , red_team, blackSpots, sn, pieceIndex,x,y)
                
        if(jump == True):
            return False        
                
            
                
        #mc = win.getMouse()
        #x1 = mc.getX()
        if(x1 > x):
            if(red_team.realEnemies[pieceIndex].row % 2 == 1):
                red_team.realEnemies[pieceIndex].currentPosition -= 3
                red_team.realEnemies[pieceIndex].row -= 1
                
                if(red_team.realEnemies[pieceIndex].currentPosition not in blackSpots and  red_team.realEnemies[pieceIndex].currentPosition not in rp):
                    # move right
                    red_team.realEnemies[pieceIndex].circ.move(50,50) 
                    goodClick = True
                else:
                    initMessageBox(win, "ERROR CHOOSE AGAIN")
                    red_team.realEnemies[pieceIndex].currentPosition += 3
                    red_team.realEnemies[pieceIndex].row += 1
            else:
                red_team.realEnemies[pieceIndex].currentPosition -= 4
                red_team.realEnemies[pieceIndex].row -= 1    
                
                if(red_team.realEnemies[pieceIndex].currentPosition not in blackSpots and red_team.realEnemies[pieceIndex].currentPosition not in rp):
                    # move right
                    red_team.realEnemies[pieceIndex].circ.move(50,50) 
                    goodClick = True
                else:
                    initMessageBox(win, "ERROR CHOOSE AGAIN")
                    red_team.realEnemies[pieceIndex].currentPosition += 4  
                    red_team.realEnemies[pieceIndex].row += 1
        else:
            if(red_team.realEnemies[pieceIndex].row % 2 == 1):
                red_team.realEnemies[pieceIndex].currentPosition -= 4
                red_team.realEnemies[pieceIndex].row -= 1

                if(red_team.realEnemies[pieceIndex].currentPosition not in blackSpots and red_team.realEnemies[pieceIndex].currentPosition not in rp):
                    # move left
                    red_team.realEnemies[pieceIndex].circ.move(-50,50)  
                    goodClick = True
                else:
                    initMessageBox(win, "ERROR CHOOSE AGAIN")
                    red_team.realEnemies[pieceIndex].currentPosition += 4  
                    red_team.realEnemies[pieceIndex].row += 1            
            else:
                red_team.realEnemies[pieceIndex].currentPosition -= 5
                red_team.realEnemies[pieceIndex].row -= 1 
                
                if(red_team.realEnemies[pieceIndex].currentPosition not in blackSpots and red_team.realEnemies[pieceIndex].currentPosition not in rp):
                    # move left
                    red_team.realEnemies[pieceIndex].circ.move(-50,50)
                    goodClick = True
                else:
                    initMessageBox(win, "ERROR CHOOSE AGAIN")
                    red_team.realEnemies[pieceIndex].currentPosition += 5  
                    red_team.realEnemies[pieceIndex].row += 1             



    #if(genesis == False):
        #drawSim(win, validSpots, spotsWithChecks, realPieces,turns, pieceHistory, gameOver, kingCrowns, realKings, genesis , red_team, x,y, pieceIndex)    
    
    initMessageBox(win, "Black's Turn")
    
    
    
    if(gameOver == True):
        return True
    
     
    
    return False
    
    

def main():
    
    genesis = True
    spotsWithChecks = []
    realPieces = []
    pieceHistory = []
    kingCrowns = []
    realKings = []
    redPieces = []
    turns = 0
    win = GraphWin("Checkers",600, 800)
    strInput = "Welcome to Checkers"
    initMessageBox(win,strInput)
    drawExit(win)
    
    gameOver = False
    
    #this array will hold all of the valid spots a checker can be
    #in a checker board half of all squares are valid spots
    validSpots = [] #has all 32 valid spots    
    
    
    
    #win.close()
    
    
    
    #this function prints the board using the graphic library
    printBoard(win, validSpots, spotsWithChecks, realPieces)
       

    #the initTeams function draws the initial red and black checkers... 
    black_team, red_team = initTeams(validSpots, win, spotsWithChecks, realPieces)
    
    #the go function represents a players turn
    #right now it can tell if a spot has a checker
    iters = 0
    spotsWithChecks = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    
        
    
    red_team = RedTeam()
    #init enemy
    gameOver = goRed(win, validSpots, spotsWithChecks, realPieces,turns, pieceHistory, gameOver, kingCrowns, realKings,genesis, red_team)
    
    genesis = False   
    
    
    while (gameOver == False):
        gameOver = go(win, validSpots, spotsWithChecks, realPieces,turns, pieceHistory, gameOver, kingCrowns, realKings, red_team)
        if(gameOver != True):
            gameOver = goRed(win, validSpots, spotsWithChecks, realPieces,turns, pieceHistory, gameOver, kingCrowns, realKings,genesis, red_team)
        
        turns = turns + 1
        
        
    
    #print("There are", len(realPieces), "real pieces.")
    #print("There are", len(spotsWithChecks), "spots with checkers.")
    #print("There are", len(validSpots), "valid spots.")
    #print(spotsWithChecks)
    
    
    #win.getMouse() # Pause to view result
    win.close()    # Close window when done
    
   

main()
