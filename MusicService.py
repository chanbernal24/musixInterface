import os
import time

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
        else:
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
            # print(f"You have successfully deleted the song {arr[songIndex]}")
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
        try:
            songs = self.getAllSongs()

            if index < 1 or index > len(songs):
                print(f"⚠️ Invalid song index. Please choose a number between 1 and {len(songs)}")
                return

            pygame.mixer.init()

            song_name = songs[index - 1]
            music_file = f"{MUSIC_PATH}/{song_name}"

            try:
                pygame.mixer.music.load(music_file)
                pygame.mixer.music.play()

                print(f"Now playing: {song_name} 🔊\n")

                keyboard_listener = KeyboardListenerService()

                try:
                    lyricService = LyricsService()
                    track_response = lyricService.searchTrack(song_name, 1)
                    lyrics = lyricService.getLyrics(track_response)
                    print(lyrics)
                except Exception as e:
                    print("⚠️ Could not load lyrics for this song")

                print(f"\n ℹ️ Press 'S' to STOP the song")

                while pygame.mixer.music.get_busy():
                    keyboard_listener.listen()
                    pygame.time.Clock().tick(10)

            except pygame.error as e:
                print(f"❌ Error playing the song: {e}")

        except Exception as e:
            print(f"❌ Error: {e}")

    def isIndexValid(self, index):
        if index <= 0 or index >= len(self.getAllSongs()) or not index.isnumeric():
            return False

        return True


from KeyboardListenerService import KeyboardListenerService

keyboardListener = KeyboardListenerService()
