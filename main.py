# การเรียกใช้ kivy ต้องเรียกใช้เมื่อเราเข้าไปใน venv ด้วย ./venv/Scripts/activate ผ่าน powershell
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
import random # เรียก librarie ที่ต้องการใช้

# ใช้คลาสนี้เพื่อแทนตัวละครในเกมทั้งชื่อตัวละคร เลือด มานา รวมถึงสกิลทั้งสามที่ใช้ในการโจมตี (ค่าโจมตี+มานาที่ใช้)
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
# ฟังก์ชั่นการโจมตีที่ได้มากจาก file original 
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

# instance ของคลาส Char ที่เทนชื่อของตัวละครทั้ง 4 
Karina = Char('Karina', 'Rocket puncher', 100, 100)
Winter = Char('Winter', 'armamenter', 100, 100)
Giselle = Char('Giselle', 'xenoglossy', 100, 100)
Ningning = Char('Ningning', 'xenoglossy', 100, 100)

# ใช้เพื่อแสดงการต้อนรับเข้าเกม ชื่อตัวละคร ชื่อตัวละคร และปุ่มไปยังหน้าต่อไป
class Intro(Screen):
    def __init__(self, **kwargs):
        super(Intro, self).__init__(**kwargs)
        # กำหนด layout สำหรับที่ของ Widget 
        self.layout = BoxLayout(orientation='vertical')
        intro_label = Label(text="Welcome to MYs world!!!") 
        
        # กำหนด layout สำหรับที่ของ Widget สำหรับดีเทลของ Char
        char_detail_layout = BoxLayout(orientation='horizontal')
        
        # กำหนดและเพิ่ม Widget ของ ชื่อและรูปภาพของตัวละครทั้ง 4
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
        
        # add widget ของข้อความต้อนรับและชื่อ รูปภาพของตัวละคร
        self.layout.add_widget(intro_label)
        self.layout.add_widget(char_detail_layout)

        # สร้างปุ่มที่เมื่อกดจะทำการเปลี่ยนหน้า
        start_button = Button(text="Start Game", on_press=self.start_game)
        self.layout.add_widget(start_button)

        self.add_widget(self.layout)
    
    # ฟังก์ชั่นที่เรียกเพื่อเปลี่ยนไปหน้าเลือกตัวละคร
    def start_game(self, instance):
        self.manager.current = "character_selection"

