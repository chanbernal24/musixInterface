import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from LyricsService import LyricsService
import json

from DownloadService import DownloadService


class MusicService:

    def __init__(self):
        pass

    def listAllSongs(self):
        arr = self.getAllSongs()
        index = 1

        print("\n🎶 Your songs in the playlist:")

        for index, song in enumerate(arr, start=1):
            print(f"{index}. {song}")
            # index += 1

    def addSong(self, songUrl):
        try:
            downloadService = DownloadService()
            if downloadService.download_audio_as_mp3(songUrl):
                print("Song Added\nYour songs in the playlist are: ")
                self.listAllSongs()

        except Exception as e:
            print(e)

    def deleteSong(self, songIndex):
        try:
            arr = self.getAllSongs()
            os.remove(rf"C:\Users\berna\PycharmProjects\mp3playercli\music\{arr[songIndex - 1]}")
            print(f"You have successfully deleted the song {arr[songIndex]}")
            self.listAllSongs()
        except Exception as e:
            print(e)

    def getAllSongs(self):
        arr = os.listdir(r"C:\Users\berna\PycharmProjects\mp3playercli\music")
        return arr

    def getTitle(self, index):
        arr = self.getAllSongs()
        return arr[index]

    def playSongWithLyrics(self, index):
        lyricService = LyricsService()
        songs = self.getAllSongs()

        pygame.mixer.init()

        music_file = rf"C:\Users\berna\PycharmProjects\mp3playercli\music\{songs[index - 1]}"
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)

        print(f"Now playing: {self.getTitle(index - 1)} 🔊\n")

        track_response = lyricService.searchTrack(songs[index - 1], 1)
        lyrics = lyricService.getLyrics(track_response)

        print(lyrics)

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


