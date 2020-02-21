import pygame 

pygame.font.init()

class Gui:

    BLACK = 0, 0, 0
    GRAY = 128, 128, 128
    WHITE = 255, 255, 255
    BLUE = 0, 0, 255
    RED = 255, 0, 0
    LIGHT_GREEN = 144, 238, 144

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def render_list(self, window, _list):
        print(_list)
        thickness = self.width / len(_list)
        heightOfOneUnit = self.height / len(_list)
        window.fill(Gui.WHITE)
        for x in range(len(_list)):
            # pygame.draw.rect(window, Gui.BLACK, (x*3,23,234,232))
            x_start = x*thickness + 10
            y_start = self.height - (heightOfOneUnit*_list[x])
            x_end = (x+1)*thickness
            y_end = self.height
            pygame.draw.rect(window, Gui.BLACK, (x_start, y_start, x_end, y_end))
        # pygame.draw.rect(window, Gui.BLACK, (0, 10, 19, 349))
        # for x in range(len(_list)):
        #     pygame.draw.rect(window, Gui.BLACK, (x*thickness, self.height, x*thickness + 10, self.height - (10*_list[x])))
        #     pygame.display.update()
        # pygame.draw.rect(window, Gui.GRAY, (0, firstGreyLineY, self.width, Gui.skinnyLine))