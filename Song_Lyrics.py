class Song(object):

    def __init__(self, lyrics, artist,title):
        self.lyrics = lyrics
        self.artist = artist
        self.title = title

    def sing_me_a_song(self):
        print self.artist
        print self.title
        for line in self.lyrics:
            print line

What_Is_Love = Song(["What is love?",
"Oh baby, don't hurt me", 
"Don't hurt me no more"], "Haddaway", "What Is Love"])

hotline_bling = Song(["You used to call me on my",
                      "You used to, you used to",
                      "Yeah"], "Drake", "Hotline Bling")
# This is your daily reminder that Drake is Canadian

What_Is_Love.sing_me_a_song()
hotline_bling.sing_me_a_song()
