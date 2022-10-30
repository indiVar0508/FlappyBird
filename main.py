import pygame
from game_config import Configurations
from utils import message
pygame.init()

def init(gameDisplay):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_s:
                    from game import init_game
                    init_game()
                if event.key == pygame.K_a:
                    from game_for_ai import init_game
                    init_game()
        gameDisplay.fill((51, 51, 51))
        message(gameDisplay, msg = 'Press A to AI play',color = (255, 255, 255), fontSize = 30, xpos = Configurations.gameWidth // 2 - 120, ypos = Configurations.gameHeight // 2 - 35)
        message(gameDisplay, msg = 'Press S to play',color = (255, 255, 255), fontSize = 30, xpos = Configurations.gameWidth // 2 - 120, ypos = Configurations.gameHeight // 2)
        message(gameDisplay, msg = 'Press Q to Quit.!',color = (255, 255, 255), fontSize = 30, xpos = Configurations.gameWidth // 2 - 120, ypos = Configurations.gameHeight // 2 + 35)
        
        pygame.display.update()

if __name__ == "__main__":
    init(pygame.display.set_mode((Configurations.gameWidth, Configurations.gameHeight)))