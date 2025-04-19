import os
import keyboard

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from dotenv import load_dotenv
import pygame
from LyricsService import LyricsService
from DownloadService import DownloadService

load_dotenv()
MUSIC_PATH = os.getenv('MUSIC_PATH', 'music/')


class MusicService:


    def __init__(self):
        pass

    def listAllSongs(self):
        arr = self.getAllSongs()
        index = 1

        if len(arr) > 0:
            print("\n🎶 Your songs in the playlist:")

            for index, song in enumerate(arr, start=1):
                print(f"{index}. {song}")
                # index += 1
        else :
            print("There are no songs in the list, please add a song.")

    def addSong(self, songUrl):
        try:
            downloadService = DownloadService()
            if downloadService.download_audio_as_mp3(songUrl):
                print("Song Added!\nYour songs in the playlist are: ")
                self.listAllSongs()

        except Exception as e:
            print(e)

    def deleteSong(self, songIndex):
        try:
            arr = self.getAllSongs()
            os.remove(rf"{MUSIC_PATH}\{arr[songIndex - 1]}")
            print(f"You have successfully deleted the song {arr[songIndex]}")
            self.listAllSongs()
        except Exception as e:
            print(e)

    def getAllSongs(self):
        arr = os.listdir(MUSIC_PATH)
        return arr

    def getTitle(self, index):
        arr = self.getAllSongs()
        return arr[index]

    def playSongWithLyrics(self, index):

        lyricService = LyricsService()
        songs = self.getAllSongs()

        pygame.mixer.init()

        music_file = rf"{MUSIC_PATH}\{songs[index - 1]}"
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(1, 0, 12000)

        print(f"Now playing: {self.getTitle(index - 1)} 🔊\n")

        track_response = lyricService.searchTrack(songs[index - 1], 1)
        lyrics = lyricService.getLyrics(track_response)

        print(lyrics)

        print(f"\n ℹ️ Here are the keyboard listeners:\n\tS = STOP\n\tP = PAUSE")

        while pygame.mixer.music.get_busy():
            keyboardListener.listen()

            pygame.time.Clock().tick(10)

    def isIndexValid(self, index):
        if index <= 0 or index >= len(self.getAllSongs()) or not index.isnumeric():
            return False

        return True

from KeyboardListenerService import KeyboardListenerService
keyboardListener = KeyboardListenerService()
