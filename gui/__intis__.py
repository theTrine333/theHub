from kivymd.app import MDApp
from kivy.base import Builder
from kivymd.uix.screenmanager import ScreenManager
from kivy.uix.modalview import ModalView
from kivy.core.window import Window
from kivymd.uix.imagelist import MDSmartTile
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.text import LabelBase
from kivy.properties import StringProperty
from kivy.network.urlrequest import UrlRequest
from goojara import *
import random

Window.size = (360,720)

class TrendingCard(MDSmartTile):
    movieTitle = StringProperty()
    movieLink = StringProperty()
    moviePoster = StringProperty()

class MovieCard(MDSmartTile):
    movieTitle = StringProperty()
    movieLink = StringProperty()
    moviePoster = StringProperty()
    
class MoviesCarousel(MDBoxLayout):
    pass
class SpinnerPopup(ModalView):
    pass