from cmu_graphics import *
import math
import copy
import random



### ### ### ### ### ### ### ### ### ###
### The Game Class

# given a "dimension" value and a "total mine" value, this class creates a Game object, i.e. a randomized cube of specified size containing the specified amount of mines
class Game:
    # intialize cube
    def __init__(self, dimension, amtMines):
        self.dimension = dim = dimension    # grid sidelength
        self.amtMines = amtMines            # total # mines on cube
        self.cornerAdjDict = {0: {'topLeft': {0: [(0, 1), (1, 0), (1, 1)],      # stores info on squares adjacent to particular corner squares
                                              4: [(dim-1, 0), (dim-1, 1)], 
                                              1: [(0, dim-1), (1, dim-1)]},    # face to indices
                                  'topRight': {0: [(0, dim-2), (1, dim-2), (1, dim-1)],
                                               4: [(dim-1, dim-2), (dim-1, dim-1)],
                                               3: [(0, 0), (1, 0)]},
                                  'botLeft': {0: [(dim-2, 0), (dim-2, 1), (dim-1, 1)],
                                              5: [(0, 0), (0, 1)],
                                              1: [(dim-2, dim-1), (dim-1, dim-1)]},
                                   'botRight': {0: [(dim-2, dim-2), (dim-1, dim-2), (dim-2, dim-1)],
                                                5: [(0, dim-2), (0, dim-1)],
                                                3: [(dim-2, 0), (dim-1, 0)]}
                                },
                              1: {'topLeft': {1: [(0, 1), (1, 0), (1, 1)], 
                                              4: [(0, 0), (1, 0)], 
                                              2: [(0, dim-1), (1, dim-1)]},    # face to indices
                                  'topRight': {1: [(0, dim-2), (1, dim-2), (1, dim-1)],
                                               4: [(dim-2, 0), (dim-1, 0)],
                                               0: [(0, 0), (1, 0)]},
                                  'botLeft': {1: [(dim-2, 0), (dim-2, 1), (dim-1, 1)],
                                              5: [(dim-1, 0), (dim-2, 0)],
                                              2: [(dim-2, dim-1), (dim-1, dim-1)]},
                                  'botRight': {1: [(dim-2, dim-2), (dim-1, dim-2), (dim-2, dim-1)],
                                               5: [(0, 0), (1, 0)],
                                               0: [(dim-2, 0), (dim-1, 0)]}
                                },
                              2: {'topLeft': {2: [(0, 1), (1, 0), (1, 1)], 
                                              4: [(0, dim-1), (0, dim-2)], 
                                              3: [(0, dim-1), (1, dim-1)]},    # face to indices
                                  'topRight': {2: [(0, dim-2), (1, dim-2), (1, dim-1)],
                                               4: [(0, 0), (0, 1)],
                                               1: [(0, 0), (1, 0)]},
                                  'botLeft': {2: [(dim-2, 0), (dim-2, 1), (dim-1, 1)],
                                              5: [(dim-1, dim-1), (dim-1, dim-2)],
                                              3: [(dim-2, dim-1), (dim-1, dim-1)]},
                                  'botRight': {2: [(dim-2, dim-2), (dim-1, dim-2), (dim-2, dim-1)],
                                               5: [(dim-1, 0), (dim-1, 1)],
                                               1: [(dim-2, 0), (dim-1, 0)]}
                                },
                              3: {'topLeft': {3: [(0, 1), (1, 0), (1, 1)], 
                                              4: [(dim-1, dim-1), (dim-2, dim-1)], 
                                              0: [(0, dim-1), (1, dim-1)]},    # face to indices
                                  'topRight': {3: [(0, dim-2), (1, dim-2), (1, dim-1)],
                                               4: [(0, dim-1), (1, dim-1)],
                                               2: [(0, 0), (1, 0)]},
                                  'botLeft': {3: [(dim-2, 0), (dim-2, 1), (dim-1, 1)],
                                              5: [(0, dim-1), (1, dim-1)],
                                              0: [(dim-2, dim-1), (dim-1, dim-1)]},
                                  'botRight': {3: [(dim-2, dim-2), (dim-1, dim-2), (dim-2, dim-1)],
                                               5: [(dim-2, dim-1), (dim-1, dim-1)],
                                               2: [(dim-2, 0), (dim-1, 0)]}
                                },
                              4: {'topLeft': {4: [(0, 1), (1, 0), (1, 1)], 
                                              2: [(0, dim-1), (0, dim-2)], 
                                              1: [(0, 0), (0, 1)]},    # face to indices
                                  'topRight': {4: [(0, dim-2), (1, dim-2), (1, dim-1)],
                                               2: [(0, 0), (0, 1)],
                                               3: [(0, dim-1), (0, dim-2)]},
                                  'botLeft': {4: [(dim-2, 0), (dim-2, 1), (dim-1, 1)],
                                              0: [(0, 0), (0, 1)],
                                              1: [(0, dim-1), (0, dim-2)]},
                                  'botRight': {4: [(dim-2, dim-2), (dim-1, dim-2), (dim-2, dim-1)],
                                               0: [(0, dim-2), (0, dim-1)],
                                               3: [(0, 0), (0, 1)]}
                                },
                              5: {'topLeft': {5: [(0, 1), (1, 0), (1, 1)], 
                                              0: [(dim-1, 0), (dim-1, 1)], 
                                              1: [(dim-1, dim-2), (dim-1, dim-1)]},    # face to indices
                                  'topRight': {5: [(0, dim-2), (1, dim-2), (1, dim-1)],
                                               0: [(dim-1, dim-2), (dim-1, dim-1)],
                                               3: [(dim-1, 0), (dim-1, 1)]},
                                  'botLeft': {5: [(dim-2, 0), (dim-2, 1), (dim-1, 1)],
                                              2: [(dim-1, dim-1), (dim-1, dim-2)],
                                              1: [(dim-1, 0), (dim-1, 1)]},
                                  'botRight': {5: [(dim-2, dim-2), (dim-1, dim-2), (dim-2, dim-1)],
                                               2: [(dim-1, 0), (dim-1, 1)],
                                               3: [(dim-1, dim-1), (dim-1, dim-2)]}
                                }
                }
        self.boardDict = self.makeBoardOutline(0)        # key (0-5) maps to 2D list---each represents a cube face grid
        self.displayDict = self.makeBoardOutline(False)
        self.fillBoardMines()
        self.edgeAdjDict = {0: {'top': (4, dim-1, None, False),     # stores info on squares adjacent to particular edge squares
                                'left': (1, None, dim-1, False),
                                'bot': (5, 0, None, False),
                                'right': (3, None, 0, False)
                                },
                            1: {'top': (4, None, 0, False),
                                'left': (2, None, dim-1, False),
                                'bot': (5, None, 0, True),
                                'right': (0, None, 0, False)
                                },
                            2: {'top': (4, 0, None, True),
                                'left': (3, None, dim-1, False),
                                'bot': (5, dim-1, None, True),
                                'right': (1, None, 0, False)
                                },
                            3: {'top': (4, None, dim-1, True),
                                'left': (0, None, dim-1, False),
                                'bot': (5, None, dim-1, False),
                                'right': (2, None, 0, False)
                                },
                            4: {'top': (2, 0, None, True),
                                'left': (1, 0, None, False),
                                'bot': (0, 0, None, False),
                                'right': (3, 0, None, True)
                                },    
                            5: {'top': (0, dim-1, None, False),
                                'left': (1, dim-1, None, True),
                                'bot': (2, dim-1, None, True),
                                'right': (3, dim-1, None, False)
                                }
}
        self.fillNumbers()
    
    # construct blank grid for each cube face
    def makeBoardOutline(self, unit):
        outputDict = dict()
        for i in range(6):
            baseBoard = []
            for _ in range(self.dimension):     # create n rows
                baseRow = []
                for _ in range(self.dimension): # create n cols
                    baseRow += [unit]
                baseBoard.append(baseRow)
            outputDict[i] = baseBoard
        return outputDict

    # [important] randomly place given quantity of mines onto entire cube
    def fillBoardMines(self):
        # obtain list of indices of the "bars" which divide 6 buckets of "stars" (one bucket for each cube face)
        # this random process assigns # of mines per face, giving each face 1 mine minimum
        starsAndBars = sorted(random.sample(range(self.amtMines - 1), 5))

        # use list of indices of bars (starsAndBars) to obtain each bucket size (mines per face)
        minesPerFace = [starsAndBars[0]+1]         # begin with size of 1st bucket
        for i in range(1, len(starsAndBars)):
            minesPerFace.append(starsAndBars[i] - (starsAndBars[i-1]))      # systematically add sizes of subsequent buckets
        minesPerFace.append(self.amtMines-1 - (starsAndBars[-1]))

        # some faces might be assigned more mines than grid space allows ... rearrange so that mine quantity legal for each face
        minesPerFace = self.minesPerFaceRearranger(copy.copy(minesPerFace))

        # create list containing 2-tuple coords for every spot in grid
        squaresUnoccupied = []
        for r in range(self.dimension):
            for c in range(self.dimension):
                squaresUnoccupied.append((r,c))
        for face in range(6):       # loop through all 6 cube faces
            self.placeMines(face, minesPerFace[face], copy.copy(squaresUnoccupied))     # place specified # mines onto corresponding face
    
    # [helper] ensures number of mines assigned to a face doesn't exceed grid size (per face)
    def minesPerFaceRearranger(self, minesPerFace):
        for i in range(len(minesPerFace)):
            if minesPerFace[i] > self.dimension**2:     # checks if, for a given face, the number of assigned mines exceeds grid capacity
                spare = minesPerFace[i] - self.dimension**2
                minesPerFace[i] = self.dimension**2
                while(spare > 0):                       # (relatively evenly) redistributes change to other faces
                    for j in range(len(minesPerFace)):
                        if spare == 0:
                            break
                        if minesPerFace[j] < self.dimension**2:
                            minesPerFace[j] += 1
                            spare -= 1
        return minesPerFace

    # [helper] recursively places the specified number of mines onto the corresponding cube face in a random way
    def placeMines(self, face, minesLeft, squaresUnoccupied):
        if minesLeft == 0:      # base case---when all mines assigned to this face have been placed
            return
        else:
            randCoordIdx = random.randint(0, len(squaresUnoccupied)-1)  # choose random (unoccupied) square in this grid
            randRow, randCol = squaresUnoccupied[randCoordIdx] 
            self.boardDict[face][randRow][randCol] = True               # place a mine onto this square
            squaresUnoccupied.pop(randCoordIdx)                         # ensure this square cannot be chosen again
            self.placeMines(face, minesLeft-1, squaresUnoccupied)

    # [important] fills cube grid squares with numbers based on adjacency to surrounding mines
    def fillNumbers(self):
        for face in range(6):
            for row in range(len(self.boardDict[face])):
                for col in range(len(self.boardDict[face][0])):
                    numAdjacentMines = 0
                    if self.boardDict[face][row][col] == True:
                        continue
                    elif self.isEdge(row) and self.isEdge(col):
                        numAdjacentMines = self.fillNumbersCornerCase(face, row, col)
                    elif self.isEdge(row) or self.isEdge(col):
                        numAdjacentMines = self.fillNumbersEdgeCase(face, row, col)
                    else:
                        for nearbyRow in range(row-1, row+2):
                            for nearbyCol in range(col-1, col+2):
                                if type(self.boardDict[face][nearbyRow][nearbyCol]) == bool:
                                    numAdjacentMines += 1
                    self.boardDict[face][row][col] = numAdjacentMines

    # [helper] checks if square is along edge, given row OR col value
    def isEdge(self, idx):
        return (idx == 0) or (idx == self.dimension-1)
    
    # [helper] identifies number of mines adjacent to a particular corner square
    def fillNumbersCornerCase(self, face, row, col):
        output = 0

        # identify which corner
        if row == col == 0:
            thisCorner = 'topLeft'
        elif row == 0 and col == self.dimension-1:
            thisCorner = 'topRight'
        elif row == self.dimension-1 and col == 0:
            thisCorner = 'botLeft'
        elif row == col == self.dimension-1:
            thisCorner = 'botRight'
        
        # count mines adjacent to that corner, referencing "cornerAdjDict"
        for thisFace in self.cornerAdjDict[face][thisCorner]:
            for nearbyRow, nearbyCol in self.cornerAdjDict[face][thisCorner][thisFace]:
                if type(self.boardDict[thisFace][nearbyRow][nearbyCol]) == bool:
                    output += 1
        return output

    # [helper] identifies number of mines adjacent to a particular edge square
    def fillNumbersEdgeCase(self, face, row, col):
        output = 0

        # identify which edge
        if row == 0:
            thisEdge = 'top'
            rRangeLocal, cRangeLocal = range(0, 2), range(-1, 2)
            fixedPoint = col
        elif col == 0:
            thisEdge = 'left'
            rRangeLocal, cRangeLocal = range(-1, 2), range(0, 2)
            fixedPoint = row
        elif row == self.dimension-1:
            thisEdge = 'bot'
            rRangeLocal, cRangeLocal = range(-1, 1), range(-1, 2)
            fixedPoint = col
        elif col == self.dimension-1:
            thisEdge = 'right'
            rRangeLocal, cRangeLocal = range(-1, 2), range(-1, 1)
            fixedPoint = row
        
        # loop through nearby squares on local grid
        for r in rRangeLocal:
            for c in cRangeLocal:
                if type(self.boardDict[face][row + r][col + c]) == bool:
                    output += 1
        
        # loop through nearby squares on adjacent grid
        thisFace, thisRow, thisCol, flip = self.edgeAdjDict[face][thisEdge]
        if thisRow == None:
            edgeList = [self.boardDict[thisFace][r][thisCol] for r in range(self.dimension)]
        elif thisCol == None:
            edgeList = self.boardDict[thisFace][thisRow]
        if flip == True:
            edgeList = edgeList[::-1]
        for i in range(-1, 2):
            if type(edgeList[fixedPoint + i]) == bool:
                output += 1
        
        return output



