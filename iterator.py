#provides a way to sequentially access the elements of a collection without exposing its underlying implementation
class Iterator:
    def has_next(self):
        pass
    def next(self):
        pass
class PlaylistIterator(Iterator):
    def __init__(self,playlist):
        self.playlist=playlist
        self.index=0
    def has_next(self):
        return self.index<len(self.playlist.songs)
    def next(self):
        if self.has_next():
            song=self.playlist.songs[self.index]
            self.index+=1
            return song
        else:
            raise StopIteration("End of playlist")
class PlayList:
    def __init__(self):
        self.songs=[]
    def add_songs(self,songs):
        self.songs.append(songs)
    def create_iterator(self):
        return PlaylistIterator(self)
playlist=PlayList()
playlist.add_songs("song1")
playlist.add_songs("song2")
playlist.add_songs("song3")
iterator=playlist.create_iterator()
while iterator.has_next():
    print(iterator.next())