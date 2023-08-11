from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.recycleview import RecycleView

class MyManager(MDScreenManager):
    pass


class MainScreen(MDScreen):
    pass


class TracksScreen(MDScreen):
    pass


class StatisticsScreen(MDScreen):
    pass

class SettingsScreen(MDScreen):
    pass

class NotesScreen(MDScreen):
    pass

class PlayingScreen(MDScreen):
    pass

class MyRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class ListeningApp(MDApp):
    pass


if __name__ == "__main__":
    ListeningApp().run()