### ### ### ### ### ### ### ### ### ###
### Create the 8 corners of a cube, store as vectors:

# [important] generates all 8 corner vectors of a cube
def makeVecList():
    output = []
    rawVecList = getCornerVectors([], [])
    for vector in rawVecList:
        output.append(makeVector(vector + [1]))
    return output

# [helper] generates all 8 corner vectors of a cube w/ backtracking
def getCornerVectors(currVec, output):
    if len(currVec) == 3:
        output.append(copy.copy(currVec))
        if len(output) == 8:
            return output
        return None
    else:
        for v in [-1, 1]:
            currVec.append(v)
            poSol = getCornerVectors(currVec, output)
            if poSol != None:
                return output
            currVec.pop()
        return None

# [helper] takes 1D-list [x,y,z,w], converts to 2D list
def makeVector(rawVector):
    output = []
    for vi in rawVector:
        output.append([vi])
    return output



### ### ### ### ### ### ### ### ### ###
### Functions called by onAppStart

# generates pleasant background color
def setBackground(app):
    app.r, app.g, app.b = random.randint(230, 250), random.randint(230, 250), random.randint(230, 250)

# creates hard-coded mini cube to be used on directions screen as a model
def makeExamplePolygonList(app):
    xAdjust, yAdjust = -370, 0
    app.examplePolygonList = []
    exp1 = [459+xAdjust, 188+yAdjust, 496+xAdjust, 233+yAdjust, 471+xAdjust, 300+yAdjust, 434+xAdjust, 255+yAdjust]
    exp2 = [496+xAdjust, 233+yAdjust, 471+xAdjust, 300+yAdjust, 538+xAdjust, 300+yAdjust, 563+xAdjust, 233+yAdjust]
    exp3 = [459+xAdjust, 188+yAdjust, 525+xAdjust, 188+yAdjust, 563+xAdjust, 233+yAdjust, 496+xAdjust, 233+yAdjust]
    app.examplePolygonList.append(exp1)
    app.examplePolygonList.append(exp2)
    app.examplePolygonList.append(exp3)

