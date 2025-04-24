import os
import sys
from MusicService import MusicService
import re


class MusixInterface:
    def __init__(self):
        self.music_service = MusicService()
        self.commands = {
            "help": self.show_help,
            "list": self.list_songs,
            "play": self.play_song,
            "add": self.add_song,
            "delete": self.delete_song,
            "exit": self.exit_program
        }

    def show_help(self, *args):
        print("\n📚 MusixInterface HELP 📚")
        print("Available commands:")
        print("  help                - Show this help message")
        print("  list                - List all available songs")
        print("  play <song_number>  - Play a song by its number")
        print("  add <youtube_url>   - Add a song from YouTube URL")
        print("  delete <song_number> - Delete a song by its number")
        print("  exit                - Exit the program")
        print("\nWhile playing, use keyboard controls:")
        print("  s - Stop song\n")

    def list_songs(self, *args):
        """List all songs in the music library"""
        try:
            self.music_service.listAllSongs()
        except Exception as e:
            print(f"❌ Error listing songs: {e}")

    def get_valid_song_index(self, prompt="Enter song number: "):
        """Get and validate a song index from user input"""
        songs = self.music_service.getAllSongs()
        song_count = len(songs)

        if song_count == 0:
            print("❌ No songs available in the library.")
            return None

        while True:
            try:
                user_input = input(prompt)

                # Check if user wants to cancel
                if user_input.lower() in ['q', 'quit', 'cancel']:
                    print("Operation cancelled.")
                    return None

                index = int(user_input)

                if 1 <= index <= song_count:
                    return index
                else:
                    print(f"⚠️ Please enter a number between 1 and {song_count}. (Enter 'q' to cancel)")
            except ValueError:
                print("⚠️ Please enter a valid number. (Enter 'q' to cancel)")

    def play_song(self, *args):
        """Play a song by its number"""
        try:
            songs = self.music_service.getAllSongs()
            if not songs:
                print("❌ No songs available to play.")
                return

            # Check if argument was provided
            if args and args[0].isdigit():
                song_index = int(args[0])
                if 1 <= song_index <= len(songs):
                    self.music_service.playSongWithLyrics(song_index)
                    return
                else:
                    print(f"⚠️ Song number must be between 1 and {len(songs)}")

            # If we reached here, either no args or invalid args
            self.music_service.listAllSongs()
            song_index = self.get_valid_song_index("Enter the number of the song to play (or 'q' to cancel): ")

            if song_index is not None:
                self.music_service.playSongWithLyrics(song_index)

        except Exception as e:
            print(f"❌ Error in play command: {e}")

    def is_valid_youtube_url(self, url):
        """Validate YouTube URL format"""
        youtube_regex = r'(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+'
        return bool(re.match(youtube_regex, url))

    def get_valid_youtube_url(self):
        """Get and validate a YouTube URL from user input"""
        while True:
            url = input("Enter YouTube URL (or 'q' to cancel): ")

            if url.lower() in ['q', 'quit', 'cancel']:
                print("Operation cancelled.")
                return None

            if self.is_valid_youtube_url(url):
                return url
            else:
                print("⚠️ Invalid YouTube URL format. Please enter a valid URL. (Enter 'q' to cancel)")

    def add_song(self, *args):
        """Add a song from YouTube URL"""
        try:
            # Check if argument was provided
            if args and self.is_valid_youtube_url(args[0]):
                youtube_url = args[0]
            else:
                if args:
                    print("⚠️ Invalid YouTube URL format.")
                youtube_url = self.get_valid_youtube_url()

            if youtube_url:
                print(f"🔄 Attempting to download from: {youtube_url}")
                self.music_service.addSong(youtube_url)
        except Exception as e:
            print(f"❌ Error adding song: {e}")

    def delete_song(self, *args):
        """Delete a song by its number"""
        try:
            songs = self.music_service.getAllSongs()
            if not songs:
                print("❌ No songs available to delete.")
                return

            # Check if argument was provided
            if args and args[0].isdigit():
                song_index = int(args[0])
                if 1 <= song_index <= len(songs):
                    confirm = input(f"Are you sure you want to delete '{songs[song_index - 1]}'? (y/n): ")
                    if confirm.lower() == 'y':
                        self.music_service.deleteSong(song_index)
                    else:
                        print("Deletion cancelled.")
                    return
                else:
                    print(f"⚠️ Song number must be between 1 and {len(songs)}")

            # If we reached here, either no args or invalid args
            self.music_service.listAllSongs()
            song_index = self.get_valid_song_index("Enter the number of the song to delete (or 'q' to cancel): ")

            if song_index is not None:
                confirm = input(f"Are you sure you want to delete '{songs[song_index - 1]}'? (y/n): ")
                if confirm.lower() == 'y':
                    self.music_service.deleteSong(song_index)
                else:
                    print("Deletion cancelled.")

        except Exception as e:
            print(f"❌ Error deleting song: {e}")

    def exit_program(self, *args):
        """Exit the program"""
        print("👋 Thanks for using MusixInterface. Goodbye!")
        sys.exit(0)

    def parse_command(self, user_input):
        """Parse and execute user command"""
        parts = user_input.strip().split()
        if not parts:
            return

        command = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []

        if command in self.commands:
            self.commands[command](*args)
        else:
            print(f"❌ Unknown command '{command}'. Type 'help' for available commands.")

    def run(self):
        """Run the CLI main loop"""
        print("\n🎵 MusixInterface 🎵")
        print("Type 'help' for available commands.")

        while True:
            try:
                user_input = input("\n> ")
                self.parse_command(user_input)
            except KeyboardInterrupt:
                print("\n👋 Program interrupted. Exiting...")
                sys.exit(0)
            except Exception as e:
                print(f"❌ An unexpected error occurred: {e}")