# ใช้เพื่อแสดง รูปภาพ ชื่อ ความสามารถของตัวละครทั้ง 4 ให้ผู้เล่นทั้งสองคนเลือก และมีปุ่มสตาร์ทไปเกมหน้าต่อไป
class CharacterSelectionScreen(Screen):
    def __init__(self, **kwargs):
        super(CharacterSelectionScreen, self).__init__(**kwargs)
        # กำหนด layout สำหรับที่ของ Widget และกำหนดข้อความที่จะให้แสดงก่อนเลือกตัวละคร และข้อความบนสุดของหน้าจอ
        self.layout1 = BoxLayout(orientation='vertical')
        self.selected_char_label = Label(text="Select Your Character", size_hint=(None, None), size=(200, 100),pos_hint={'center_x': 0.5, 'center_y': 0.5})
        char_select = Label(text="CharacterSelectionScreen", size_hint=(None, None), size=(200, 100),pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.layout1.add_widget(char_select)
        char_detail_layout = BoxLayout(orientation='horizontal')

        # เก็บตัวละครที่เลือกให้เป็น set ทำให้ไม่สามารถเก็บค่าที่ซ้ำได้
        self.selected_characters = set()
        
        # แสดงรูปภาพ ชื่อ(เป็นปุ่มสำหรับกดเลือกตัวละคร) ความสามารถของตัวครแต่ละตัว พร้อมกับ add widget
        for char_name in ['Karina', 'Winter', 'Giselle', 'Ningning']:
            player_image = Image(source=f"./image/{char_name}.jpg")
            char_button = Button(text=char_name, on_press=lambda x, char_name=char_name: self.select_character(char_name),size_hint=(1, 0.25))
            skill = Label(text = self.display_attack_skills(char_name))
            player_layout = BoxLayout(orientation='vertical')
            player_layout.add_widget(player_image)
            player_layout.add_widget(skill)
            player_layout.add_widget(char_button)
            char_detail_layout.add_widget(player_layout)

        # add widget และทำการสร้างปุ่มมสำหรับกดเริ่มเกม
        self.layout1.add_widget(char_detail_layout)
        start_button = Button(text="Start Game", on_press=self.start_game,size_hint=(1, 0.25))
        self.layout1.add_widget(self.selected_char_label)
        self.layout1.add_widget(start_button)
        self.add_widget(self.layout1)
        self.player1_char = None
        self.player2_char = None

    # เป็นฟังก์ชั่นสำหรับการเลือกตัวละครและเก็บค่าเพื่อใช้ดำเนินเกมต่อในหน้าถัดไป พร้อมเปลี่ยนข้อความจาก Select Your Character แบบด้านบนเป็นชื่อ player1/2 และชื่อตัวละคร
    def select_character(self, char_name):
        if char_name not in self.selected_characters:
            if self.player1_char is None:
                self.player1_char = Char(char_name, 'Type', 100, 100)
                self.selected_characters.add(char_name)
                self.selected_char_label.text = f"Player 1 selected: {char_name}"
            elif self.player2_char is None:
                self.player2_char = Char(char_name, 'Type', 100, 100)
                self.selected_characters.add(char_name)
                self.selected_char_label.text = f"Player 2 selected: {char_name}"

    # ใช้สำหรับแสดงค่า skill ค่าการโจมตีที่อีกฝั่งได้รับและมานาที่ใช้
    def display_attack_skills(self, character):
        char_instance = Char(character, 'Type', 100, 100) 
        attack_skills = char_instance.skill_with_damage_and_mana()
        skills_text = "Attack Skills:\n"
        for skill, damage, mana in attack_skills:
            skills_text += f"{skill} - Damage: {damage}, Mana: {mana}\n"
        return skills_text
    
    # ฟังก์ชั่นที่เรียกเพื่อเปลี่ยนไปหน้าเล่นเกม
    def start_game(self, instance):
        if self.player1_char is not None and self.player2_char is not None:
            self.manager.get_screen("game").set_players(self.player1_char, self.player2_char)
            self.manager.current = "game"
        else:
            self.selected_char_label.text = "Both players must select a character."

# ใช้เพื่อแสดง ชื่อ รูปภาพ ของผู้เล่นสำหรับการเล่นเกม ผู้เล่นทั้งสองคนจะสลับกันกดปุ่มสกิล โดยเมื่อถึงตาของตัวเองจะมีสกิลทั้งสาม ค่าการโจมตี ค่ามานาที่ต้องใช้
class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.player1 = None
        self.player2 = None
        self.attack_levels = [1, 2, 3]
        self.current_player = None

        # กำหนด layout สำหรับที่ของ Widget
        self.layout = BoxLayout(orientation='vertical')
        player_info_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        # กำหนดตัวแปรสำหรับชื่อของตัวละคร (เรียกผา่นอีกฟังก์ชั่นเพราะเราจะใช้ตัวละคร 2 จาก 4) และ add widget
        self.player1_name_label = Label(text="", font_size=18, halign='center', valign='middle')
        self.player2_name_label = Label(text="", font_size=18, halign='center', valign='middle')
        player_info_layout.add_widget(self.player1_name_label)
        player_info_layout.add_widget(self.player2_name_label)
        self.layout.add_widget(player_info_layout)

        # กำหนดตัวแปรสำหรับรูปของตัวละคร (เรียกผา่นอีกฟังก์ชั่นเพราะเราจะใช้ตัวละคร 2 จาก 4) และ add widget
        player_images_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.4))
        self.player1_image = Image(source="", size_hint=(0.5, 1))
        self.player2_image = Image(source="", size_hint=(0.5, 1))
        player_images_layout.add_widget(self.player1_image)
        player_images_layout.add_widget(self.player2_image)
        self.layout.add_widget(player_images_layout)

        # กำหนดตัวแปรสำหรับสกิลของตัวละคร (เรียกผา่นอีกฟังก์ชั่นเพราะเราจะใช้ตัวละคร 2 จาก 4) และ add widget
        skills_and_attack_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.4))
        self.player1_skills_label = Label(text="", font_size=16)
        self.player2_skills_label = Label(text="", font_size=16)
        skills_and_attack_layout.add_widget(self.player1_skills_label)
        skills_and_attack_layout.add_widget(self.player2_skills_label)

        # การสร้างปุ่มสามปุ่มสำหรับสกิลทั้ง 3 สกิล และ add widget
        attack_buttons_layout = BoxLayout(orientation='vertical', size_hint=(0.2, 1))
        for level in self.attack_levels:
            button = Button(text=f"Attack {level}", on_press=self.attack, size_hint_y=None, height=50,background_color=(0.2, 0.7, 0.3, 1),color=(1, 1, 1, 1))  
            attack_buttons_layout.add_widget(button)

        # add widget
        skills_and_attack_layout.add_widget(attack_buttons_layout)
        self.layout.add_widget(skills_and_attack_layout)
        self.add_widget(self.layout)

    # มีการรับค่าจาก class เลือกตัวละครเพื่อกำหนดตัวละคร และทำการสุ่มตัวละครที่เล่นเกมก่อน พร้อมเรียกใช้ฟังก์ชั่นอัพเดตตัวละครปัจจุบันที่เล่นเกม 
    def set_players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = random.choice([player1, player2])
        self.update_player_info()
        self.skill_use()

    # แสดงผลชื่อตัวละคร เลือด มานาของผู้เล่นทั้งสองคน พร้อมรูปภาพ
    def update_player_info(self):
        self.player1_name_label.text = f"{self.player1.name}\nHealth: {self.player1.hp}\nMana: {self.player1.mana}"
        self.player2_name_label.text = f"{self.player2.name}\nHealth: {self.player2.hp}\nMana: {self.player2.mana}"
        self.player1_image.source = f"./image/{self.player1.name}.jpg"
        self.player2_image.source = f"./image/{self.player2.name}.jpg"

    # แสดงผลสกิลของผู้เล่นเทิร์นนั้น ๆ
    def skill_use(self):
        skills = self.current_player.skill_with_damage_and_mana()
        skills_text = "Attack Skills:\n"
        for skill, damage, mana in skills:
            skills_text += f"{skill} - Damage: {damage}, Mana: {mana}\n"
        if self.current_player == self.player1:
            self.player1_skills_label.text = skills_text
            self.player2_skills_label.text = ""
        else:
            self.player1_skills_label.text = ""
            self.player2_skills_label.text = skills_text

    # ใช้สำหรับการนำค่าโจมตีของฝั่งนึงไปลดค่าเลือดของอีกฝั่งโดยที่จะมีฝั่งตรงข้ามกับ current_player จะเป็น target
    def attack(self, instance):
        if self.current_player == self.player1:
            target = self.player2
        else:
            target = self.player1

        skill_number = int(instance.text.split()[-1])

        self.current_player.attack(target, skill_number)

        # หลังจบเทิร์นจะมีการเพิ่มมานาต่างกันตามสกิลที่ใช้ คือถ้าเลือกสกิลที่ค่าการโจมตีเยอะมานาจะเพิ่มน้อย
        if skill_number == 1:
            self.current_player.mana += 10
        elif skill_number == 2:
            self.current_player.mana += 5
        elif skill_number == 3:
            self.current_player.mana += 3

        self.current_player.mana = min(self.current_player.mana, 100)

        # เมื่อมีฝั่งนึงเลือด = 0 ให้เก็บชื่อผู้ชนะ และตัวละคร พร้อมเปลี่ยนหน้า ถ้าไม่ให้ดำเนินเกมต่อ
        if self.player1.hp <= 0 or self.player2.hp <= 0:
            winner = self.player2 if self.player1.hp <= 0 else self.player1
            winner_name = "Player 2" if self.player1.hp <= 0 else "Player 1"
            self.manager.get_screen("result").update_winner(winner.name)
            self.manager.current = "result"
        else:
            self.current_player = self.player2 if self.current_player == self.player1 else self.player1
            self.update_player_info()
            self.skill_use()

