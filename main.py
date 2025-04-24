from MusicService import MusicService
import pygame
import keyboard
import sys
from MusixInterface import MusixInterface

musicService = MusicService()

# songUrl = input("Enter Song URL: ")
#
# musicService.addSong(songUrl)
#

try:
    cli = MusixInterface()
    cli.run()
except Exception as e:
    print(f"❌ Critical error: {e}")
    print("The application will now exit.")
    sys.exit(1)
