import pygame

def makeobjMsg(msg, fontD,color = (0, 0, 0)):
    return fontD.render(msg, True, color), fontD.render(msg, True, color).get_rect()
    
def message(gameDisplay, msg, color = (0, 0, 0), fontType = 'freesansbold.ttf', fontSize = 15, xpos = 10, ypos = 10):
    fontDefination = pygame.font.Font(fontType, fontSize)
    msgSurface, msgRectangle = makeobjMsg(msg, fontDefination, color)
    msgRectangle = (xpos, ypos)
    gameDisplay.blit(msgSurface, msgRectangle)