import random, time, pygame, sys
from pygame.locals import *

FPS=30
windowwidth=640
windowheight=480
boxsize=30
boardwidth=15
boardheight=30
blank="="

movesidewayfreq=0.15
movedownfreq=0.1

Xmargin= int((windowwidth-boardwidth*boxsize)/2)
Topmargin=windowheight-(boardheight*boxsize)-5

WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 155,   0)
LIGHTGREEN  = ( 20, 175,  20)
BLUE        = (  0,   0, 255)
LIGHTBLUE   = ( 20,  20, 175)
YELLOW      = (155, 155,   0)
LIGHTYELLOW = (175, 175,  20)

Bordercolor=BLUE
BGcolor=BLACK
TextColor=WHITE
TextShadowColor=GRAY
COLORS=(BLUE, GREEN, RED, YELLOW)
LIGHTColors=(LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)
assert len(COLORS)==len(LIGHTColors)

TemplateWidth=5
TemplateHeight=5

S_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']]

Z_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]

I_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]

O_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]

J_SHAPE_TEMPLATE = [['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']]

L_SHAPE_TEMPLATE = [['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]

T_SHAPE_TEMPLATE = [['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....']]

PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}

def main():
	global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT
	pygame.init()
	FPSCLOCK=pygame.time.Clock()
	DISPLAYSURF=pygame.display.set_mode((windowwidth,windowheight))
	BASICFONT=pygame.font.Font('freesansbold.ttf',18)
	BIGFONT=pygame.font.Font('freesansbold.ttf',100)
	pygame.display.set_caption("Welcome to Tetris")
		
	showTextScreen('Tetris')
	while True:
		if random.randint(0,1)==0:
			print "hi"
		#pygame.mixer.music.load('tetrisb.mid')
		else:
			print "Potato"
		#pygame.mixer.music.load('tetrisc.mid')
		#pygame.mixer.music.play(-1, 0.0)
		runGame()
		#pygame.mixer.music.stop()
		showTextScreen('Game Over')
def runGame():
	board=getBlankBoard()
	lastMoveDownTime=time.time()
	lastMoveSidewaysTime=time.time()
	lastFallTime=time.time()
	movingDown=False
	movingLeft=False
	movingRight=False
	score=0
	level,fallFreq=calculatedLevelAndFallFreq(score)
	
	fallingPiece=getNewPiece()
	nextPiece=getNewPiece()
	
	while True:
		if fallingPiece==None:
			fallingPiece=nextPiece
			nextPiece=getNewPiece()
			lastFallTime=time.time()
			
			if not isValidPosition(board,fallingPiece):
				return
	checkForQuit()
        for event in pygame.event.get():
            if event.type == KEYUP:
                if (event.key == K_p):
                    DISPLAYSURF.fill(BGCOLOR)
                    pygame.mixer.music.stop()
                    showTextScreen('Paused')
                    #pygame.mixer.music.play(-1, 0.0)
                    lastFallTime = time.time()
                    lastMoveDownTime = time.time()
                    lastMoveSidewaysTime = time.time()
                elif (event.key == K_LEFT or event.key == K_a):
                    movingLeft = False
                elif (event.key == K_RIGHT or event.key == K_d):
                    movingRight = False
                elif (event.key == K_DOWN or event.key == K_s):
                    movingDown = False

            elif event.type == KEYDOWN:
                # moving the piece sideways
                if (event.key == K_LEFT or event.key == K_a) and isValidPosition(board, fallingPiece, adjX=-1):
                    fallingPiece['x'] -= 1
                    movingLeft = True
                    movingRight = False
                    lastMoveSidewaysTime = time.time()

                elif (event.key == K_RIGHT or event.key == K_d) and isValidPosition(board, fallingPiece, adjX=1):
                    fallingPiece['x'] += 1
                    movingRight = True
                    movingLeft = False
                    lastMoveSidewaysTime = time.time()

                # rotating the piece (if there is room to rotate)
                elif (event.key == K_UP or event.key == K_w):
                    fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])
                    if not isValidPosition(board, fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
                elif (event.key == K_q): # rotate the other direction
                    fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
                    if not isValidPosition(board, fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])

                # making the piece fall faster with the down key
                elif (event.key == K_DOWN or event.key == K_s):
                    movingDown = True
                    if isValidPosition(board, fallingPiece, adjY=1):
                        fallingPiece['y'] += 1
                    lastMoveDownTime = time.time()

                # move the current piece all the way down
                elif event.key == K_SPACE:
                    movingDown = False
                    movingLeft = False
                    movingRight = False
                    for i in range(1, BOARDHEIGHT):
                        if not isValidPosition(board, fallingPiece, adjY=i):
                            break
                    fallingPiece['y'] += i - 1
					
		if (movingLeft or movingRight) and time.time()-lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
			if movingLeft and isValidPosition(board,fallingPiece,adjX-1):
				fallingPiece['x']-=1
			elif movingRight and isValidPosition(board,fallingPiece,adjX=1):
				fallingPiece['x']+=1
			lastMoveDownTime=time.time()
			
		if movingDown and time.time() - lastMoveDownTime > MOVEDOWNFREQ and isValidPosition(board, fallingPiece, adjY=1):
			fallingPiece['y'] += 1
            lastMoveDownTime = time.time()
	if time.time()-lastFallTime>fallFreq:
			if not isValidPosition(board,fallingPiece,adjY=1):
				addToBoard(board,fallingPiece)
				score+=removeCompleteLines(board)
				level,fallFreq=calculatedLevelAndFallFreq(score)
				fallingPiece=None
			else:
				fallingPiece['y']+=1
				lastFallTime=time.time()
			
			DISPLAYSURF.fill(BGcolor)
			drawBoard(board)
			drawStatus(score,level)
			drawNextPiece(nextPiece)
			if fallingPiece!=None:
				drawPiece(fallingPiece)
			
			pygame.display.update()
			FPSCLOCK.tick(FPS)
