"""
Import library for generating HTML pages
Import library for Movie class
"""
import fresh_tomatoes
import movie

# Create four instances of Movie class
the_incredibles = movie.Movie("The Incredibles",
                              "https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg",  # noqa
                              "https://www.youtube.com/watch?v=eZbzbC9285I")
ratatouille = movie.Movie("Ratatouille",
                          "http://bit.ly/2wX8CfR",

                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")
inside_out = movie.Movie("Inside Out",
                         "http://bit.ly/2wWWBqD",
                         "https://www.youtube.com/watch?v=_MC3XuMvsDI")
monsters_inc = movie.Movie("Monsters Inc",
                           "https://lumiere-a.akamaihd.net/v1/images/image_3c4add40.jpeg",  # noqa
                           "https://www.youtube.com/watch?v=cvOQeozL4S0")

# Create a list of all movies to use in the web page
movies = [the_incredibles, ratatouille, inside_out, monsters_inc]

# Call function to open web page with all movies inside of it
fresh_tomatoes.open_movies_page(movies)