# ใช้เพื่อแสดงผลลัพธ์ของเกม คือเพลยเยอร์ 1/2 ชื่อผู้ชนะ และรูปภาพของผู้ชนะ
class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        # add widget ชื่อ player1/2 ชื่อตัวละคร และรูปภาพของผู้ชนะ
        self.layout = BoxLayout(orientation='vertical')
        self.winner_label = Label(text='', font_size=20)
        self.winner_image = Image(source='', size=(100, 100))
        self.layout.add_widget(self.winner_label)
        self.layout.add_widget(self.winner_image)
        self.add_widget(self.layout)

    # ฟังก์ชั่นที่ทำการอัพเดตชื่อของผู้ชนะจาก คลาส game_screen
    def update_winner(self, winner_name):
        self.winner_label.text = f"The winner is {winner_name}"
        self.winner_image.source = f'./image/{winner_name}.jpg'

# ใช้เพื่อการสร้างและทำงานของ kivy
class MainApp(App):
    def build(self):
        # ใช้เพื่อจัดการ screen ต่าง ๆ และแสดงผลทีละ 1 จอ
        screen_manager = ScreenManager()

        # กำหนดชื่อแทน screen ทุกอัน ใช้สำหรับการเปลี่ยนหน้าและ add widget
        intro_screen = Intro(name="intro")
        screen_manager.add_widget(intro_screen)

        character_selection_screen = CharacterSelectionScreen(name="character_selection")
        screen_manager.add_widget(character_selection_screen)

        game_screen = GameScreen(name="game")
        screen_manager.add_widget(game_screen)

        result_screen = ResultScreen(name="result")
        screen_manager.add_widget(result_screen)

        return screen_manager

# ใช้เพื่อการรันแอพเกม kivy ของเรา
if __name__ == '__main__':
    MainApp().run()