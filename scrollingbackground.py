# import function from pygame_functions.py, * indicates load all the functions
from pygame_functions import *


#screenSize(600,600) sets up screen, background = Background() is used here, we can put that specfic part elsewhere
#setAutoUpdate(False), sets up auto refresh, a boolean for when we should update the screen, no needed

# A list of images to use as background
setBackgroundImage( [  ["images/dungeonFloor1.png", "images/dungeonFloor2.png"] ,
                       ["images/dungeonFloor3.png", "images/dungeonFloor4.png"]  ])

"""
def setBackgroundImage(img):
  
    # This line is used to specify that the variable were using is the global version
    # Any change made to any global variable applies through out the whole file
    global background
  
    # Calls a Background function called setTiles
    background.setTiles(img)
  
    # Screen Refresh is a boolean, if True, update screen
    if screenRefresh:

        updateDisplay()
"""

# not needed, sets up animation frames for player
#testSprite  = makeSprite("images/links.gif",32)  # links.gif contains 32 separate frames of animation. Sizes are automatically calculated.

# not needed, for moving the player
#moveSprite(testSprite,300,300,True)

# not needed, shows players
#showSprite(testSprite)

# these 2 lines are for animation, not needed to scroll backgrond
#nextFrame = clock()
#frame=0
while True:
    # Set fps, for animation, not needed for scrolling background
    #if clock() > nextFrame:                         # We only animate our character every 80ms.
    #    frame = (frame+1)%8                         # There are 8 frames of animation in each direction
    #    nextFrame += 80                             # so the modulus 8 allows it to loop

    # changeSpriteImage is for animations of the player, no needed
    if keyPressed("right"):
        #changeSpriteImage(testSprite, 0*8+frame)    # 0*8 because right animations are the 0th set in the sprite sheet
        scrollBackground(-5,0)                      # The player is moving right, so we scroll the background left
        
     """
    def scrollBackground(x,y):

      global background

      background.scroll(x,y)
    """

    elif keyPressed("down"):
        #changeSpriteImage(testSprite, 1*8+frame)    # down facing animations are the 1st set
        scrollBackground(0, -5)

    elif keyPressed("left"):
        #changeSpriteImage(testSprite, 2*8+frame)    # and so on
        scrollBackground(5,0)

    elif keyPressed("up"):
        #changeSpriteImage(testSprite,3*8+frame)
        scrollBackground(0,5)

    else:
        #changeSpriteImage(testSprite, 1 * 8 + 5)  # the static facing front look

     # updates screen
    updateDisplay()
    # set fps, not needed until we have animation
    #tick(120)
# wait function, for quitting the game, not needed
#endWait()