# creates hard-coded mini cursor to be used on directions screen as an icon
def makeCursorPolygonList(app):
    xAdjust, yAdjust = 690, 240
    scalingFactor = 5
    app.cursorPolygonList = []
    starterList = [(0, 0), (0, 10), (3, 8.5), (4.5, 11.25), (7, 10), (5.5, 7.25), (8, 6)]
    for x, y in starterList:
        app.cursorPolygonList.append((x*scalingFactor) + xAdjust)
        app.cursorPolygonList.append((y*scalingFactor) + yAdjust)

# every portion of resetCube that doesn't require making a new cube
def resetOtherCubeItems(app):
    app.scalar = app.dim*20
    app.unfinishedGrids = [face for face in range(6)]
    app.amtMinesRemaining = app.amtMines
    updateButtonDict(app)

# updates buttonDict
def updateButtonDict(app):
    yAdj = 20
    # contains UI features intended to be drawn, clicked, or both
    app.buttonDict = {
                    # every non-menu screen
                            'backToMenu': [(50, 50, 150, 50, 'antiqueWhite'), ('Back to Menu', 125, 75, 20, None)],
                    # cube screen
                             'minesLeft': [(50, 150, 150, 100, 'honeydew'), (f'{app.amtMinesRemaining}', 125, 220, 30, None), ('Mines Left', 125, 180, 25, None)],
                              'gameOver1': [(50, 150, 150, 100, 'mistyRose'), ('Game Over', 125, 200, 25, None)],
                              'gameOver2': [(50, 400, 150, 50, 'mistyRose'), ('Game Over', 125, 425, 20, None)],
                                'gameWon1': [(50, 150, 150, 100, 'honeydew'), ('You Win', 125, 200, 25, None)],
                                'gameWon2': [(50, 400, 150, 50, 'honeydew'), ('You Win', 125, 425, 20, None)],
                               'newGame': [(50, 300, 150, 50, 'aliceBlue'), ('New Game', 125, 325, 20, None)],
                           'revealMines': [(50, 400, 150, 50, 'ghostWhite'), ('Reveal Mines', 125, 425, 20, None)],
                    # menu screen
                              'playGame': [(300, 350, 150, 50, 'aliceBlue'), ('PLAY GAME', 375, 375, 20, None)],
                            'directions': [(550, 350, 150, 50, 'antiqueWhite'), ('DIRECTIONS', 625, 375, 20, None)],
                    # customization screen
                         'cubeDimension': [(275, 100, 200, 300, 'ivory'), (f'{app.dim}', 375, 200, 120, None), ('CUBE DIMENSION', 375, 75, 20, None)],
                        'totalMineCount': [(525, 100, 200, 300, 'lavender'), (f'{app.amtMines}', 625, 200, 120, None), ('TOTAL MINE COUNT', 625, 75, 20, None)],
                             'higherDim': [(275, 410, 200, 40, 'lightYellow'), ('HIGHER', 375, 430, 20, None)],
                              'lowerDim': [(275, 450, 200, 40, 'lightYellow'), ('LOWER', 375, 470, 20, None)],
                              'higherMine': [(525, 410, 200, 40, 'plum'), ('HIGHER', 625, 430, 20, None)],
                              'lowerMine': [(525, 450, 200, 40, 'plum'), ('LOWER', 625, 470, 20, None)],
                           'clickMineRec': [(525, 325, 200, 75, 'black'), (None)],       # placeholder for mouse tracking (not indended to be drawn)
                         'playGameCustom': [(788, 430, 150, 50, 'aliceBlue'), ('Play Game', 863, 455, 20, None)],
                    # directions screen
                                'gameplay': [(250, 50, 300, 400, 'mistyRose'), ('GAMEPLAY', 400, 75, 30, None)],
                                'controls': [(600, 50, 350, 400, 'aliceBlue'), ('CONTROLS', 775, 75, 30, None)],
                                    'E': [(625, 100+yAdj, 50, 50, 'lightGrey'), ('Q', 650, 125+yAdj, 20, None)],
                                    'W': [(680, 100+yAdj, 50, 50, 'lightGrey'), ('W', 705, 125+yAdj, 20, None)],
                                    'Q': [(735, 100+yAdj, 50, 50, 'lightGrey'), ('E', 760, 125+yAdj, 20, None)],
                                    'A': [(625, 155+yAdj, 50, 50, 'lightGrey'), ('A', 650, 180+yAdj, 20, None)],
                                    'S': [(680, 155+yAdj, 50, 50, 'lightGrey'), ('S', 705, 180+yAdj, 20, None)],
                                    'D': [(735, 155+yAdj, 50, 50, 'lightGrey'), ('D', 760, 180+yAdj, 20, None)],
                                'space': [(625, 290+yAdj, 160, 50, 'lightGrey'), ('space', 705, 315+yAdj, 20, None)],
                                    '+': [(653, 355+yAdj, 50, 50, 'lightGrey'), ('+', 678, 380+yAdj, 20, None)],
                                    '-': [(708, 355+yAdj, 50, 50, 'lightGrey'), ('-', 733, 380+yAdj, 20, None)],
                                'numbers': [(275, 120, 250, 50, 'lightGrey')] + [(f'{key}', 265+int(key)*30, 145, 30, app.colorDict[key]) for key in app.colorDict if isinstance(key, int)],
                                'bombSymb': [(275, 250, 50, 50, 'lightGrey'), (f'{app.bombSymb}', 300, 275, 20, app.colorDict[app.bombSymb])],
                                'markSymb': [(275, 320, 50, 50, 'lightGrey'), (f'{app.markSymb}', 300, 345, 20, app.colorDict[app.markSymb])]
                           }



