import arcade
import arcade.gui
# Set how many rows and columns we will have
SPRITE_SCALING = 0.13

ROW_COUNT = 7
COLUMN_COUNT = 7

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 80
HEIGHT = 80

# This sets the margin between each cell
# and on the edges of the screen.``65
MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN + 100
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Array Backed Grid Example"


class Player(arcade.Sprite):
    """ Player Class """

    def update(self):
        """ Move the player """
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 1
        elif self.right > SCREEN_WIDTH - 5:
            self.right = SCREEN_WIDTH - 5

        if self.bottom < 0:
            self.bottom = 1
        elif self.top > SCREEN_HEIGHT - 5:
            self.top = SCREEN_HEIGHT - 5


laser_sound = arcade.load_sound("laser.wav")
impact_sound = arcade.load_sound("impact.wav")

class WelcomeView(arcade.View):
    def on_show_view(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.color.AMAZON)
        self.background = arcade.load_texture("int.png")
        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)
    def on_draw(self):
        """ Draw this view """
        self.clear()

        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        ins_view = InstructionView()
        ins_view.on_show_view()
        self.window.show_view(ins_view)

class InstructionView(arcade.View):

    def on_show_view(self):
        """ This is run once when we switch to this view """
        self.background = arcade.load_texture("bg.png")
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()
        self.v_box = arcade.gui.UIBoxLayout()
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

        quit = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.v_box.add(quit.with_space_around(bottom=20))

        self.uimanager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x",anchor_y="center_y",child=self.v_box))
        start_button.on_click = self.on_buttonclick1
        quit.on_click = self.on_buttonclick2

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)
    def on_draw(self):
        """ Draw this view """
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,self.background)
#        arcade.draw_text("Two Player Snail Game", self.window.width / 2, self.window.height / 2,arcade.color.ANDROID_GREEN, font_size=30, anchor_x="center")
        self.uimanager.draw()

    def on_buttonclick1(self, event):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)
    def on_buttonclick2(self, event):
        exit()




