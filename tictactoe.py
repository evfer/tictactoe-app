import pygame, sys

pygame.init()

WIDTH = 1200
HEIGHT = 800
BG_COLOUR = (28,170,156)
HGL_COLOUR = (48,190,176)
LN_COLOUR = (13,155,141)
BTN_COLOUR = (51,51,51)
CIRCL_COLOUR = (222,217,202)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOUR)

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Reset', True, BG_COLOUR, BTN_COLOUR)
textRect = text.get_rect()
textRect.center = (605,763)

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def draw_lines():
    pygame.draw.line(screen, LN_COLOUR, (530,220), (530,620), 10)
    pygame.draw.line(screen, LN_COLOUR, (670,220), (670,620), 10)
    pygame.draw.line(screen, LN_COLOUR, (400,350), (800,350), 10)
    pygame.draw.line(screen, LN_COLOUR, (400,490), (800,490), 10)

def draw_reset():
    pygame.draw.rect(screen, BTN_COLOUR, pygame.Rect(0,725,1200,75))
    pygame.draw.rect(screen, BTN_COLOUR, pygame.Rect(0,0,1200,115))
    screen.blit(text, textRect)

def draw_piece(board, type):
    placments = [[425,320],[565,320],[705,320],[425,460],[565,460],[705,460],[425,600],[565,600],[705,600]]

    xVal = placments[board][0]
    yVal = placments[board][1]
    
    if(type):  
        pygame.draw.line(screen, BTN_COLOUR, (xVal,yVal), (xVal + 75,yVal - 75), 10)
        pygame.draw.line(screen, BTN_COLOUR, (xVal + 75, yVal), (xVal , yVal - 75), 10)
    else:
        pygame.draw.circle(screen, CIRCL_COLOUR, (xVal + 37, yVal - 37), 50)
        pygame.draw.circle(screen, BG_COLOUR, (xVal + 37, yVal - 37), 40)

def clearBoard():
    for i in range(9):
        board[i] = '-'
    pygame.draw.rect(screen, BG_COLOUR, pygame.Rect(0,115,1200,610))
    draw_lines()

def checkWin():
    gameState = checkGameState()
    if gameState == 'X':
      print("X player wins!\n")
    elif gameState == 'O':
      print("O player wins!\n")
    elif gameState == 't':
      print("Tie game!\n")

def playTurn(player, n, gameState):
    if player == 1:
      for i in range(9):
          if n == i:
              board[i] = 'X'
              draw_piece(i, True)
      playTurn(0,0,1)
    elif(gameState == 1):
      print("Computers move!\n")
      bestScore = -1000
      bestMove = -1
      for i in range(9):
        score = 0
        if board[i] == '-':
          board[i] = 'O'
          
          score = minimax(board, 0, False)
          board[i] = '-'
          if(score > bestScore):
            bestScore = score
            bestMove = i
      board[bestMove] = 'O'
      draw_piece(bestMove, False)
      correctInput = 0
    checkWin()

def minimax(board, depth, isMaximizing):
  gameState = checkGameState()
  if gameState == 'X':
    return -100
  elif gameState == 'O':
    return 100
  elif gameState == 't':
    return 0

  if isMaximizing:
    bestScore = -1000
      
    for i in range(9):
      if board[i] == '-':
        board[i] = 'O'
        score = minimax(board, depth + 1, False)
        board[i] = '-'
        if(score > bestScore):
          bestScore = score
    return bestScore
  else:
    bestScore = 1000
      
    for i in range(9):
      if board[i] == '-':
        board[i] = 'X'
        score = minimax(board, depth + 1, True)
        board[i] = '-'
        if(score < bestScore):
          bestScore = score
    return bestScore

def checkGameState():
  if board[0] == board[1] and board[0] == board[2] and board[0] != '-':
    return board[0]
  elif board[3] == board[4] and board[3] == board[5] and board[3] != '-':
    return board[3]
  elif board[6] == board[7] and board[6] == board[8] and board[6] != '-':
    return board[6]
  elif board[0] == board[3] and board[0] == board[6] and board[0] != '-':
    return board[0]
  elif board[1] == board[4] and board[1] == board[7] and board[1] != '-':
    return board[1]
  elif board[2] == board[5] and board[2] == board[8] and board[2] != '-':
    return board[2]
  elif board[0] == board[4] and board[0] == board[8] and board[0] != '-':
    return board[0]
  elif board[2] == board[4] and board[2] == board[6] and board[2] != '-':
    return board[2]
  else:
    for i in range(9):
      if board[i] == '-':
        return 'n'
    return 't'

draw_lines()
draw_reset()

gameState = 1
finish = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            if(mouseY >= 215 and mouseY <= 355):
                if(mouseX >= 395 and mouseX <= 535):
                    print("top-left")
                    playTurn(1, 0, gameState)
                elif(mouseX >= 535 and mouseX <= 675):
                    print("top-mid")
                    playTurn(1, 1, gameState)
                elif(mouseX >= 675 and mouseX <= 805):
                    print("top-right")
                    playTurn(1, 2, gameState)
            if(mouseY >= 355 and mouseY <= 495):
                if(mouseX >= 395 and mouseX <= 535):
                    print("mid-left")
                    playTurn(1, 3, gameState)
                elif(mouseX >= 535 and mouseX <= 675):
                    print("mid-mid")
                    playTurn(1, 4, gameState)
                elif(mouseX >= 675 and mouseX <= 805):
                    print("mid-right")
                    playTurn(1, 5, gameState)
            if(mouseY >= 495 and mouseY <= 625):
                if(mouseX >= 395 and mouseX <= 535):
                    print("bot-left")
                    playTurn(1, 6, gameState)
                elif(mouseX >= 535 and mouseX <= 675):
                    print("bot-mid")
                    playTurn(1, 7, gameState)
                elif(mouseX >= 675 and mouseX <= 805):
                    print("bot-right")
                    playTurn(1, 8, gameState)
            if(mouseY >= 725 and mouseY <= 800):
                print("reset")
                clearBoard()
        pygame.display.update()
 