### ### ### ### ### ### ### ### ### ###
### Routinely update cube vectors, convert data to format that is convenient to draw

# takes 2D vector, outputs (x,y) point for MVC to draw
def formatToDraw(app, vector):
    x, y = vector[0][0], vector[1][0]
    return int(math.floor(app.cx+(x*app.scalar))), int(math.floor(app.cy+(y*app.scalar)))     # scales cube size, sets center position, and rounds to nearest int

# scales x,y coords using w, turns z coord to 0
def vectorConvertTo2D(vector):
    w = vector[3][0]
    output = []
    for i in range(2):      # loop through x,y coords
        output.append([vector[i][0] / w])       # divide by scaling factor
    output.append([0])
    output.append([1])
    return output

# converts list of 3D vectors (corners for a given face) to list of points to be unpacked into a polygon;
# also outputs zTotal, used to identify which cube faces are spacially closest to user
def getVecList2D(app, vecList):
    # vars
    zTotal = 0
    output = []
    unorderedPolygonTuples = []

    # count total z value across face, convert each vec to 2D
    for currVec3D in vecList:
        zTotal += currVec3D[2][0]
        currVec2D = vectorConvertTo2D(currVec3D)
        unorderedPolygonTuples.append(formatToDraw(app, currVec2D))

    # reformat vectors into a list of points unpackable by drawPolygon
    orderedPolygonTuples = unorderedPolygonTuples[:2] + [unorderedPolygonTuples[-1]] + [unorderedPolygonTuples[-2]]
    for x, y in orderedPolygonTuples:
        output.append(int(x))
        output.append(int(y))
    
    return unorderedPolygonTuples, output, zTotal

# make & update dictionary which contains corner vectors organized by face
def makeFaceDict(app):
    output = dict()
    mainListCopy = copy.copy(app.mainVecList)

    # assign face index to respective corner vecs
    output[0] = mainListCopy[:4]
    output[1] = mainListCopy[2:4] + mainListCopy[-2:]
    output[2] = mainListCopy[-4:]
    output[3] = mainListCopy[:2] + mainListCopy[-4:-2]
    output[4] = [mainListCopy[i] for i in range(8) if i % 2 == 1]
    output[5] = [mainListCopy[i] for i in range(8) if i % 2 == 0]

    # order each list [topLeft, topRight, botLeft, botRight]
    output[0][0], output[0][1], output[0][2], output[0][3] = output[0][3], output[0][1], output[0][2], output[0][0]
    output[1][0], output[1][1], output[1][2], output[1][3] = output[1][3], output[1][1], output[1][2], output[1][0]
    output[2][0], output[2][1], output[2][2], output[2][3] = output[2][1], output[2][3], output[2][0], output[2][2]
    output[3][0], output[3][1], output[3][2], output[3][3] = output[3][1], output[3][3], output[3][0], output[3][2]
    output[4][0], output[4][1], output[4][2], output[4][3] = output[4][3], output[4][2], output[4][1], output[4][0]
    output[5][0], output[5][1], output[5][2], output[5][3] = output[5][1], output[5][0], output[5][3], output[5][2]

    return output

# obtains orderedCornerDict (corners of all six faces) and displayableFaces (2D list of polygon points to be drawn)
def getFaceInfo(app):
    # vars
    faceDict = makeFaceDict(app)
    formattedFaceDict = dict()
    orderedCornerDict = dict()
    zTotalListUnsorted = []
    displayableFaces = []

    # get polygon points and zTotal for each cube face
    for k in faceDict:
        orderedCornerTuples, currFace, zTotal = getVecList2D(app, faceDict[k])
        orderedCornerDict[k] = orderedCornerTuples
        formattedFaceDict[k] = currFace
        zTotalListUnsorted.append(zTotal)

    # identify the faces spacially closest to viewer, discard the others
    zTotalListSorted = sorted(zTotalListUnsorted)
    for i in range(len(zTotalListUnsorted)):
        if zTotalListUnsorted[i] in zTotalListSorted[:3]:
            displayableFaces.append([i] + formattedFaceDict[i])

    return orderedCornerDict, displayableFaces



### ### ### ### ### ### ### ### ### ###
### Functions to help user interact with and switch between screens (gameModes)

# makes new cube every time user restarts game
def resetCube(app):
    app.mainVecList = makeVecList()
    app.game = Game(app.dim, app.amtMines)
    app.boardDict = app.game.boardDict
    app.displayDict = app.game.displayDict
    resetOtherCubeItems(app)

# sets all gamemode bools to false, resets background
def falsifyGameModes(app):
    app.menuMode = app.directionsMode = app.customizeGameMode = app.gameLostMode = app.gameWonMode = app.playGameMode = app.newGame = False
    setBackground(app)

# given a button name, draws corresponding rectangle + label
def drawButton(app, name):
    rectInfo = app.buttonDict[name][0]
    labelInfo = app.buttonDict[name][1:]
    if rectInfo != None:
        drawRect(rectInfo[0], rectInfo[1], rectInfo[2], rectInfo[3], fill=rectInfo[4], borderWidth=1, border='black')
    if labelInfo != None:
        for i in range(len(labelInfo)):
            labelColor = labelInfo[i][4] if labelInfo[i][4] != None else 'black'
            drawLabel(labelInfo[i][0], labelInfo[i][1], labelInfo[i][2], size=labelInfo[i][3], fill=labelColor)

# check if won
def isGameWon(app):
    remainingGrids = copy.copy(app.unfinishedGrids)
    for face in remainingGrids:
        for shownValsRow in app.displayDict[face]:
            for val in shownValsRow:
                if (type(val) == bool) and (not val):
                    return False
        app.unfinishedGrids.pop(app.unfinishedGrids.index(face))
    return True

# runs after any click / key press ... updates vars and cheks for game win / loss
def actionTaken(app):
    # update the button dict
    updateButtonDict(app)

    # act in event of loss / win
    if app.gameLostMode:
        app.displayDict = app.boardDict
    elif ((not app.gameWonMode) and (not app.newGame) and (not app.menuMode) and (not app.customizeGameMode) and (not app.directionsMode)
          and isGameWon(app)):     # ensure that game can only be won on cube screen
        falsifyGameModes(app)
        app.gameWonMode = True

    # new game
    elif app.newGame:
        resetCube(app)
        app.newGame = False

    # update vars during game customization
    elif app.customizeGameMode:
        app.minesRecommendedFlexy = int(math.ceil(((app.dim**2)*6)*(2/15)))
        app.minesMaxFlexy = (app.dim**2)*6 - 1
        if app.amtMines > app.minesMaxFlexy:
            app.amtMines = app.minesMaxFlexy
            updateButtonDict(app)

