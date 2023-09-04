# My first coding project on Github! :)

# It's a philosophy game, it has a boring graphical interface since I couldn't get the most of the backgrounds to work properly, so I decided to not waste time on something dumb like that. 
# Bored...


import kivy
import os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import LabelBase
from kivy.uix.image import Image

arsenal = r"C:\Users\Mat\Downloads\Arsenal\Arsenal-Bold.ttf"
LabelBase.register(name='Arsenal', fn_regular=arsenal)

class Thinkight(App):
    def build(self):
        self.scrm = ScreenManager()

        self.create_startupscreen()
        self.create_mainscreen()

        return self.scrm
    
    def create_mainscreen(self):
        screen_01 = Screen(name="Thinkight")

        game_title = Label(font_size=60, color=(1, 1, 1, 1), text="Thinkight", pos_hint={'center_x': 0.5, 'top': 10}, font_name="Arsenal")
          
        select_charactertitle_start = Label(font_size = 20, color=(1 ,1, 1, 1), text="Select Thinker", pos_hint={'center_x': 0.5, 'top': 0.8})
        
        layout_1 = BoxLayout(orientation='vertical', size_hint=(1, None), pos_hint={'center_x': 0.5, 'top': 0.9})
        layout_1.add_widget(game_title)
        
        layout_1.add_widget(select_charactertitle_start)

        screen_01.add_widget(layout_1)

        self.scrm.add_widget(screen_01)
    def create_startupscreen(self):
        startup_screen = Screen(name="Thinkights")

        background = Image(source=r"C:\Users\Mat\Downloads\naturephilo.jpg", keep_ratio=False, allow_stretch=True)

        startup_screen.add_widget(background)
        title_label = Label(font_size=40, color=(0.5, 0.5, 1, 1), text="Thinkight", pos_hint={'center_x': 0.5, 'top': 0.95}, font_name="Arsenal")
        
    
        
        startup_screen.add_widget(title_label)

        button_start = Button(text="Start", font_size=30, size=(150, 50), size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        button_start.bind(on_press=self.begin_game)
        startup_screen.add_widget(button_start)

        self.scrm.add_widget(startup_screen)

    def begin_game(self, instance):
        begin_game_screen = Screen(name= "Select Thinkers")
        
        self.scrm.switch_to(Screen(name="Thinkight"))
        self.scrm.current = "Thinkight"
        
        self.scrm.add_widget(begin_game_screen)
        
    

if __name__ == "__main__":
    Thinkight().run()
