class Char:
  def __init__(self,name,type,mana,hp) :
    self.name = name
    self.typeforchar = type
    self.mana = mana
    self.hp = hp
    
  def get_mana(self):
    return self.mana

  def get_hp(self):
    return self.hp
    
  def print(self):
    print("Name:",self.name)
    print('Type:', self.typeforchar)
    print('Mana:', self.mana)
    print( 'HP:', self.hp)

  def skill_with_damage_and_mana(self): 
    characters = {
        'Karina': [('Skill 1',30 ,20), ('Skill 2',40,30), ('Skill 3',50,40)],
        'Winter': [('Skill 1',25,15), ('Skill 2',35,25), ('Skill 3',45,35)],
        'Giselle': [('Skill 1',35,25), ('Skill 2',45,35), ('Skill 3',55,45)],
        'Ningning': [('Skill 1',20,10), ('Skill 2',30,20), ('Skill 3',40,30)]
          }
    for skill, damage, mana in characters[self.name]:
      print(f"{skill} damage {damage} mana {mana}")
      
  def attack_1(self, player_1, player_2, player_1_attack, player_2_attack):
    if player_1 == Karina :
      if player_1_attack == 1 :
        player_2.hp -= 30
        player_1.mana -= 20
      elif player_1_attack == 2 :
        player_2.hp -= 40
        player_1.mana -= 30
      elif player_1_attack == 3 :
        player_2.hp -= 50
        player_1.mana -= 40
    elif player_1 == Winter :
      if player_1_attack == 1 :
        player_2.hp -= 25
        player_1.mana -= 15
      elif player_1_attack == 2 :
        player_2.hp -= 35
        player_1.mana -= 25
      elif player_1_attack == 3 :
        player_2.hp -= 45
        player_1.mana -= 35
    elif player_1 == Giselle :
      if player_1_attack == 1 :
        player_2.hp -= 35
        player_1.mana -= 25
      elif player_1_attack == 2 :
        player_2.hp -= 45
        player_1.mana -= 35
      elif player_1_attack == 3 :
        player_2.hp -= 55
        player_1.mana -= 45
    elif player_1 == Ningning :
      if player_1_attack == 1 :
        player_2.hp -= 20
        player_1.mana -= 10
      elif player_1_attack == 2 :
        player_2.hp -= 30
        player_1.mana -= 20
      elif player_1_attack == 3 :
        player_2.hp -= 40
        player_1.mana -= 30
    player_1.hp = max(player_1.hp, 0)
    player_1.mana = max(player_1.mana, 0)
    
  def attack_2(self,player_2, player_1, player_2_attack, player_1_attack):
    if player_2 == Karina :
      if player_2_attack == 1 :
        player_1.hp -= 30
        player_2.mana -= 20
      elif player_2_attack == 2 :
        player_1.hp -= 40
        player_2.mana -= 30
      elif player_2_attack == 3 :
        player_1.hp -= 50
        player_2.mana -= 40
    elif player_2 == Winter :
      if player_2_attack == 1 :
        player_1.hp -= 25
        player_2.mana -= 15
      elif player_2_attack == 2 :
        player_1.hp -= 35
        player_2.mana -= 25
      elif player_2_attack == 3 :
        player_1.hp -= 45
        player_2.mana -= 35
    elif player_2 == Giselle :
      if player_2_attack == 1 :
        player_1.hp -= 35
        player_2.mana -= 25
      elif player_2_attack == 2 :
        player_1.hp -= 45
        player_2.mana -= 35
      elif player_2_attack == 3 :
        player_1.hp -= 55
        player_2.mana -= 45
    elif player_2 == Ningning :
      if player_2_attack == 1 :
        player_1.hp -= 20
        player_2.mana -= 10
      elif player_2_attack == 2 :
        player_1.hp -= 30
        player_2.mana -= 20
      elif player_2_attack == 3 :
        player_1.hp -= 40
        player_2.mana -= 30
    player_2.hp = max(player_2.hp, 0)
    player_2.mana = max(player_2.mana, 0)
        
Karina = Char('Karina','Rocket puncher',100,100)
Winter = Char('Winter','armamenter',100,100)
Giselle = Char('Giselle','xenoglossy',100,100)
Ningning = Char('Ningning','xenoglossy',100,100)

print(10 * '*' + 'Welcome to fight with your ae-nermy' + 10 * '*')
print("\nThis game In this game you have to choose\nyour character and fight with your ae-nermy.\n\n1.Karina who got Rocket puncher\n2.Winter who got armamenter\n3.Giselle who got xenoglossy\n4.Ningning who got e.d. Hacker")