def makeTextObjs(text,font,color):
	surf=font.render(text,True,color)
	return surf, surf.get_rect()

def terminate():
	pygame.quit()
	sys.exit()

def checkForKeyPress():
	checkForQuit()
	for event in pygame.event.get([KEYDOWN,KEYUP]):
		if event.type==KEYDOWN:
			continue
		return event.key
	return None

def showTextScreen(text):

	titleSurf, titleRect = makeTextObjs(text, BIGFONT, TextShadowColor)
	titleRect.center = (int(windowwidth / 2), int(windowheight / 2))
	DISPLAYSURF.blit(titleSurf, titleRect)

	titleSurf, titleRect = makeTextObjs(text, BIGFONT, TextColor)
	titleRect.center = (int(windowwidth / 2) - 3, int(windowheight / 2) - 3)
	DISPLAYSURF.blit(titleSurf, titleRect)

	pressKeySurf, pressKeyRect = makeTextObjs('Press a key to play.', BASICFONT, TextColor)
	pressKeyRect.center = (int(windowwidth / 2), int(windowheight / 2) + 100)
	DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

	while checkForKeyPress() == None:
		pygame.display.update()
		FPSCLOCK.tick()
		
		
def checkForQuit():
	for event in pygame.event.get(QUIT):
		terminate()
	for event in pygame.event.get(KEYUP):
		if event.key==K_ESCAPE:
			terminate()
		pygame.event.post(event)
		
def calculatedLevelAndFallFreq(score):
	level= int(score/10)+1
	fallFreq=0.27-(level*0.02)
	return level, fallFreq

def getNewPiece():
	shape=random.choice(list(PIECES.keys()))
	newPiece = {'shape': shape,
                'rotation': random.randint(0, len(PIECES[shape]) - 1),
                'x': int(boardwidth / 2) - int(TemplateWidth / 2),
                'y': -2, # start it above the board (i.e. less than 0)
                'color': random.randint(0, len(COLORS)-1)}
	return newPiece			
	
