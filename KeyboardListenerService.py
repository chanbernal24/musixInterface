import time

import keyboard
import pygame


class KeyboardListenerService:

    def __init__(self):
        pass

    def listen(self):

        # KEYBOARD KEYS
        # s = STOP
        # p = PAUSE
        # u = UNPAUSE



        if keyboard.is_pressed('s'):
            print("\nThe song is stopped.\n")
            pygame.mixer.music.stop()
        elif keyboard.is_pressed('p'):
            print("\nThe song is paused.\n")
            pygame.mixer.music.pause()
            # musicService.playSongWithLyrics(5)
            # time.sleep(3)
            # pygame.mixer.music.unpause()
            # pygame.mixer.music.play(1, 0, 12000)
        elif keyboard.is_pressed('u'):
            print("\nThe song is unpaused.\n")
            pygame.mixer.music.unpause()


from MusicService import MusicService

musicService = MusicService()