# checks if given button is pressed
def buttonClicked(app, name, mouseX, mouseY):
    buttonInfo = app.buttonDict[name][0]
    xTopLeft, yTopLeft, buttonWidth, buttonHeight = buttonInfo[0], buttonInfo[1], buttonInfo[2], buttonInfo[3]
    return (xTopLeft <= mouseX <= xTopLeft+buttonWidth) and (yTopLeft <= mouseY <= yTopLeft+buttonHeight)



### ### ### ### ### ### ### ### ### ###
### CMU Graphics functions (and the cube rotation helpers)

# [BUILTIN]
def onAppStart(app):
    # initiate gameModes
    app.menuMode = app.directionsMode = app.customizeGameMode = app.gameLostMode = app.gameWonMode = app.playGameMode = app.newGame = False
    app.menuMode = True     # start app on menu screen

    # general settings
    app.width = 1000
    app.height = 500
    app.cx, app.cy = app.width/2, app.height/2
    setBackground(app)
    app.bombSymb = '[ X ]'
    app.markSymb = '[ ! ]'
    app.colorDict = {app.markSymb: 'red',       # use for number colors 
                     app.bombSymb: 'black',
                                1: 'blue',
                                2: 'green',
                                3: 'red',
                                4: 'indigo',
                                5: 'darkRed',
                                6: 'mediumAquamarine',
                                7: 'darkViolet',
                                8: 'darkSlateGray'}
    app.currMouseX = app.currMouseY = None
    makeExamplePolygonList(app)     # used to draw cube on direction screen
    makeCursorPolygonList(app)      # used to draw mouse icon on direction screen

    # cube attributes
    app.dim = 3
    app.amtMines = 8
    app.dimMinFixed, app.dimMaxFixed, app.minesMinFixed = 3, 10, 6
    app.minesRecommendedFlexy = int(math.ceil(((app.dim**2)*6)*(2/15)))
    app.minesMaxFlexy = (app.dim**2)*6 - 1

    resetOtherCubeItems(app)        # sets the table for making a cube, without actually making a full cube
    updateButtonDict(app)

# [BUILTIN]
def redrawAll(app):
    # background
    drawRect(0, 0, app.width, app.height, fill=rgb(app.r, app.g, app.b))
    
    # menu screen
    if app.menuMode:
        drawPolygon(358, 72, 500, 18, 641, 72, 500, 126, fill=gradient('red', 'orange', 'yellow', start='top'), border='white')
        drawPolygon(500, 126, 641, 72, 641, 258, 500, 311, fill=gradient('red', 'orange', 'yellow', start='right-bottom'), border='white')
        drawPolygon(500, 311, 358, 258, 358, 72, 500, 126, fill=gradient('red', 'orange', 'yellow', start='left-bottom'), border='white')
        drawLabel('Surface Sweeper', app.cx, 175, size=50, font='orbitron', bold=True)
        drawButton(app, 'playGame')
        drawButton(app, 'directions')

    # game customization screen
    elif app.customizeGameMode:
        drawButton(app, 'backToMenu')
        drawButton(app, 'cubeDimension')
        drawButton(app, 'totalMineCount')
        drawButton(app, 'higherDim')
        drawButton(app, 'lowerDim')
        drawButton(app, 'higherMine')
        drawButton(app, 'lowerMine')
        drawRect(788, 430, 150, 50, fill='aliceBlue', border='black', borderWidth=1)
        drawLabel('Play Game', 863, 455, size=20)

        # check if dim at bounds
        if app.dim == app.dimMinFixed:
            drawLabel('(minimum)', 375, 287, size=20)
        elif app.dim == app.dimMaxFixed:
            drawLabel('(maximum)', 375, 287, size=20)

        # check it amtMines at bounds
        if app.amtMines == app.minesMinFixed:
            drawLabel('(minimum)', 625, 287, size=20)
        elif app.amtMines == app.minesMaxFlexy:
            drawButton(app, 'totalMineCount')
            drawLabel('(max for dimension)', 625, 287, size=20)

        # draw recommendedMines button
        if app.amtMines != app.minesRecommendedFlexy:
            textAreaCorners = [(525, 325), (725, 325), (525, 400), (725, 400)]
            currColor = 'black'
            if (app.currMouseX != None) and (app.currMouseY != None) and isInsideFace(app.currMouseX, app.currMouseY, textAreaCorners):
                currColor = 'red'
            drawLabel('Click for', 625, 350, size=20, fill=currColor)
            drawLabel('Suggested Amount', 625, 375, size=20, fill=currColor)

    # directions screen
    elif app.directionsMode:
        # draw major features
        drawButton(app, 'backToMenu')
        drawButton(app, 'gameplay')
        drawButton(app, 'controls')

        # draw gameplay section
        drawButton(app, 'numbers')
        drawLabel('Each square has a number', 400, 190, size=17)
        drawLabel('indicating the amount', 400, 210, size=17)
        drawLabel('of adjacent mines', 400, 230, size=17)
        # show bomb symbol
        drawButton(app, 'bombSymb')
        drawLabel('This is a mine...', 437, 265, size=17)
        drawLabel('If you see it, you lose', 437, 285, size=17)
        # show mark symbol
        drawButton(app, 'markSymb')
        drawLabel('Instead, flag mines to keep', 437, 335, size=17)
        drawLabel('track of hazardous areas', 437, 355, size=17)
        # describe adjacency
        drawLabel('Two squares are adjacent if they', 400, 390, size=17)
        drawLabel('share a vertex or an edge...', 400, 410, size=17)
        drawLabel('they can be on different sides!', 400, 430, size=17)

        # draw controls section
        for key in ['W', 'A', 'S', 'D', 'E', 'Q', 'space', '+', '-']: #, 'space', '+', '-'
            drawButton(app, key)
        # rotation keys
        drawLabel('Press keys to spin cube', 868, 150, size=12)
        drawLabel('c-clockwise | up | clockwise', 868, 170, size=12)
        drawLabel('left | down | right', 868, 190, size=12)
        # spacebar
        drawLabel('Hover over square,', 868, 310, size=15)
        drawLabel('press space bar', 868, 330, size=15)
        drawLabel('to flag mines', 868, 350, size=15)
        # zoom
        drawLabel('Press keys to', 868, 390, size=15)
        drawLabel('zoom in / out', 868, 410, size=15)
        # draw decorative cursor icon
        drawPolygon(*app.cursorPolygonList, fill='lightGrey', border='black', borderWidth=1)
        drawLabel('Click mouse to', 868, 250, size=15)
        drawLabel('reveal square', 868, 270, size=15)

        # draw mini cube
        for currExPolygon in app.examplePolygonList:
            drawPolygon(*currExPolygon, fill='lightGrey', border='black', borderWidth=1)
            drawGridlines(2, currExPolygon)
        drawLabel('(example)', 125, 315, size=15)

    # cube screen
    elif app.playGameMode or app.gameLostMode or app.gameWonMode:
        # draw playGameMode interface
        if app.scalar < 200:
            drawButton(app, 'backToMenu')
            drawButton(app, 'newGame')
            if app.playGameMode:
                drawButton(app, 'minesLeft')
                drawButton(app, 'revealMines')
            elif app.gameLostMode:
                drawButton(app, 'gameOver1')
                drawButton(app, 'gameOver2')
            elif app.gameWonMode:
                drawButton(app, 'gameWon1')
                drawButton(app, 'gameWon2')

        # draw cube
        orderedCornerDict, displayableFaces = getFaceInfo(app)
        for currFace in displayableFaces:       # draw cube
            currFaceNum = currFace[0]
            currPolygon = currFace[1:]
            currCorners = orderedCornerDict[currFaceNum]
            drawPolygon(*currPolygon, fill='lightGray', border='black', borderWidth=1)     # EVENTUALLY, change how the faces are drawn
            drawGridlines(app.dim, currPolygon)
            if not(app.currMouseX == None) and not(app.currMouseY == None) and isInsideFace(app.currMouseX, app.currMouseY, currCorners):
                drawHoverSquare(app, currCorners, currFaceNum)
            if isShowing(app, currCorners):
                drawNumbers(app, currCorners, currFaceNum) 

