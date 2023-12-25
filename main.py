# main.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput



class BattleApp(App):
    def build(self):
        self.title = 'Battle App'
        self.layout = BoxLayout(orientation='vertical', spacing=10)

        # Create widgets
        self.label = Label(text='Welcome to the Battle App!')
        self.player1_input = TextInput(hint_text='Input character name for player 1')
        self.player2_input = TextInput(hint_text='Input character name for player 2')
        self.start_button = Button(text='Start Battle', on_press=self.start_battle)

        return self.layout

    def start_battle(self, instance):
        player1_name = self.player1_input.text
        player2_name = self.player2_input.text

# Run the app
if __name__ == '__main__':
    BattleApp().run()
