from MusicService import MusicService
import pygame
import keyboard


musicService = MusicService()

# songUrl = input("Enter Song URL: ")
#
# musicService.addSong(songUrl)
#

songIndex = int(input("\nEnter Song Index to play: "))

musicService.playSongWithLyrics(songIndex)
if keyboard.is_pressed('q'):
    pygame.mixer.quit()








