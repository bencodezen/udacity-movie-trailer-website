import fresh_tomatoes
import movie

the_incredibles = movie.Movie("The Incredibles", "https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg", "https://www.youtube.com/watch?v=eZbzbC9285I")
ratatouille = movie.Movie("Ratatouille", "http://static.rogerebert.com/uploads/movie/movie_poster/ratatouille-2007/large_taAPNsf6G4EXBYSG7Jyvd9HHKnH.jpg", "https://www.youtube.com/watch?v=c3sBBRxDAqk")
inside_out = movie.Movie("Inside Out", "https://images-na.ssl-images-amazon.com/images/M/MV5BOTgxMDQwMDk0OF5BMl5BanBnXkFtZTgwNjU5OTg2NDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg", "https://www.youtube.com/watch?v=_MC3XuMvsDI")
monsters_inc = movie.Movie("Monsters Inc", "https://lumiere-a.akamaihd.net/v1/images/image_3c4add40.jpeg", "https://www.youtube.com/watch?v=cvOQeozL4S0")

movies = [the_incredibles, ratatouille, inside_out, monsters_inc]

fresh_tomatoes.open_movies_page(movies)
