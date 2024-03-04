from __intis__ import *
class theHub(MDApp):
    global screenManager
    screenManager = ScreenManager()
    MoviePoster = StringProperty()
    Info = StringProperty()
    Cast = StringProperty()
    movieTitle = StringProperty()
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        self.modal = SpinnerPopup()
        screenManager.add_widget(Builder.load_file('screens/main.kv'))
        #screenManager.add_widget(Builder.load_file('screens/home.kv'))
        screenManager.add_widget(Builder.load_file('screens/about.kv'))
        return screenManager

    def show_movie_details(self,title,link,moviePoster):
        self.MoviePoster = moviePoster
        try:
            details = getMovieDetails(link)
            self.movieTitle = title
            self.Info = details[0][0]
            self.Cast = details[0][2][6:]
            
            screenManager.transition.direction="left"
            screenManager.current = "about"
        except requests.exceptions.ConnectionError:
            print("error connecting...please try again")

    def on_start(self):
        trending_movies = getMovies(1)
        popular_movies = getPopularMovies()
        animated_movies = getAnimations()
        action_movies = getAction()
        if trending_movies !={}:
            for i in range(0,22):
                card = TrendingCard()
                card.movieTitle = f"{trending_movies[i][0]}"
                card.moviePoster = f"https:{trending_movies[i][2]}"
                card.movieLink = f"{trending_movies[i][1]}"
                screenManager.get_screen("main").ids.trending_corousel.add_widget(card)
            
            for i in range(12,len(popular_movies)):
                card = TrendingCard()
                f = random.randint(0,len(popular_movies))
                card.movieTitle = f"{popular_movies[i][0]}"
                card.moviePoster = f"https:{popular_movies[i][2]}"
                card.movieLink = f"{popular_movies[i][1]}"
                screenManager.get_screen("main").ids.popular_corousel.add_widget(card)
                    
            for i in range(8,len(animated_movies)) :
                card = TrendingCard()
                f = random.randint(0,len(animated_movies))
                card.movieTitle = f"{animated_movies[i][0]}"
                card.moviePoster = f"https:{animated_movies[i][2]}"
                card.movieLink = f"{animated_movies[i][1]}"
                screenManager.get_screen("main").ids.animations_corousel.add_widget(card)
            for i in range(8,len(action_movies)) :
                card = TrendingCard()
                f = random.randint(0,len(action_movies))
                card.movieTitle = f"{action_movies[i][0]}"
                card.moviePoster = f"https:{action_movies[i][2]}"
                card.movieLink = f"{action_movies[i][1]}"
                screenManager.get_screen("main").ids.action_corousel.add_widget(card)
      
if __name__ == '__main__':
    LabelBase.register(name="MPoppins",fn_regular="assets/fonts/Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins",fn_regular="assets/fonts/Poppins-SemiBold.ttf")
    theHub().run()