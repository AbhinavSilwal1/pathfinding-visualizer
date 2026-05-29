import pygame
import sys

WIDTH, HEIGHT = 800, 600
FPS = 60


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pathfinding Visualizer")

    clock = pygame.time.Clock()

    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # white background

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()