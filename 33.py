#Write a Python program to create an empty Pygame window.
import pygame
pygame.init()
screen=pygame.display.set_mode((400,500))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.flip() 


#Write a program to create a Pygame window with an image in it. Use white colour as background RGB (255, 255, 255). You can use any image of your choice.