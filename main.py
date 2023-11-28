import pygame
from controller import Controller #import your controller

def main():
    pygame.init()
    screen = pygame.display.set_mode()#Create an instance on your controller object
    mainloop(screen)#Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
