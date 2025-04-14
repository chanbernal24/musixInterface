from MusicService import MusicService

musicService = MusicService()
#
# songUrl = input("Enter Song URL: ")
#
# musicService.addSong(songUrl)

musicService.listAllSongs()

songIndex = int(input("\nEnter Song Index to play: "))

musicService.playSongWithLyrics(songIndex)







