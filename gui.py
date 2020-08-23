import pygame


WHITE = (255, 255, 255)
screenSize = (450,450)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("Puzzle Solver")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # main program that will loop until user exits
    done = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        # close pygame window and exit loop
        if done:
            pygame.quit()
            break

        # background colour
        screen.fill(WHITE)
        
        # draw here
        
        # update the screen (use pygame.display.update(rect_list) for more efficiency)
        pygame.display.flip()

        # fps limit
        clock.tick(30)