# [BUILTIN] sets real time mouse position as app attribute
def onMouseMove(app, mouseX, mouseY):
    app.currMouseX, app.currMouseY = mouseX, mouseY

# [BUILTIN] click UI buttons or click cube to reveal square value
def onMousePress(app, mouseX, mouseY):
    # menu screen
    if app.menuMode:
        if buttonClicked(app, 'playGame', mouseX, mouseY):
            falsifyGameModes(app)
            app.customizeGameMode = True
        elif buttonClicked(app, 'directions', mouseX, mouseY):
            falsifyGameModes(app)
            app.directionsMode = True

    # directions screen
    elif app.directionsMode:
        if buttonClicked(app, 'backToMenu', mouseX, mouseY):
            falsifyGameModes(app)
            app.menuMode = True
        
    # customization screen
    elif app.customizeGameMode:
        if buttonClicked(app, 'higherDim', mouseX, mouseY) and (app.dim < app.dimMaxFixed):
            app.dim += 1
        elif buttonClicked(app, 'lowerDim', mouseX, mouseY) and (app.dim > app.dimMinFixed):
            app.dim -= 1
        elif buttonClicked(app, 'higherMine', mouseX, mouseY) and (app.amtMines < app.minesMaxFlexy):
            app.amtMines += 1
        elif buttonClicked(app, 'lowerMine', mouseX, mouseY) and (app.amtMines > app.minesMinFixed):
            app.amtMines -= 1
        elif buttonClicked(app, 'clickMineRec', mouseX, mouseY):
            app.amtMines = app.minesRecommendedFlexy
        elif buttonClicked(app, 'backToMenu', mouseX, mouseY):
            falsifyGameModes(app)
            app.menuMode = True
        elif buttonClicked(app, 'playGameCustom', mouseX, mouseY):
            falsifyGameModes(app)
            app.playGameMode = True
            app.newGame = True

    # cube screen
    elif app.playGameMode or app.gameLostMode or app.gameWonMode:
        # mid-game or postgame
        if app.scalar < 200:
            if buttonClicked(app, 'backToMenu', mouseX, mouseY):
                falsifyGameModes(app)
                app.customizeGameMode = True
            elif buttonClicked(app, 'newGame', mouseX, mouseY):
                falsifyGameModes(app)
                app.playGameMode = True
                app.newGame = True

        # mid-game
        if app.playGameMode:
            # square clicked
            sqfOutput = squareFinder(app, mouseX, mouseY)
            if sqfOutput != None:
                r, c, currFaceNum = sqfOutput
                newVal = app.boardDict[currFaceNum][r][c]
                if app.displayDict[currFaceNum][r][c] != app.markSymb:
                    app.displayDict[currFaceNum][r][c] = newVal
                    if (newVal == 0) and (type(newVal) == int):     # hit a zero
                        zeroExtrapolate(app, r, c, currFaceNum)
                    elif (newVal == True) and (type(newVal) == bool):       # hit a mine
                        falsifyGameModes(app)
                        app.gameLostMode = True
            
            # revealMines clicked
            elif buttonClicked(app, 'revealMines', mouseX, mouseY) and app.scalar < 200:
                falsifyGameModes(app)
                app.gameLostMode = True

    # action taken
    actionTaken(app)

# [BUILTIN] rotate cube w/ arrow keys or WASD ... mark mines with space bar   
def onKeyPress(app, key):
    # only on cube screen
    if app.playGameMode or app.gameLostMode or app.gameWonMode:    
        if (key == 'space') and app.playGameMode:
            sqfOutput = squareFinder(app, app.currMouseX, app.currMouseY)
            if sqfOutput != None:
                r, c, currFaceNum = sqfOutput
                currVal = app.displayDict[currFaceNum][r][c]
                if currVal == app.markSymb:
                    app.displayDict[currFaceNum][r][c] = False
                    app.amtMinesRemaining += 1
                elif (not currVal) and (type(currVal) == bool) and (app.amtMinesRemaining > 0):
                    app.displayDict[currFaceNum][r][c] = app.markSymb
                    app.amtMinesRemaining -= 1

        # cube orientation control
        if (key == 'down') or (key == 's'):
            app.mainVecList = xAxisRotate(app.mainVecList, -1*math.pi/16) # ADJUST ANGLE LATER
        if (key == 'up') or (key == 'w'):
            app.mainVecList = xAxisRotate(app.mainVecList, math.pi/16)
        if (key == 'right') or (key == 'd'):
            app.mainVecList = yAxisRotate(app.mainVecList, -1*math.pi/16)
        if (key == 'left') or (key == 'a'):
            app.mainVecList = yAxisRotate(app.mainVecList, math.pi/16)
        if (key == 'e'):
            app.mainVecList = zAxisRotate(app.mainVecList, math.pi/16)
        if (key == 'q'):
            app.mainVecList = zAxisRotate(app.mainVecList, -1*math.pi/16)
        # zoom
        if (key == '-') and (app.scalar > app.dim*10):
            app.scalar -= 10
        if (key == '='):
            app.scalar += 10

    # action taken
    actionTaken(app)

# rotates cube vectors about chosen axis
def xAxisRotate(vecList, theta):
    output = []
    for vector in vecList:
        newVector = [] + [vector[0]]
        newVector.append([vector[1][0]*math.cos(theta) - vector[2][0]*math.sin(theta)])
        newVector.append([vector[1][0]*math.sin(theta) + vector[2][0]*math.cos(theta)])
        newVector += [vector[3]]
        output.append(newVector)
    return output

def yAxisRotate(vecList, theta):
    output = []
    for vector in vecList:
        newVector = []
        newVector.append([vector[0][0]*math.cos(theta) - vector[2][0]*math.sin(theta)])
        newVector += [vector[1]]
        newVector.append([vector[0][0]*math.sin(theta) + vector[2][0]*math.cos(theta)])
        newVector += [vector[3]]
        output.append(newVector)
    return output