def addToBoard(board, piece):
    for x in range(TemplateWidth):
        for y in range(TemplateHeight):
            if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                board[x + piece['x']][y + piece['y']] = piece['color']

				
def getBlankBoard():
	board=[]
	for i in range(boardwidth):
		board.append([blank]*boardheight)
	return board
	
def isOnBoard(x,y):
	return x>=0 and x<boardwidth and y< boardheight

def isValidPosition(board, piece, adjX=0, adjY=0):
		for x in range(TemplateWidth):
			for y in range(TemplateHeight):
				isAboveBoard=y+piece['y']+adjY<0
				if isAboveBoard or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
					continue
			if not isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
				return False
			if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != blank:
				return False
		return True

def isCompleteLine(board,y):
	for x in range(boardwidth):
		if board[x][y]==blank:
			return False
	return True
def removeCompleteLines(board):
    numLinesRemoved = 0
    y = BOARDHEIGHT - 1
    while y >= 0:
        if isCompleteLine(board, y):
            for pullDownY in range(y, 0, -1):
                for x in range(BOARDWIDTH):
                    board[x][pullDownY] = board[x][pullDownY-1]
            for x in range(BOARDWIDTH):
                board[x][0] = BLANK
            numLinesRemoved += 1
        else:
            y -= 1
    return numLinesRemoved	

def convertToPixelCoords(boxx,boxy):
	return(Xmargin+(boxx*boxsize)),(Topmargin+(boxy*boxsize))

def drawBox(boxx,boxy,color,pixelx=None,pixely=None):
	if color == BLANK:
		return
	if pixelx == None and pixely == None:
		pixelx, pixely = convertToPixelCoords(boxx, boxy)
		pygame.draw.rect(DISPLAYSURF, COLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 1, BOXSIZE - 1))
		pygame.draw.rect(DISPLAYSURF, LIGHTCOLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 4, BOXSIZE - 4))

def drawBoard(board):
	pygame.draw.rect(DISPLAYSURF,Bordercolor,(Xmargin-3,Topmargin-7,(boardwidth * Boxsize) + 8, (boardheight * Boxsize) + 8), 5)
	pygame.draw.rect(DISPLAYSURF,Bordercolor,(Xmargin, Topmargin, Boxsize * boardwidth, Boxsize * boardheight))
	for x in range(boardwidth):
		for y in range(boardheight):
			drawBox(x,y,board[x][y])

def drawStatus(score,level):
	scoreSurf=BASICFONT.render('Score: %s' % score, True, TextColor)
	scoreRect = scoreSurf.get_rect()
	scoreRect.topleft = (windowwidth - 150, 20)
	DISPLAYSURF.blit(scoreSurf, scoreRect)
	
	levelSurf = BASICFONT.render('Level: %s' % level, True, TEXTCOLOR)
	levelRect = levelSurf.get_rect()
	levelRect.topleft = (windowwidth - 150, 50)
	DISPLAYSURF.blit(levelSurf, levelRect)
	
def drawPiece(piece,pixelx=None,pixely=None):
	shapeToDraw = PIECES[piece['shape']][piece['rotation']]
	if pixelx == None and pixely == None:
		pixelx,pixely=convertToPixelCoords(piece['x'],piece['y'])
		
	for x in range(TemplateWidth):
		for y in range(TemplateHeight):
			if shapeToDraw[y][x]!=blank:
				drawBox(None,None,piece['color'], pixelx+(x * BOXSIZE), pixely + (y * BOXSIZE))
	
def drawNextPiece(piece):
	nextSurf = BASICFONT.render('Next:', True, TEXTCOLOR)
	nextRect = nextSurf.get_rect()
	nextRect.topleft = (windowwidth - 120, 80)
	DISPLAYSURF.blit(nextSurf, nextRect)
	drawPiece(piece,pixelx=windowwidth-120,pixely=100)
	
if __name__ == '__main__':
    main()