from gamefunctions import *


class Background:
    def __init__(self, screen):
        self.color = pygame.Color("white")
        self.tiles = None
        self.stagePosX = 0
        self.stagePosY = 0
        self.tileHeight = 0
        self.tileWidth = 0
        self.screen = screen
        self.surface = screen.copy()

    def setTiles(self, tiles):
        if type(tiles) is str:
            self.tiles = [[loadImage(tiles)]]
        elif type(tiles[0]) is str:
            self.tiles = [[loadImage(i) for i in tiles]]
        else:
            self.tiles = [[loadImage(i) for i in row] for row in tiles]
        self.stagePosX = 0
        self.stagePosY = 0
        self.tileWidth = self.tiles[0][0].get_width()
        self.tileHeight = self.tiles[0][0].get_height()
        self.screen.blit(self.tiles[0][0], [0, 0])

    def scroll(self, x, y):
        self.stagePosX -= x
        self.stagePosY -= y
        col = (self.stagePosX % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth
        xOff = (0 - self.stagePosX % self.tileWidth)
        row = (self.stagePosY % (self.tileHeight * len(self.tiles))) // self.tileHeight
        yOff = (0 - self.stagePosY % self.tileHeight)

        col2 = ((self.stagePosX + self.tileWidth) % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth
        row2 = ((self.stagePosY + self.tileHeight) % (self.tileHeight * len(self.tiles))) // self.tileHeight
        self.screen.blit(self.tiles[row][col], [xOff, yOff])
        self.screen.blit(self.tiles[row][col2], [xOff + self.tileWidth, yOff])
        self.screen.blit(self.tiles[row2][col], [xOff, yOff + self.tileHeight])
        self.screen.blit(self.tiles[row2][col2], [xOff + self.tileWidth, yOff + self.tileHeight])

        self.surface = self.screen.copy()

    def setColor(self, color):
        self.color = parseColor(color)
        self.screen.fill(self.color)
        pygame.display.update()
        self.surface = self.screen.copy()
