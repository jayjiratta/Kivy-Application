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
        
        return characters[self.name]

    def attack(self, target, skill_number):
        skills = {
            'Karina': [30, 40, 50],
            'Winter': [25, 35, 45],
            'Giselle': [35, 45, 55],
            'Ningning': [20, 30, 40]
        }

        if 1 <= skill_number <= 3:
            damage = skills[self.name][skill_number - 1]
            mana_cost = self.skill_with_damage_and_mana()[skill_number - 1][2]

            if self.mana >= mana_cost:
                target.hp -= damage
                self.mana -= mana_cost

        self.hp = max(self.hp, 0)
        self.mana = max(self.mana, 0)

Karina = Char('Karina', 'Rocket puncher', 100, 100)
Winter = Char('Winter', 'armamenter', 100, 100)
Giselle = Char('Giselle', 'xenoglossy', 100, 100)
Ningning = Char('Ningning', 'xenoglossy', 100, 100)

class Intro(Screen):
    def __init__(self, **kwargs):
        super(Intro, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        intro_label = Label(text="Welcome to MYs world!!!")
        
        char_detail_layout = BoxLayout(orientation='horizontal')
        
        player1_label = Label(text="Karina")
        player1_image = Image(source="./image/Karina.jpg")
        player1_layout = BoxLayout(orientation='vertical')
        player1_layout.add_widget(player1_image)
        player1_layout.add_widget(player1_label)
        char_detail_layout.add_widget(player1_layout)
        
        player2_label = Label(text="Winter")
        player2_image = Image(source="./image/Winter.jpg")
        player2_layout = BoxLayout(orientation='vertical')
        player2_layout.add_widget(player2_image)
        player2_layout.add_widget(player2_label)
        char_detail_layout.add_widget(player2_layout)
        
        player3_label = Label(text="Giselle")
        player3_image = Image(source="./image/Giselle.jpg")
        player3_layout = BoxLayout(orientation='vertical')
        player3_layout.add_widget(player3_image)
        player3_layout.add_widget(player3_label)
        char_detail_layout.add_widget(player3_layout)
        
        player4_label = Label(text="Ningning")
        player4_image = Image(source="./image/Ningning.jpg")
        player4_layout = BoxLayout(orientation='vertical')
        player4_layout.add_widget(player4_image)
        player4_layout.add_widget(player4_label)
        char_detail_layout.add_widget(player4_layout)
        
        self.layout.add_widget(intro_label)
        self.layout.add_widget(char_detail_layout)

        start_button = Button(text="Start Game", on_press=self.start_game)
        self.layout.add_widget(start_button)

        self.add_widget(self.layout)
    
    def start_game(self, instance):
        self.manager.current = "character_selection"

class CharacterSelectionScreen(Screen):
    def __init__(self, **kwargs):
        super(CharacterSelectionScreen, self).__init__(**kwargs)
        self.layout1 = BoxLayout(orientation='vertical')
        self.selected_char_label = Label(text="Select Your Character", size_hint=(None, None), size=(200, 100),pos_hint={'center_x': 0.5, 'center_y': 0.5})
        char_select = Label(text="CharacterSelectionScreen", size_hint=(None, None), size=(200, 100),pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.layout1.add_widget(char_select)
        char_detail_layout = BoxLayout(orientation='horizontal')
        
        for char_name in ['Karina', 'Winter', 'Giselle', 'Ningning']:
            player_image = Image(source=f"./image/{char_name}.jpg")
            char_button = Button(text=char_name, on_press=lambda x, char_name=char_name: self.select_character(char_name),size_hint=(1, 0.25))
            skill = Label(text = self.display_attack_skills(char_name))
            player_layout = BoxLayout(orientation='vertical')
            player_layout.add_widget(player_image)
            player_layout.add_widget(skill)
            player_layout.add_widget(char_button)
            char_detail_layout.add_widget(player_layout)

        self.layout1.add_widget(char_detail_layout)
        start_button = Button(text="Start Game", on_press=self.start_game,size_hint=(1, 0.25))
        self.layout1.add_widget(self.selected_char_label)
        self.layout1.add_widget(start_button)
        self.add_widget(self.layout1)
        self.player1_char = None
        self.player2_char = None

    def select_character(self, char_name):
        if self.player1_char is None:
            self.player1_char = Char(char_name, 'Type', 100, 100)
            self.selected_char_label.text = f"Player 1 selected: {char_name}"
        elif self.player2_char is None:
            self.player2_char = Char(char_name, 'Type', 100, 100)
            self.selected_char_label.text = f"Player 2 selected: {char_name}"

    def display_attack_skills(self, character):
        char_instance = Char(character, 'Type', 100, 100) 
        attack_skills = char_instance.skill_with_damage_and_mana()
        skills_text = "Attack Skills:\n"
        for skill, damage, mana in attack_skills:
            skills_text += f"{skill} - Damage: {damage}, Mana: {mana}\n"
        return skills_text

    def start_game(self, instance):
        if self.player1_char is not None and self.player2_char is not None:
            self.manager.get_screen("game").set_players(self.player1_char, self.player2_char)
            self.manager.current = "game"
        else:
            self.selected_char_label.text = "Both players must select a character."

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.player1 = None
        self.player2 = None

        self.attack_levels = [1, 2, 3]
        self.current_player = None

        self.layout = BoxLayout(orientation='vertical')
        self.player_label = Label(text="", font_size=20)
        self.player_skill_use = Label(text="", font_size=20)
        self.attack_buttons = BoxLayout(orientation='horizontal')

        for level in self.attack_levels:
            button = Button(text=f"Attack {level}", on_press=self.attack,size_hint=(1, 0.75))
            self.attack_buttons.add_widget(button)

        self.layout.add_widget(self.player_label)
        self.layout.add_widget(self.player_skill_use)
        self.layout.add_widget(self.attack_buttons)

        self.add_widget(self.layout)

    def set_players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = random.choice([player1, player2])
        self.update_player_label()
        self.skill_use()

    def update_player_label(self):
        enemy = self.player2 if self.current_player == self.player1 else self.player1
        self.player_label.text = f"{self.current_player.name}'s Turn\nHealth: {self.current_player.hp}\nMana:{self.current_player.mana} \n\nEnemy: {enemy.name}'s Health: {enemy.hp}"
    
    def skill_use(self):
        skills = self.current_player.skill_with_damage_and_mana()
        self.player_skill_use.text = "Attack Skills:\n"
        for skill, damage, mana in skills:
            self.player_skill_use.text += f"{skill} - Damage: {damage}, Mana: {mana}\n"
        
    def attack(self, instance):
        if self.current_player == self.player1:
            target = self.player2
        else:
            target = self.player1

        self.current_player.attack(target, int(instance.text.split()[-1]))

        if self.player1.hp <= 0 or self.player2.hp <= 0:
            winner = self.player2 if self.player1.hp <= 0 else self.player1
            self.manager.get_screen("result").update_winner(winner.name)
            self.manager.current = "result"
        else:
            self.current_player = self.player2 if self.current_player == self.player1 else self.player1
            self.update_player_label()
            self.skill_use()
        
class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.winner_label = Label(text='', font_size=20)
        self.layout.add_widget(self.winner_label)
        self.add_widget(self.layout)

    def update_winner(self, winner_name):
        self.winner_label.text = f"The winner is {winner_name}"

class MainApp(App):
    def build(self):
        screen_manager = ScreenManager()

        intro_screen = Intro(name="intro")
        screen_manager.add_widget(intro_screen)

        character_selection_screen = CharacterSelectionScreen(name="character_selection")
        screen_manager.add_widget(character_selection_screen)

        game_screen = GameScreen(name="game")
        screen_manager.add_widget(game_screen)

        result_screen = ResultScreen(name="result")
        screen_manager.add_widget(result_screen)

        return screen_manager

if __name__ == '__main__':
    MainApp().run()




