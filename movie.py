"""
Define the Movie class
"""
class Movie():
    def __init__(self, movie_title, movie_artwork, movie_trailer_url):
        self.title = movie_title
        self.poster_image_url = movie_artwork
        self.trailer_youtube_url = movie_trailer_url