def zAxisRotate(vecList, theta):
    output = []
    for vector in vecList:
        newVector = []
        newVector.append([vector[0][0]*math.cos(theta) - vector[1][0]*math.sin(theta)])
        newVector.append([vector[0][0]*math.sin(theta) + vector[1][0]*math.cos(theta)])
        newVector += [vector[2]] + [vector[3]]
        output.append(newVector)
    return output



### ### ### ### ### ### ### ### ### ###
### Draw different auxhiliary portions of the cube (everything but the main polygon itself)

# draws polygon on individual square over which the mouse hovers
def drawHoverSquare(app, currCorners, currFaceNum):
    xTopLeft, yTopLeft = currCorners[0][0], currCorners[0][1]
    xIntervHoriz, yIntervHoriz, xIntervVert, yIntervVert = getLineIntervals(app, currCorners)

    # loop through all squares in grid
    for r in range(app.dim):
        for c in range(app.dim):
            currShownVal = app.displayDict[currFaceNum][r][c]
            if not(type(currShownVal) == int or currShownVal == app.markSymb or (type(currShownVal) == bool and currShownVal)):     # excludes squares whose values are revealed
                squareCorners = getSquareCorners(r, c, xTopLeft, yTopLeft, xIntervHoriz, yIntervHoriz, xIntervVert, yIntervVert)
                # finds unique square which mouse hovers over
                if isInsideFace(app.currMouseX, app.currMouseY, squareCorners):
                    squareCorners[-2], squareCorners[-1] = squareCorners[-1], squareCorners[-2]
                    polygonSquare = []
                    for x, y in squareCorners:      # converts to drawable polygon list
                        polygonSquare.append(x)
                        polygonSquare.append(y)
                    drawPolygon(*polygonSquare, fill='white', border='black', borderWidth=1)

# positions and draws minesweper numbers onto each square
def drawNumbers(app, currCorners, currFaceNum):
    xTopLeft, yTopLeft = currCorners[0][0], currCorners[0][1]
    xIntervHoriz, yIntervHoriz, xIntervVert, yIntervVert = getLineIntervals(app, currCorners)    

    # loop through all squares in grid
    for r in range(app.dim):
        for c in range(app.dim):
            xDot = xTopLeft + c*xIntervHoriz + r*xIntervVert + 0.5*(xIntervHoriz + xIntervVert)     # set x,y value to center of square
            yDot = yTopLeft + c*yIntervHoriz + r*yIntervVert + 0.5*(yIntervHoriz + yIntervVert)
            squareNumber = app.displayDict[currFaceNum][r][c]

            # check if val is mine or undrawable or zero value
            if (squareNumber) and type(squareNumber) == bool:       # draw mine symbol
                squareNumber = app.bombSymb
            elif (not squareNumber) and type(squareNumber) == bool:     # don't draw unrevealed square 
                continue
            elif (squareNumber == 0) and type(squareNumber) == int:     # change square color instead of revealing 0
                squareCorners = getSquareCorners(r, c, xTopLeft, yTopLeft, xIntervHoriz, yIntervHoriz, xIntervVert, yIntervVert)
                squareCorners[-2], squareCorners[-1] = squareCorners[-1], squareCorners[-2]
                polygonSquare = []
                for x, y in squareCorners:
                    polygonSquare.append(x)
                    polygonSquare.append(y)
                drawPolygon(*polygonSquare, fill='darkGray', border='black', borderWidth=0.5)
                continue

            drawLabel(squareNumber, xDot, yDot, fill=app.colorDict[squareNumber], bold=True)

# when a zero square is revealed, this function recursively reveals all adjacent zero squares and the number perimiter surrounding the zero region 
def zeroExtrapolate(app, row, col, face):
    # check squares adjacent to corner
    if (app.game.isEdge(row)) and (app.game.isEdge(col)):
        # identify which corner
        if (row == col == 0):
            thisCorner = 'topLeft'
        elif (row == 0) and (col == app.game.dimension-1):
            thisCorner = 'topRight'
        elif (row == app.game.dimension-1) and (col == 0):
            thisCorner = 'botLeft'
        elif (row == col == app.game.dimension-1):
            thisCorner = 'botRight'

        for thisFace in app.game.cornerAdjDict[face][thisCorner]:
            for nearbyRow, nearbyCol in app.game.cornerAdjDict[face][thisCorner][thisFace]:
                displayedVal = app.displayDict[thisFace][nearbyRow][nearbyCol]
                if (displayedVal == False) and (type(displayedVal) == bool):
                    currVal = app.boardDict[thisFace][nearbyRow][nearbyCol]
                    if (type(currVal) != bool) or (not currVal == True):
                        app.displayDict[thisFace][nearbyRow][nearbyCol] = currVal
                    if (currVal == 0) and (type(currVal) == int):
                        zeroExtrapolate(app, nearbyRow, nearbyCol, thisFace)        # recurr
    
    # check squares adjacent to edges
    elif (app.game.isEdge(row)) or (app.game.isEdge(col)):

        # identify which edge
        if row == 0:
            thisEdge = 'top'
            rRangeLocal, cRangeLocal = range(0, 2), range(-1, 2)
            fixedPoint = col
        elif col == 0:
            thisEdge = 'left'
            rRangeLocal, cRangeLocal = range(-1, 2), range(0, 2)
            fixedPoint = row
        elif row == app.game.dimension-1:
            thisEdge = 'bot'
            rRangeLocal, cRangeLocal = range(-1, 1), range(-1, 2)
            fixedPoint = col
        elif col == app.game.dimension-1:
            thisEdge = 'right'
            rRangeLocal, cRangeLocal = range(-1, 2), range(-1, 1)
            fixedPoint = row

        # loop through nearby squares on local grid
        for r in rRangeLocal:
            for c in cRangeLocal:
                displayedVal = app.displayDict[face][row + r][col + c]
                if (displayedVal == False) and (type(displayedVal) == bool):
                    currVal = app.boardDict[face][row + r][col + c]
                    if (type(currVal) != bool) or (not currVal == True):
                        app.displayDict[face][row + r][col + c] = currVal
                    if (currVal == 0) and (type(currVal) == int):
                        zeroExtrapolate(app, row + r, col + c, face)        # recurr
        
        # loop through nearby squares on adjacent grid
        thisFace, thisRow, thisCol, flip = app.game.edgeAdjDict[face][thisEdge]

        for i in range(-1, 2):
            if flip == True:
                thisFixedPoint = (app.dim-1) - fixedPoint
            else:
                thisFixedPoint = fixedPoint
            
            # if vertical edge
            if thisRow == None:
                displayedVal = app.displayDict[thisFace][thisFixedPoint + i][thisCol]
                if (displayedVal == False) and (type(displayedVal) == bool):
                    currVal = app.boardDict[thisFace][thisFixedPoint + i][thisCol]
                    if (type(currVal) != bool) or (not currVal == True):
                        app.displayDict[thisFace][thisFixedPoint + i][thisCol] = currVal
                    if (currVal == 0) and (type(currVal) == int):
                        zeroExtrapolate(app, thisFixedPoint + i, thisCol, thisFace)     # recurr
            
            # if horizontal edge
            elif thisCol == None:
                displayedVal = app.displayDict[thisFace][thisRow][thisFixedPoint + i]
                if (displayedVal == False) and (type(displayedVal) == bool):
                    currVal = app.boardDict[thisFace][thisRow][thisFixedPoint + i]
                    if (type(currVal) != bool) or (not currVal == True):
                        app.displayDict[thisFace][thisRow][thisFixedPoint + i] = currVal
                    if (currVal == 0) and (type(currVal) == int):
                        zeroExtrapolate(app, thisRow, thisFixedPoint + i, thisFace)     # recurr

    # check squares adjacent to inner squares
    else:
        for nearbyRow in range(row-1, row+2):
            for nearbyCol in range(col-1, col+2):
                displayedVal = app.displayDict[face][nearbyRow][nearbyCol]
                if (displayedVal == False) and (type(displayedVal) == bool):
                    currVal = app.boardDict[face][nearbyRow][nearbyCol]
                    if (type(currVal) != bool) or (not currVal == True):
                        app.displayDict[face][nearbyRow][nearbyCol] = currVal
                    if (currVal == 0) and (type(currVal) == int):
                        zeroExtrapolate(app, nearbyRow, nearbyCol, face)        # recurr

