import pygame
from menu import *

class Game():

    def __init__(self):
        pygame.init()
        self.running = True # the program is running
        self.playing = False # the game is being played
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        self.DISPLAY_W, self.DISPLAY_H = 480, 270 # screen size in px
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = "pygame-menu/8-BIT WONDER.TTF"
        self.BLACK, self.WHITE = (0,0,0), (255,255,255)
        self.main_menu = MainMenu(self)
        self.options_menu = OptionsMenu(self)
        self.credits_menu = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                # Exit game loop
                self.playing = False
            # set background to black
            self.display.fill(self.BLACK) # create a black surface
            self.draw_text("Thanks For Playing", 20, int(self.DISPLAY_W/2), int(self.DISPLAY_H/2))
            self.window.blit(self.display, (0,0)) # window is our screen and we set display to cover our screen
            pygame.display.update() # draws the display on the monitor
            self.reset_keys() # set all flags to false

    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self): # if the key is no longer being pressed we can reset the boolean flag
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    
    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size) # get the font at a given font size
        text_surface = font.render(text, True, self.WHITE) # renders white text
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)
            



