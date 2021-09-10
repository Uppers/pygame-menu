import pygame

class Menu():

    def __init__(self, game): # reference to game module so we can reuse some of that code.
        self.game = game 
        self.mid_w = int(self.game.DISPLAY_W/2)
        self.mid_h = int(self.game.DISPLAY_H/2)
        self.run_display = True
        self.cursor_rect = pygame.Rect(0,0,20,20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text("*", 20,self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):

    def __init__(self, game):
        super().__init__(game)
        self.state = "Start"
        self.startx = self.mid_w
        self.starty = self.mid_h + 30
        self.optionsx = self.mid_w
        self.optionsy = self.mid_h + 50
        self.creditsx = self.mid_w
        self.creditsy = self.mid_h + 70
        self.cursor_rect.midtop = (self.startx+self.offset, self.starty) # starts the cursor at the start option

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input() # check what the user did
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("Main Menu", 20, self.mid_w, self.mid_h-20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Options", 20, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = "Options"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
        elif self.game.UP_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = "Options"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"



    def check_input(self):
        self.move_cursor() # did the player move the cursor?
        if self.game.START_KEY: # if RETURN key has been pressed
            if self.state == "Start":
                self.game.playing = True # start playing the game
            elif self.state == "Options":
                self.game.curr_menu  = self.game.options_menu
            elif self.state == "Credits":
                self.game.curr_menu = self.game.credits_menu
            self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state = "Volume" # options menu starts at the state for navigateing through the volume settings.
        self.volx, self.voly = self.mid_w, self.mid_h + 20 # where to put the volume text
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40 # where to put the controls text
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()     # the options menu requires checking the player input as we're moving the cursor 
            self.check_input()
            self.game.display.fill(self.game.BLACK) # black background
            self.game.draw_text("Options", 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2-30) # title
            self.game.draw_text("Volume", 15, self.volx, self.voly) # volume state
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy) # control state
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY: # to return to the main menu
            self.game.curr_menu = self.game.main_menu # the current menu is the main menu
            self.run_display = False # ends the options menu display
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == "Volume":
                self.state = "Controls"
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            else:
                self.state = "Volume"
                self.cursor_rect.midtop = (self.volx +  self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a volume Menu and a controls menu
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        super().__init__(game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("Credits", 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2-30)
            self.game.draw_text("Made by me", 15, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2-10)
            self.blit_screen()






