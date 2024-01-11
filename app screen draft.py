
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10

class GameScreen(Screen):
    def __init__(self, player1, player2, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.player1 = player1
        self.player2 = player2

        self.attack_levels = [1, 2, 3]
        self.current_player = random.choice([player1, player2])

        self.layout = BoxLayout(orientation='vertical')
        self.player_label = Label(text=f"{self.current_player.name}'s Turn\nHealth: {self.current_player.health}")
        self.attack_buttons = BoxLayout(orientation='horizontal')

        for level in self.attack_levels:
            button = Button(text=f"Attack {level}", on_press=self.attack)
            self.attack_buttons.add_widget(button)

        self.layout.add_widget(self.player_label)
        self.layout.add_widget(self.attack_buttons)

        self.add_widget(self.layout)

    def attack(self, instance):
        # Simulate an attack and update health
        damage = random.randint(5, 15) * self.current_player.attack * int(instance.text.split()[-1])
        self.current_player.health -= damage

        if self.current_player.health <= 0:
            winner = self.player2 if self.current_player == self.player1 else self.player1
            self.manager.current = "result"
            self.manager.get_screen("result").update_winner(winner.name)
        else:
            # Switch to the other player's turn
            self.current_player = self.player2 if self.current_player == self.player1 else self.player1
            self.player_label.text = f"{self.current_player.name}'s Turn\nHealth: {self.current_player.health}"

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.winner_label = Label(text='')
        self.layout.add_widget(self.winner_label)
        self.add_widget(self.layout)

    def update_winner(self, winner_name):
        self.winner_label.text = f"The winner is {winner_name}"

class MainApp(App):
    def build(self):
        # Create player instances
        player1 = Player("Player 1")
        player2 = Player("Player 2")

        # Create screens
        screen_manager = ScreenManager()

        # Welcome Screen
        welcome_screen = Screen(name="welcome")
        welcome_layout = BoxLayout(orientation='vertical')
        welcome_label = Label(text="Welcome to the Game!")
        start_button = Button(text="Start Game", on_press=lambda x: screen_manager.switch_to(game_screen))
        welcome_layout.add_widget(welcome_label)
        welcome_layout.add_widget(start_button)
        welcome_screen.add_widget(welcome_layout)
        screen_manager.add_widget(welcome_screen)

        # Game Screen
        game_screen = GameScreen(name="game", player1=player1, player2=player2)
        screen_manager.add_widget(game_screen)

        # Result Screen
        result_screen = ResultScreen(name="result")
        screen_manager.add_widget(result_screen)

        return screen_manager

if __name__ == '__main__':
    MainApp().run()