class GameView(arcade.View):
    row1 = 0
    col1 = 0
    row2 = 5
    col2 = 6
    score = 0
    score2 = 0
    switch = 1
    restricted_p1 = []
    restricted_p2 = []

    def __init__(self):
        super().__init__()

        # Create a 2 dimensional array. A two-dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell
        self.player_list = None
        self.player_sprite = None
        self.splash_p1 = None
        self.player_splash = None
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.splash_p1 = arcade.SpriteList()
        # Set up the player
        self.player_sprite = Player("snail.png", SPRITE_SCALING)
        self.player_2 = Player("snail2.png", SPRITE_SCALING)
        self.player_2.center_x = 45 + (85 * 6)
        self.player_2.center_y = 45 + (85 * 5)

        self.player_sprite.center_x = 45
        self.player_sprite.center_y = 45
        self.player_list.append(self.player_sprite)
        self.player_list.append(self.player_2)

    #   self.splash_p1.append(self.copy)
    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player
        self.player_list.update()
        self.splash_p1.update()

    def Splash(self, center_x, center_y):
        self.player_splash = Player("splash.png", SPRITE_SCALING)
        self.player_splash.center_x = center_x
        self.player_splash.center_y = center_y
        self.player_list.append(self.player_splash)

    def Splash2(self, center_x, center_y):
        self.player_splash = Player("splash2.png", SPRITE_SCALING)
        self.player_splash.center_x = center_x
        self.player_splash.center_y = center_y
        self.player_list.append(self.player_splash)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()
        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the boxself.score+=1
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.BLACK

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the bo5x
                self.player_sprite.draw()
                self.player_2.draw()
                self.player_list.draw()
                #   self.player_splash.draw()

                output = f"Score"
                arcade.draw_text(text=output, start_x=85 * 7 + 15, start_y=85 * 6.5, color=arcade.color.BLACK,
                                 font_size=14)
                output = f"Player's"
                arcade.draw_text(text=output, start_x=85 * 7 + 15, start_y=85 * 5.5, color=arcade.color.BLACK,
                                 font_size=14)
                output = f"P1: {self.score}"
                arcade.draw_text(text=output, start_x=85*7+15, start_y=85*6.2, color=arcade.color.ANDROID_GREEN, font_size=14)
                output = f"P2: {self.score2}"
                arcade.draw_text(text=output, start_x=85 * 7 + 15, start_y=85 * 6, color=arcade.color.BLIZZARD_BLUE,
                                 font_size=14)

                output = f"Turn: {self.switch}"
                arcade.draw_text(text=output, start_x=85*7+15, start_y=85*5.3, color=arcade.color.ANDROID_GREEN, font_size=14)
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_key_press(self, key, modifiers):

        if self.switch == 2:
            if key == arcade.key.W:
                arcade.play_sound(laser_sound)
                if (self.row1 + 1, self.col1) not in self.restricted_p2 and (self.row1 + 1, self.col1) != (
                self.row2, self.col2):
                    self.restricted_p1.append((self.row1, self.col1))
                    self.Splash(self.player_sprite.center_x, self.player_sprite.center_y)
                    self.switch = 11
                    self.score += 1

                return 0
            if key == arcade.key.A:
                arcade.play_sound(laser_sound)
                if (self.row1, self.col1 - 1) not in self.restricted_p2 and (self.row1, self.col1 - 1) != (
                self.row2, self.col2):
                    self.restricted_p1.append((self.row1, self.col1))
                    self.Splash(self.player_sprite.center_x, self.player_sprite.center_y)
                    self.switch = 11
                    self.score += 1

                return 0
            if key == arcade.key.S:
                arcade.play_sound(laser_sound)
                if (self.row1 - 1, self.col1) not in self.restricted_p2 and (self.row1 - 1, self.col1) != (
                self.row2, self.col2):
                    self.restricted_p1.append((self.row1, self.col1))
                    self.Splash(self.player_sprite.center_x, self.player_sprite.center_y)
                    self.switch = 11
                    self.score += 1

                return 0
            if key == arcade.key.D:
                arcade.play_sound(laser_sound)
                if (self.row1, self.col1 + 1) not in self.restricted_p2 and (self.row1, self.col1 + 1) != (
                self.row2, self.col2):
                    self.restricted_p1.append((self.row1, self.col1))
                    self.Splash(self.player_sprite.center_x, self.player_sprite.center_y)
                    self.switch = 11
                    self.score += 1
                return 0
        if self.switch == 1:
            if key == arcade.key.UP:
                arcade.play_sound(impact_sound)
                if (self.row2 + 1, self.col2) not in self.restricted_p1 and (self.row2 + 1, self.col2) != (
                self.row1, self.col1):
                    self.restricted_p2.append((self.row2, self.col2))
                    self.Splash2(self.player_2.center_x, self.player_2.center_y)
                    self.switch = 22
                    self.score2 += 1

                return 0
            if key == arcade.key.LEFT:
                arcade.play_sound(impact_sound)
                if (self.row2, self.col2 - 1) not in self.restricted_p1 and (self.row2, self.col2 - 1) != (
                self.row1, self.col1):
                    self.restricted_p2.append((self.row2, self.col2))
                    self.Splash2(self.player_2.center_x, self.player_2.center_y)
                    self.switch = 22
                    self.score2 += 1

                return 0
            if key == arcade.key.DOWN:
                arcade.play_sound(impact_sound)
                if (self.row2 - 1, self.col2) not in self.restricted_p1 and (self.row2 - 1, self.col2) != (
                self.row1, self.col1):
                    self.restricted_p2.append((self.row2, self.col2))
                    self.Splash2(self.player_2.center_x, self.player_2.center_y)
                    self.switch = 22
                    self.score2 += 1

                return 0
            if key == arcade.key.RIGHT:
                arcade.play_sound(impact_sound)
                if (self.row2, self.col2 + 1) not in self.restricted_p1 and (self.row2, self.col2 + 1) != (
                self.row1, self.col1):
                    self.restricted_p2.append((self.row2, self.col2))
                    self.Splash2(self.player_2.center_x, self.player_2.center_y)
                    self.switch = 22
                    self.score2 += 1

                return 0

    def on_key_release(self, key, modifiers):
        print(self.restricted_p1)
        if self.switch == 22:
            print("Turn of Player 1")
            if key == arcade.key.UP:
                if self.row2 < ROW_COUNT - 1:
                    if (self.row2 + 1, self.col2) not in self.restricted_p1 and (self.row2 + 1, self.col2) != (
                    self.row1, self.col1):
                        self.row2 += 1
                        self.player_2.center_y += 85
                        self.switch = 2
                    return 0
            if key == arcade.key.DOWN:
                if self.row2 > 0:
                    if (self.row2 - 1, self.col2) not in self.restricted_p1 and (self.row2 - 1, self.col2) != (
                    self.row1, self.col1):
                        self.row2 -= 1
                        self.player_2.center_y += -85
                        self.switch = 2
                    return 0
            if key == arcade.key.RIGHT:
                if self.col2 < COLUMN_COUNT - 1:
                    if (self.row2, self.col2 + 1) not in self.restricted_p1 and (self.row2, self.col2 + 1) != (
                    self.row1, self.col1):
                        self.col2 += 1
                        self.player_2.center_x += 85
                        self.switch = 2
                    return 0
            if key == arcade.key.LEFT:
                if self.col2 > 0:
                    if (self.row2, self.col2 - 1) not in self.restricted_p1 and (self.row2, self.col2 - 1) != (
                    self.row1, self.col1):
                        self.col2 -= 1
                        self.player_2.center_x += -85
                        self.switch = 2
                    return 0
        if self.switch == 11:
            print("Turn of Player 2")
            if key == arcade.key.W:
                if self.row1 < ROW_COUNT - 1:
                    if (self.row1 + 1, self.col1) not in self.restricted_p2 and (self.row1 + 1, self.col1) != (
                    self.row2, self.col2):
                        self.row1 += 1
                        # print("Row", self.row)
                        self.player_sprite.center_y += 85
                        self.switch = 1
                        return 0
            if key == arcade.key.S:
                if self.row1 > 0:
                    if (self.row1 - 1, self.col1) not in self.restricted_p2 and (self.row1 - 1, self.col1) != (
                    self.row2, self.col2):
                        self.row1 -= 1
                        # print("Row",self.row)
                        self.player_sprite.center_y += -85
                        self.switch = 1
                    return 0
            if key == arcade.key.D:
                if self.col1 < COLUMN_COUNT - 1:
                    if (self.row1, self.col1 + 1) not in self.restricted_p2 and (self.row1, self.col1 + 1) != (
                    self.row2, self.col2):
                        self.col1 += 1
                        #  print("Col",self.col)
                        self.player_sprite.center_x += 85
                        self.switch = 1
                    return 0
            if key == arcade.key.A:
                if self.col1 > 0:
                    if (self.row1, self.col1 - 1) not in self.restricted_p2 and (self.row1, self.col1 - 1) != (
                    self.row2, self.col2):
                        self.col1 -= 1
                        # print("Col",self.col)
                        self.player_sprite.center_x += -85
                        self.switch = 1
                    return 0


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = WelcomeView()
    window.show_view(start_view)
    arcade.run()


main()
