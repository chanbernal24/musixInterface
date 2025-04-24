import pygame
import keyboard
import time


class KeyboardListenerService:
    def __init__(self):
        # Track if we've already detected a keypress to avoid repeating
        self.key_detected = {
            's': False
        }

    def listen(self):
        # Check for the 'S' key press
        if keyboard.is_pressed('s') and not self.key_detected['s']:
            print("\nThe song is stopped.\n")
            pygame.mixer.music.stop()
            self.key_detected['s'] = True
            return True

        # Reset the key_detected status when key is released
        if not keyboard.is_pressed('s') and self.key_detected['s']:
            self.key_detected['s'] = False

        return False
