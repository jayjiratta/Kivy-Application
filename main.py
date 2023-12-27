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

Karina = Char('Karina', 'Rocket puncher', 100, 100)
Winter = Char('Winter', 'armamenter', 100, 100)
Giselle = Char('Giselle', 'xenoglossy', 100, 100)
Ningning = Char('Ningning', 'xenoglossy', 100, 100)


class BattleApp(App):
    def build(self):
        return BattleLayout()

class BattleLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(BattleLayout, self).__init__(orientation='vertical', spacing=10, **kwargs)

        self.header_label = Label(text='Welcome to my Game', font_size=24)
        self.add_widget(self.header_label)

        self.character_images = {
            'Karina': 'karina_image.png',
            'Winter': 'winter_image.png',
            'Giselle': 'giselle_image.png',
            'Ningning': 'ningning_image.png'
        }

        self.character_buttons = []
        for char_name, char_image in self.character_images.items():
            button = Button(text=char_name, on_press=self.select_character)
            self.character_buttons.append(button)
            self.add_widget(button)

        self.selected_character_labels = [
            Label(text='Player 1: None'),
            Label(text='Player 2: None')
        ]

        for label in self.selected_character_labels:
            self.add_widget(label)

        self.start_battle_button = Button(text='Start Battle', on_press=self.start_battle, disabled=True)
        self.add_widget(self.start_battle_button)

    def select_character(self, instance):

        button_index = self.character_buttons.index(instance)

        player = 'Player 1' if button_index % 2 == 0 else 'Player 2'

        character_name = instance.text

        self.selected_character_labels[button_index % 2].text = f'{player}: {character_name}'

        if all(label.text != f'{player}: None' for player, label in zip(['Player 1', 'Player 2'], self.selected_character_labels)):
            self.start_battle_button.disabled = False

    def start_battle(self, instance):
        pass
    


if __name__ == '__main__':
    BattleApp().run()

