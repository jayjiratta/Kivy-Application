# main.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

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

# Instances of characters
Karina = Char('Karina', 'Rocket puncher', 100, 100)
Winter = Char('Winter', 'armamenter', 100, 100)
Giselle = Char('Giselle', 'xenoglossy', 100, 100)
Ningning = Char('Ningning', 'xenoglossy', 100, 100)

class BattleApp(App):
    def build(self):
        self.title = 'Welcome to my Game'
        self.layout = BoxLayout(orientation='vertical', spacing=10)

        # Header Label
        self.header_label = Label(text='Welcome to my Game', font_size=24)
        self.layout.add_widget(self.header_label)

        # Character Selection Section
        self.character_images = {
            'Karina': 'karina_image.png',  # Replace with actual file paths
            'Winter': 'winter_image.png',
            'Giselle': 'giselle_image.png',
            'Ningning': 'ningning_image.png'
        }

        self.character_buttons = []
        for char_name, char_image in self.character_images.items():
            button = Button(text=char_name, on_press=self.select_character)
            self.character_buttons.append(button)
            self.layout.add_widget(button)

        # Selected Characters Display
        self.selected_character_labels = [
            Label(text='Player 1: None'),
            Label(text='Player 2: None')
        ]

        for label in self.selected_character_labels:
            self.layout.add_widget(label)

        # Start Battle Button
        self.start_battle_button = Button(text='Start Battle', on_press=self.start_battle, disabled=True)
        self.layout.add_widget(self.start_battle_button)

        return self.layout

    def select_character(self, instance):
        # Find the index of the clicked button
        button_index = self.character_buttons.index(instance)

        # Determine the player based on the index
        player = 'Player 1' if button_index % 2 == 0 else 'Player 2'

        # Extract the character name from the button text
        character_name = instance.text

        # Update the corresponding label
        self.selected_character_labels[button_index % 2].text = f'{player}: {character_name}'

        # Enable the "Start Battle" button if both players have selected characters
        if all(label.text != f'{player}: None' for player, label in zip(['Player 1', 'Player 2'], self.selected_character_labels)):
            self.start_battle_button.disabled = False

    def start_battle(self, instance):
        # Implement the logic for starting the battle
        pass

# Run the app
if __name__ == '__main__':
    BattleApp().run()

