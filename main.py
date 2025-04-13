from MusicService import MusicService



musicService = MusicService()
musicService.listAllSongs()

songIndex = int(input("\nEnter Song Index to play: "))

musicService.playSongWithLyrics(songIndex)







