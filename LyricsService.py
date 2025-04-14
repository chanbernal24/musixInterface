from musicxmatch_api import MusixMatchAPI

class LyricsService:
    def __init__(self):
        self.api = MusixMatchAPI()


    def searchTrack(self, q_track, page) :
        resp = self.api.search_tracks(q_track, page)
        return resp

    def getTrackId(self, dict) :
        trackId = dict["message"]["body"]["track_list"][0]["track"]["track_id"]
        return trackId

    def getTrackIsrc(self, dict) :
        trackIsrc = dict["message"]["body"]["track_list"][0]["track"]["track_isrc"]
        return trackIsrc

    def getTrackIdTrackIsrcDict(self, dict) :
        tracksInfo = {
            "trackId" : self.getTrackId(dict),
            "trackIsrc" : self.getTrackIsrc(dict)
        }

        return tracksInfo

    def getLyrics(self, dict) :
        tracksInfo = self.getTrackIdTrackIsrcDict(dict)
        resp = self.api.get_track_lyrics(tracksInfo["trackId"], tracksInfo["trackIsrc"])
        lyrics = resp["message"]["body"]["lyrics"]["lyrics_body"]
        if not lyrics :
            lyrics = "This song has no lyrics."

        return lyrics