while True:
    to_know_info = input("\nWould you like to know their skill and mana stats?\nAns (Yes or No) : ")
    if to_know_info == 'Yes':
        to_know_info_char = input('\nWhose skill are you curious about? \nAns(Karina, Winter, Giselle, Ningning) : ')

        if to_know_info_char == 'Karina':
          print('')
          Karina.print()
          print(10*'*')
          Karina.skill_with_damage_and_mana()
          
        elif to_know_info_char == 'Winter':
          print('')
          Winter.print()
          print(10*'*')
          Winter.skill_with_damage_and_mana()
          
        elif to_know_info_char == 'Giselle':
          print('')
          Giselle.print()
          print(10*'*')
          Giselle.skill_with_damage_and_mana()
          
        elif to_know_info_char == 'Ningning':
          print('')
          Ningning.print()
          print(10*'*')
          Ningning.skill_with_damage_and_mana()
          
        else:
            print('You entered an incorrect player name.')

    elif to_know_info == 'No':
        print("\nYou'll definitely want to know about it later.")
        break
    
while True:
    tmi = input("\nWould you like to know about their skills (tmi)? \nAns (Yes or No) : ")

    if tmi == 'Yes':
        tmi_char = input('\nWhose skill are you curious about? \nAns(Karina, Winter, Giselle, Ningning) : ')

        if tmi_char == 'Karina':
            print("\nPlayer 1 - Rocket Puncher:\n")
            print("Skill 1: Power Slam")
            print("Description: Channels kinetic energy into a devastating ground pound, creating shockwaves that damage and knock back nearby enemies.")
            print("Skill 2: Meteor Strike")
            print("Description: Launches into the air and descends with incredible force, crashing down on a targeted enemy, causing a massive explosion on impact.")
            print("Skill 3: Rocket Barrage")
            print("Description: Unleashes a rapid flurry of rocket-powered punches, striking multiple enemies in quick succession with immense strength.")

        elif tmi_char == 'Winter':
            print("\nPlayer 2 - Armament:\n")
            print("Skill 1: Arsenal Overdrive")
            print("Description: Activates an enhanced combat mode, increasing attack speed and damage output for a short duration.")
            print("Skill 2: Shield Matrix")
            print("Description: Generates an impenetrable energy shield, providing temporary invulnerability against incoming attacks.")
            print("Skill 3: Weaponized Fury")
            print("Description: Unleashes a barrage of energy projectiles, obliterating enemies in a wide area of effect.")

        elif tmi_char == 'Giselle':
            print("\nPlayer 3 - Xenoglossy:\n")
            print("Skill 1: Linguistic Insight")
            print("Description: Harnesses ancient knowledge to gain insight into enemy weaknesses, revealing their vulnerabilities for a limited time.")
            print("Skill 2: Babel Blast")
            print("Description: Unleashes a powerful sonic blast that disorients and stuns enemies in its path, rendering them temporarily unable to attack or defend.")
            print("Skill 3: Polyglot Empowerment")
            print("Description: Enhances the player's physical and mental capabilities by tapping into the power of languages, increasing damage output and agility.")

        elif tmi_char == 'Ningning':
            print("\nPlayer 4 - E.D. Hacker:\n")
            print("Skill 1: Virus Surge")
            print("Description: Releases a digital virus that infects enemy systems, causing damage over time and reducing their accuracy.")
            print("Skill 2: Firewall Shield")
            print("Description: Creates a protective firewall barrier that blocks incoming attacks and reflects a portion of the damage back to the attacker.")
            print("Skill 3: Data Override")
            print("Description: Hacks into enemy machinery and overrides their control systems, temporarily turning them against their allies or disabling them completely.")

        else:
            print('You entered an incorrect player name.')

    elif tmi == 'No':
        print("\nYou'll definitely want to know about it later.")
        break

player_1 = input("Input character name for player 1 : ")
if player_1 == 'Karina' :
  player_1 = Karina
elif player_1 == 'Winter' :
  player_1 = Winter
elif player_1 == 'Giselle' :
  player_1 = Giselle
elif player_1 == 'Ningning' :
  player_1 = Ningning
  
player_2 = input("Input character name for player 2 : ")
if player_2 == 'Karina' :
  player_2 = Karina
elif player_2 == 'Winter' :
  player_2 = Winter
elif player_2 == 'Giselle' :
  player_2 = Giselle
elif player_2 == 'Ningning' :
  player_2 = Ningning

Round  = 1
while True :
  print()
  print('Round {}'.format(Round))
  print('-'*10)
  mana_value_1 = player_1.mana
  hp_value_1 = player_1.hp
  mana_value_2 = player_2.mana
  hp_value_2 = player_2.hp
  if mana_value_1 <= 0 or hp_value_1 <= 0 :
    print("{} won !!!".format(player_2.name))
    break
  elif mana_value_2 <= 0 or hp_value_2 <= 0 :
    print("{} won !!!".format(player_1.name))
    break
  else :
    player_1.print()
    print()
    player_1.skill_with_damage_and_mana()
    player_1_attack = int(input("Input your skill action (1 or 2 or 3) : "))
    print()
    
    player_2.print()
    print()
    player_2.skill_with_damage_and_mana()
    player_2_attack = int(input("Input your skill action (1 or 2 or 3) : "))
    
    player_1.attack_1(player_1, player_2, player_1_attack, player_2_attack)
    player_2.attack_2(player_2, player_1, player_2_attack, player_1_attack)
    print()
    
    player_1.print()
    print()
    player_2.print()
    
    print()
    print("Your mana increase 10")
    player_1.mana += 10
    player_2.mana += 10
    Round += 1
    print()