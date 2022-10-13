import pygame
from network import Network
from button import Button

pygame.font.init()

width = 800
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
drafted_cards = []
BLACK = [0, 0, 0]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
WHITE = [255, 255, 255]

# card images
btns = [Button("0", 25, 100, BLUE), Button("1", 125, 100, BLUE), Button("2", 225, 100, BLUE),
        Button("3", 325, 100, BLUE), Button("4", 425, 100, BLUE), Button("5", 525, 100, BLUE),
        Button("6", 625, 100, BLUE), Button("7", 725, 100, BLUE), Button("8", 50, 300, BLUE),
        Button("9", 150, 300, BLUE), Button("10", 250, 300, BLUE), Button("11", 350, 300, BLUE),
        Button("12", 450, 300, BLUE), Button("13", 550, 300, BLUE), Button("14", 650, 300, BLUE)]


def game_end(p, drafted_cards):
    print("End of draft")
    # save deck on computer in same place as this file
    deck_name = p + "_deck.txt"
    file = open(deck_name, "w")
    for item in drafted_cards:
        file.write("%s\n" % item)
    file.close()
    quit()


def redraw_window(window, pack):
    window.fill((128,128,128))
    # show buttons in window
    for i in range(0, 15):
        if pack[i] == 0:
            btns[i].color = BLACK
        else:
            btns[i].color = BLUE

    for btn in btns:
        btn.draw(window)

    # show pack to see IDs - delete later
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(str(pack), True, GREEN, BLUE)
    textRect = text.get_rect()
    win.blit(text, textRect)

    pygame.display.update()


def main():
    run = True
    went = False
    clock = pygame.time.Clock()
    n = Network()
    p = n.get_player_num()
    print("You are player: ", p)

    while run:
        clock.tick(60)
        try:
            game = n.send_and_receive("get")
        except:
            run = False
            print("Couldn't get game")
            break

        for event in pygame.event.get():
            # quit if they click the "X" button
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if game.went[int(p)] == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for btn in btns:
                        if btn.click(pos) and not pack[int(btn.text)] == 0:
                            # send card number to server, so it knows which card to 0-out from the cube
                            n.send_pick(btn.text)
                            # add to list "drafted cards" so we keep track of all the indexes of cards we've drafted
                            drafted_cards.append(pack[int(btn.text)])
                            print(drafted_cards)
                            if len(drafted_cards) == 45:
                                game_end(p, drafted_cards)

        pack = game.cube[game.pack_num[int(p)]]
        redraw_window(win, pack)


if __name__ == '__main__':
    main()

    # this prints the index of the pack onto the buttons.  but screws up the send_pick(btn.text) code
    # for i in range(0, 15):
    #   btns[i].text = str(pack[i])