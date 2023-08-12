from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget

from kivy.core.window import Window

Window.size = (320, 600)


class MyManager(ScreenManager):
    pass


class MainScreen(MDScreen):
    pass


class StatisticsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.box = MDBoxLayout(orientation='vertical')
        self.bar = MDTopAppBar(title="Statistics", left_action_items=[['menu']],
                               right_action_items=[["home", lambda x: self.home()]])
        self.space = MDLabel(text='', size_hint_y=0.05)
        self.data_tables = MDDataTable(
            use_pagination=True,
            column_data=[("TrackName", dp(55)), ("NumberOfPlays", dp(25)), ("LastPlayed", dp(30))],
            row_data=self.view_data(),
            size_hint=(0.90, 0.80),
            pos_hint={"center_x": 0.5, 'center_y': 0.43},
            sorted_on="NumberOfPlays",
            sorted_order='ASC',
            elevation=2,
            background_color_header="lightblue")

        self.box.add_widget(self.bar)
        self.box.add_widget(self.space)
        self.box.add_widget(self.data_tables)
        self.add_widget(self.box)

    def view_data(self):
        """placeholder function """  # note - return as a sorted list
        return [("KingKong", 5, '23/05/2023'), ("PEPFAR 5x5 Strategy for 2023", 10, '24/05/2023'),
                ("Annual Implementation Plan 2024", 6, '7/7/2023')]

    def home(self):
        self.manager.current = 'main'


class SettingsScreen(MDScreen):
    pass


class NewNotesScreen(MDScreen):
    def reader(self):
        self.manager.current = 'noteslist'


class NotesListScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.box = MDBoxLayout(orientation='vertical')
        self.bar = MDTopAppBar(title="NoteList", left_action_items=[['menu']],
                               right_action_items=[["home", lambda x: self.home()],
                                                   ['arrow-left-circle', lambda x: self.noteEdit()]])
        self.space = MDLabel(text='', size_hint_y=0.02)
        self.scroll = MDScrollView()
        self.list = TwoLineListItem(text='Date Note Created', secondary_text='Name of Note', on_release=self.clicked)
        self.scroll.add_widget(self.list)
        self.box.add_widget(self.bar)
        self.box.add_widget(self.space)
        self.box.add_widget(self.scroll)
        self.add_widget(self.box)

    def clicked(self, instance):
        self.parent.current = 'read'

    def noteEdit(self):
        self.parent.current = 'notes'

    def home(self):
        self.manager.current = 'main'


class ReadNotesScreen(MDScreen):
    def editor(self):
        self.manager.current = 'notes'

    def notelist(self):
        self.manager.current = 'noteslist'


class TracksFolderScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.box = MDBoxLayout(orientation='vertical')
        self.bar = MDTopAppBar(title="Folders", left_action_items=[['menu']],
                               right_action_items=[["home", lambda x: self.home()]])
        self.space = MDLabel(text='', size_hint_y=0.02)
        self.scroll = MDScrollView()
        self.list = OneLineIconListItem(IconLeftWidget(icon='folder-music'), text="Utano Concept",
                                        on_release=self.clicked)
        self.scroll.add_widget(self.list)
        self.box.add_widget(self.bar)
        self.box.add_widget(self.space)
        self.box.add_widget(self.scroll)
        self.add_widget(self.box)

    def clicked(self, instance):
        self.parent.current = 'tracks'

    def home(self):
        self.manager.current = 'main'


class TracksScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.box = MDBoxLayout(orientation='vertical')
        self.bar = MDTopAppBar(title="TracksList", left_action_items=[['menu']],
                               right_action_items=[["home", lambda x: self.home()],
                                                   ['arrow-left-circle', lambda x: self.folderlist()]])
        self.space = MDLabel(text='', size_hint_y=0.02)
        self.scroll = MDScrollView()
        self.list = OneLineIconListItem(IconLeftWidget(icon='music-circle'), text="TrackOne", on_release=self.clicked)
        self.scroll.add_widget(self.list)
        self.box.add_widget(self.bar)
        self.box.add_widget(self.space)
        self.box.add_widget(self.scroll)
        self.add_widget(self.box)

    def clicked(self, instance):
        self.parent.current = 'playing'

    def folderlist(self):
        self.manager.current = 'folder'

    def home(self):
        self.manager.current = 'main'


class PlayingScreen(MDScreen):
    def tracklist(self):
        self.manager.current = 'tracks'


class ListeningApp(MDApp):

    def callback(self, button):
        MDApp.get_running_app().root.current = 'main'


if __name__ == "__main__":
    ListeningApp().run()