# draw gridLines
def drawGridlines(dim, currFace):
    # vars for line points
    startPointsHoriz = []
    endPointsHoriz = []
    startPointsVert = []
    endPointsVert = []

    # horizontal line
    xIntervalHoriz = (currFace[2] - currFace[0])/dim
    yIntervalHoriz = (currFace[3] - currFace[1])/dim
    # vertical line
    xIntervalVert = (currFace[6] - currFace[0])/dim
    yIntervalVert = (currFace[7] - currFace[1])/dim

    for m in range(1, dim):
        # horizontal line
        startPointsHoriz.append((currFace[0] + (m)*xIntervalHoriz, currFace[1] + (m)*yIntervalHoriz))
        endPointsHoriz.append((currFace[4] - (dim-m)*xIntervalHoriz, currFace[5] - (dim-m)*yIntervalHoriz))
        # vertical line
        startPointsVert.append((currFace[0] + (m)*xIntervalVert, currFace[1] + (m)*yIntervalVert))
        endPointsVert.append((currFace[2] + (m)*xIntervalVert, currFace[3] + (m)*yIntervalVert))

    for i in range(dim-1):
        xh0, yh0 = startPointsHoriz[i]
        xhf, yhf = endPointsHoriz[i]
        xv0, yv0 = startPointsVert[i]
        xvf, yvf = endPointsVert[i]
        drawLine(xh0, yh0, xhf, yhf, lineWidth=1)
        drawLine(xv0, yv0, xvf, yvf, lineWidth=1)

# get x,y intervals between gridlines, based on dimension of grid
def getLineIntervals(app, currCorners):
    xTopLeft, yTopLeft = currCorners[0][0], currCorners[0][1]
    xTopRight, yTopRight = currCorners[1][0], currCorners[1][1]
    xBotLeft, yBotLeft = currCorners[2][0], currCorners[2][1]

    xIntervHoriz = (xTopRight - xTopLeft)/app.dim
    yIntervHoriz = (yTopRight - yTopLeft)/app.dim
    xIntervVert = (xBotLeft - xTopLeft)/app.dim
    yIntervVert = (yBotLeft - yTopLeft)/app.dim

    return xIntervHoriz, yIntervHoriz, xIntervVert, yIntervVert



### ### ### ### ### ### ### ### ### ###
### Get information essential to drawing and/or interacting with the cube

# T/F function determines whether cube face is visible to user (not perpendicular to screen)
def isShowing(app, cornerList):
    xCornerSet = set()
    yCornerSet = set()
    for i in range(len(cornerList)):
        xCurrCorner, yCurrCorner = cornerList[i]
        xCornerSet.add(xCurrCorner)
        yCornerSet.add(yCurrCorner)
        otherCorners = cornerList[0:i] + cornerList[i+1:]
        for xOtherCorner, yOtherCorner in otherCorners:
            if (abs(xCurrCorner - xOtherCorner) <= 2*app.scalar/50) and (abs(yCurrCorner - yOtherCorner) <= 2*app.scalar/50):
                return False
    if (len(xCornerSet) == 1) or (len(yCornerSet) == 1):
        return False
    return True

# given (x,y) coord, identifies which individual square (if any) contains the coord
def squareFinder(app, mouseX, mouseY):
    orderedCornerDict, displayableFaces = getFaceInfo(app)

    for currFace in displayableFaces:
        currFaceNum = currFace[0]
        currCorners = orderedCornerDict[currFaceNum]

        # checks if mouse click overlaps with visible face
        if isShowing(app, currCorners) and isInsideFace(mouseX, mouseY, currCorners):
            xTopLeft, yTopLeft = currCorners[0][0], currCorners[0][1]
            xIntervHoriz, yIntervHoriz, xIntervVert, yIntervVert = getLineIntervals(app, currCorners)
            for r in range(app.dim):
                for c in range(app.dim):

                    # identifies which (unique) square the mouse clicked
                    squareCorners = getSquareCorners(r, c, xTopLeft, yTopLeft, xIntervHoriz, yIntervHoriz, xIntervVert, yIntervVert)
                    if isInsideFace(mouseX, mouseY, squareCorners):
                        return r, c, currFaceNum

# obtain all four corners of an individual square, given topLeft corner and width/height of that square
def getSquareCorners(r, c, xTopLeft, yTopLeft, xIntervHoriz, yIntervHoriz, xIntervVert, yIntervVert):
    # creates a new tuple list w/ corners of individual square
    squareCorners = []
    for horizSum in range(2):
        for vertSum in range(2):
            xSqCorner = xTopLeft + (c + horizSum)*xIntervHoriz + (r + vertSum)*xIntervVert
            ySqCorner = yTopLeft + (c + horizSum)*yIntervHoriz + (r + vertSum)*yIntervVert
            squareCorners.append((xSqCorner, ySqCorner))
    return squareCorners

# T/F checks if coords of mouse press are inside a given parallelogram
def isInsideFace(x, y, currCorners):
    v1, v2, v3 = currCorners[0], currCorners[1], currCorners[2]

    # edge vectors
    vec1 = (v2[0] - v1[0], v2[1] - v1[1])
    vec2 = (v3[0] - v1[0], v3[1] - v1[1])

    # vector from (x,y) to 0th corner
    vecPoint = (x - v1[0], y - v1[1])

    # [SOURCE / MAJOR INSPIRATION: GeeksForGeeks] "Barycentric coordinates" ... https://www.geeksforgeeks.org/check-whether-a-given-point-lies-inside-a-triangle-or-not/
    uDenom = ((vec1[0] * vec2[1]) - (vec1[1] * vec2[0]))
    vDenom = ((vec2[0] * vec1[1]) - (vec2[1] * vec1[0]))
    if not(uDenom == 0 or vDenom == 0):
        u = ((vecPoint[0] * vec2[1]) - (vecPoint[1] * vec2[0])) / uDenom
        v = ((vecPoint[0] * vec1[1]) - (vecPoint[1] * vec1[0])) / vDenom
        return (0 <= u <= 1) and (0 <= v <= 1)
    
    return False



runApp()