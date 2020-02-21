from Gui import Gui
from ListGenerator import Generator
from Sorter import Sorter

import pygame

pygame.init()

HEIGHT = 600
WIDTH = 600


def main():

    surface = (WIDTH, HEIGHT)
    window = pygame.display.set_mode(surface)
    pygame.display.set_caption("Sudoku Solver")
    gui = Gui(HEIGHT, WIDTH)

    g = Generator(25, 25)
    random_list = g.generate_random_list()
    s = Sorter()

    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        gui.render_list(window, random_list)

        # print("Recursive List", end = "")
        # recursive_selection_sort = s.sort("rs")
        # print(recursive_selection_sort)
        # print()

        # print("Iterative List", end = "")
        # iterative_selection_sort = s.sort("is")
        # print(iterative_selection_sort)
        # print()
        pygame.display.update()
    
if __name__ == "__main__":
    main()
    pygame.quit()