import pygame, sys, time

#initialize pygame
pygame.init()

windowSize=(800,800)

screen = pygame.display.set_mode(windowSize)

cambriaProFont = pygame.font.SysFont("arialProFont",48)

helloWorldText = cambriaProFont.render("helloWorld",1,(0,0,0))
helloWorldSize= helloWorldText.get_size()
x_helloWorldText,y_helloWorldText=(0,0)
x_dir_helloWorldText=1
y_dir_helloWorldText=1

mouseText = cambriaProFont.render("MOUSE",1,(0,255,0))
mouseSize= mouseText.get_size()
x_mouseText,y_mouseText=(100,200)
x_dir_mouseText=1
y_dir_mouseText=1

#images
exampleImage1 = pygame.image.load("handCursor.png")
exampleImage1Size=exampleImage1.get_size()
xImage1, yImage1 = 0,0


clock = pygame.time.Clock()

#updates the clock
while 1:
  clock.tick(40)
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      sys.exit()
  mousePosition= pygame.mouse.get_pos()
  xImage1, yImage1 = mousePosition
  #x_mouseText,y_mouseText= mousePosition
  #backgroundcolor
  screen.fill((100,100,200))

  #displays helloWorldText 
  screen.blit(helloWorldText, (x_helloWorldText,y_helloWorldText))
  screen.blit(mouseText,(x_mouseText,y_mouseText))
  screen.blit(exampleImage1,(xImage1,yImage1))

  #makes helloWorldTextMove
  x_helloWorldText+=5 * x_dir_helloWorldText
  y_helloWorldText+=5 * y_dir_helloWorldText

  #makes helloWorldText bounce
  if x_helloWorldText+ helloWorldSize[0] > 800 or x_helloWorldText < 0:
    x_dir_helloWorldText*=-1
  
  if y_helloWorldText+ helloWorldSize[0] > 750 or y_helloWorldText < 0:
    y_dir_helloWorldText*=-1
#displays the game
  pygame.display.update()