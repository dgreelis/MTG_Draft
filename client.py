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


def redrawWindow(win, player):
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
    drafted_cards = []

    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                # set that card number to 0
                if event.key == pygame.K_KP_0:
                    print(p)
                    print(p[3][0])
                    drafted_cards.append(p[3][0])
                    p[3][0] = 0
                if event.key == pygame.K_KP_1:
                    drafted_cards.append(p[3][1])
                    p[3][1] = 0
                if event.key == pygame.K_KP_2:
                    drafted_cards.append(p[3][2])
                    p[3][2] = 0
                if event.key == pygame.K_KP_3:
                    drafted_cards.append(p[3][3])
                    p[3][3] = 0
                if event.key == pygame.K_KP_4:
                    drafted_cards.append(p[3][4])
                    p[3][4] = 0
                if event.key == pygame.K_KP_5:
                    drafted_cards.append(p[3][5])
                    p[3][5] = 0
                if event.key == pygame.K_KP_6:
                    drafted_cards.append(p[3][6])
                    p[3][6] = 0
                if event.key == pygame.K_KP_7:
                    drafted_cards.append(p[3][7])
                    p[3][7] = 0
                if event.key == pygame.K_KP_8:
                    drafted_cards.append(p[3][8])
                    p[3][8] = 0
                if event.key == pygame.K_KP_9:
                    drafted_cards.append(p[3][9])
                    p[3][9] = 0
                # played = 1
                p[2] = 1
                print(drafted_cards)
                print(p)
                n.send(p)
        redrawWindow(win, p)


if __name__ == '__main__':
    main()
