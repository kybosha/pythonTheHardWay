class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
	war_pigs = "Generals gather in their masses."

happy_bday = Song(["Happy birthday to you",
		"I don't want to get sued",
		"So I'll stop right there!"])

bulls_on_parade = Song(["They rall around the family",
			"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

oasis = Song(["What's the story morning glory?"])

yesterday = """Yesterday\n
All my troubles seemed so far away."""

#yesterday.sing_me_a_song()

print Song.war_pigs

