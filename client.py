from network import Network
import pygame
import pickle

width = 700
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

pygame.font.init()




def redrawWindow(win,player):
    win.fill(white)
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(str(player), True, green, blue)
    textRect = text.get_rect()
    win.blit(text, textRect)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(30)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()



            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_0:
                    p[1][0] = 0
                    response = [0]
                if event.key == pygame.K_KP_1:
                    p[1][1] = 0
                    response = [1]
                if event.key == pygame.K_KP_2:
                    p[1][2] = 0
                if event.key == pygame.K_KP_3:
                    p[1][3] = 0
                if event.key == pygame.K_KP_4:
                    p[1][4] = 0
                if event.key == pygame.K_KP_5:
                    p[1][5] = 0
                if event.key == pygame.K_KP_6:
                    p[1][6] = 0
                if event.key == pygame.K_KP_7:
                    p[1][7] = 0
                if event.key == pygame.K_KP_8:
                    p[1][8] = 0
                if event.key == pygame.K_KP_9:
                    p[1][9] = 0
                n.send(p)

        redrawWindow(win, p)
if __name__ == '__main__':
    main()