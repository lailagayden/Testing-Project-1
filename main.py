import pygame, sys, time

#initialize pygame
pygame.init()

windowSize=(800,800)

screen = pygame.display.set_mode(windowSize)

arialProFont = pygame.font.SysFont("arialProFont",48)

helloWorldText = arialProFont.render("helloWorld",1,(100,100,40),(255,255))

x,y=(0,0)

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      sys.exit()
  screen.blit(helloWorldText, (100,100))

  pygame.display.update()