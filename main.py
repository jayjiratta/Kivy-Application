# main.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
import random

class Char:
    def __init__(self, name, char_type, mana, hp):
        self.name = name
        self.char_type = char_type
        self.mana = mana
        self.hp = hp

    def get_mana(self):
        return self.mana

    def get_hp(self):
        return self.hp

    def print_info(self):
        print("Name:", self.name)
        print('Type:', self.char_type)
        print('Mana:', self.mana)
        print('HP:', self.hp)

    def skill_with_damage_and_mana(self):
        characters = {
            'Karina': [('Skill 1', 30, 20), ('Skill 2', 40, 30), ('Skill 3', 50, 40)],
            'Winter': [('Skill 1', 25, 15), ('Skill 2', 35, 25), ('Skill 3', 45, 35)],
            'Giselle': [('Skill 1', 35, 25), ('Skill 2', 45, 35), ('Skill 3', 55, 45)],
            'Ningning': [('Skill 1', 20, 10), ('Skill 2', 30, 20), ('Skill 3', 40, 30)]
        }

        for skill, damage, mana in characters[self.name]:
            print(f"{skill} damage {damage} mana {mana}")

    def attack(self, target, skill_number):
        skills = {
            'Karina': [30, 40, 50],
            'Winter': [25, 35, 45],
            'Giselle': [35, 45, 55],
            'Ningning': [20, 30, 40]
        }

        if 1 <= skill_number <= 3:
            damage = skills[self.name][skill_number - 1]
            mana_cost = Char[self.name][skill_number - 1][2]

            if self.mana >= mana_cost:
                target.hp -= damage
                self.mana -= mana_cost

        self.hp = max(self.hp, 0)
        self.mana = max(self.mana, 0)

Karina = Char('Karina', 'Rocket puncher', 100, 100)
Winter = Char('Winter', 'armamenter', 100, 100)
Giselle = Char('Giselle', 'xenoglossy', 100, 100)
Ningning = Char('Ningning', 'xenoglossy', 100, 100)

class MainApp(App):
    def build(self):
        # Create screens
        screen_manager = ScreenManager()

        # Welcome Screen
        welcome_screen = Screen(name="welcome")
        welcome_layout = BoxLayout(orientation='vertical')
        welcome_label = Label(text="Welcome to MYs world!!!")
        
        # Char details layout
        char_detail_layout = BoxLayout(orientation='horizontal')
        
        # Player 1
        player1_label = Label(text="Karina")
        player1_image = Image(source="./image/Karina.jpg")
        player1_layout = BoxLayout(orientation='vertical')
        player1_layout.add_widget(player1_image)
        player1_layout.add_widget(player1_label)
        char_detail_layout.add_widget(player1_layout)
        
        # Player 2
        player2_label = Label(text="Winter")
        player2_image = Image(source="./image/Winter.jpg")
        player2_layout = BoxLayout(orientation='vertical')
        player2_layout.add_widget(player2_image)
        player2_layout.add_widget(player2_label)
        char_detail_layout.add_widget(player2_layout)
        
        # Player 3
        player3_label = Label(text="Giselle")
        player3_image = Image(source="./image/Giselle.jpg")
        player3_layout = BoxLayout(orientation='vertical')
        player3_layout.add_widget(player3_image)
        player3_layout.add_widget(player3_label)
        char_detail_layout.add_widget(player3_layout)
        
        # Player 4
        player4_label = Label(text="Ningning")
        player4_image = Image(source="./image/Ningning.jpg")
        player4_layout = BoxLayout(orientation='vertical')
        player4_layout.add_widget(player4_image)
        player4_layout.add_widget(player4_label)
        char_detail_layout.add_widget(player4_layout)
        
        welcome_layout.add_widget(welcome_label)
        welcome_layout.add_widget(char_detail_layout)
        
        start_button = Button(text="Start Game")
        welcome_layout.add_widget(start_button)

        welcome_screen.add_widget(welcome_layout)
        screen_manager.add_widget(welcome_screen)

        return screen_manager

if __name__ == '__main__':
    MainApp().run()




