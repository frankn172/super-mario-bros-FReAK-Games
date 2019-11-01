class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = screenSize[0]
        self.h = screenSize[1]
        self.getValues()

    def reset(self):
        self.x = 0
        self.y = 0

    def setPosition(self, newX, newY):
        self.x = newX
        self.y = newY

    def setSize(self, width, height):
        self.w = width
        self.h = height

    def update(self):
        self.getValues()

    def getValues(self):
        mario = level.getMario()

        # If player object isn't created yet, don't modify camera.
        if mario is None:
            return

        # If player X position lies in the right half of the camera's
        # viewport, then update camera to follow player to the right.
        if mario.x > self.x + self.w / 2 - mario.w / 2:
            self.x = level.getMario().x - screenSize[0] / 2 + tileWidth / 2

        # Make sure mario doesn't move off-screen to the left.
        # Camera doesn't follow player left.
        if mario.x < self.x:
            mario.x = self.x
