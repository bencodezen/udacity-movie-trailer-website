"""
Define the Movie class
"""
class Movie():
    """
    Movie class object to store movie related information
    """
    def __init__(self, movie_title, movie_artwork, movie_trailer_url):
        """
        Initialize an instance of the Movie class

        :param movie_title: string
        :param movie_artwork: string
        :param movie_trailer_url: string
        """
        self.title = movie_title
        self.poster_image_url = movie_artwork
        self.trailer_youtube_url = movie_trailer_url
