import arcade

class ComputerSprite:
    def __init__(self):
        self.sprite = None
        self.MINSPEED = 1         # slowest other fish speed
        self.MAXSPEED = 4         # fastest other fish speed
        self.DIRCHANGEFREQ = 2    # % chance of direction change per frame
        self.x, self.y = x, y
        self.vx, self.vy = 0, 0
        self.colrect = arcade.Rect(x, y)

    def set_image(self, image_source, scaling):
        self.sprite = arcade.Sprite(image_source, scaling)

    def set_position(self, x, y):
        self.sprite.center_x = x
        self.sprite.center_y = y

    def move(self):
        """Move the fish according to its velocity & update collision rect"""
        self.sprite.center_y += self.vy
        self.sprite.center_x += self.vx
        self.colrect = arcade.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen, camera):
        """Draws the fish in the game"""
        self.camrect = arcade.Rect(self.x - camera.x, self.y - camera.y, self.size, self.size)
        screen.blit(self.image, self.camrect)

    