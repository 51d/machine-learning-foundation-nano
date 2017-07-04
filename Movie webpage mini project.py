import fresh_tomatoes
import class_Movie
dangal = class_Movie.Movie('Dangal',
                           'Story of two sisters who learned wrestling from their father and won a medal in commonwealth games',
                           'http://www.media.glamsham.com/download/poster/images/dangal/04-Dangal.jpg',
                           'https://www.youtube.com/watch?v=x_7YlGv9u1g')
spiderman_returns = class_Movie.Movie('Spiderman homecoming',
                                      'SuperHero',
                                      'http://images.complex.com/complex/images/c_fill,g_center,w_1200/fl_lossy,pg_1,q_auto/uc7ae2rek8ne8ov0ue8e/spider-man-homecoming-poster',
                                      'https://www.youtube.com/watch?v=n9DwoQ7HWvI')
movie = [dangal,spiderman_returns]
fresh_tomatoes.open_movies_page(movie)
