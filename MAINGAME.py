import random
import PLAYER_ATK
import PLAYER_HEALTH_BAR
import PLAYER
import Shadow_Knight
import PLAYER_STAMINA_BAR 
import PLAYER_HEAL
import PLAYER_MP_BAR
import CRIT
import CRITHEAL
import PLAYER_MAGIC_MENU
import PLAYER_Defend
import CLEAR_SCREEN
import XP_BAR
import ENEMY_HEALTH_BAR
import ENEMY_RNG

print('welcome to terminal RPG\n')

print('stage 1: Shadow knight')


print('\nEnemy is approaching\n')
 
print('press enter to continue\n')

while True:

 CRIT.critical_hit = random.randint(7, 10)
 CRITHEAL.critical_heal = random.randint(7, 10)

 ENEMY_HEALTH_BAR.BLACK_HEALTH_BAR()

 print('Command Menu\n')

 print('attack.')
 print('heal.')
 print('magic.')
 print('defend.\n')
 XP_BAR.XP_BAR()
 PLAYER_HEALTH_BAR.player_health_bar()
 PLAYER_MP_BAR.SHOW_MP()
 PLAYER_STAMINA_BAR.show_stamina()
 action = input('> \n')
 CLEAR_SCREEN.CLEAR()
 ENEMY_RNG.rng = random.randint(0, 2)

 if PLAYER.player_turn == 1:

  #Attacking
  
  if action.lower() == 'attack' and CRIT.critical_hit != 10 and PLAYER.stamina <=0:
      print('Your Body Felt Heavy\n')
      print('⚡ STAMINA [░░░░░░░░░░]')
      PLAYER.stamina = PLAYER.stamina + 10
      PLAYER.player_turn = PLAYER.player_turn - 1
      
  elif action.lower() == 'attack' and CRIT.critical_hit != 10:
     PLAYER_ATK.attacking()
    
 
 #critical attack
  
  elif action.lower() == 'attack' and CRIT.critical_hit == 10 and PLAYER.stamina <= 0:
      print('Your Body Felt Heavy\n')
      print('⚡ STAMINA [░░░░░░░░░░]')
      PLAYER.stamina = PLAYER.stamina + 10
      PLAYER.player_turn = PLAYER.player_turn - 1

  elif action.lower() == 'attack' and CRIT.critical_hit == 10:
      PLAYER_ATK.critical_atk()
 
  #Healing

  elif action.lower() == 'heal' and CRITHEAL.critical_heal != 10 and PLAYER.stamina <= 0:
      print('Your Body Felt Heavy\n')
      print('⚡ STAMINA [░░░░░░░░░░]')
      PLAYER.stamina = PLAYER.stamina + 10
      PLAYER.player_turn = PLAYER.player_turn - 1
      

  elif action.lower() == 'heal' and CRITHEAL.critical_heal != 10:

      PLAYER_HEAL.heal()

 #critical heal

  elif action.lower() == 'heal' and CRITHEAL.critical_heal == 10 and PLAYER.stamina <= 0:
      print('Your Body Felt Heavy And Could Not Heal\n')
      print('⚡ STAMINA [░░░░░░░░░░]')
      PLAYER.stamina = PLAYER.stamina + 10
      PLAYER.player_turn = PLAYER.player_turn - 1

  elif action.lower() == 'heal' and CRITHEAL.critical_heal == 10:

      PLAYER_HEAL.crit_heal()
      
 #defend

  elif action.lower() == 'defend':

      PLAYER_Defend.DEFEND()
    
 #spells

  elif  action.lower() == 'magic':
      PLAYER_MAGIC_MENU.magic()

 #if you defeat the enemy this is what it will print and end the game

  if ENEMY_HEALTH_BAR.enemy_hp <= 0:
       PLAYER.xp = PLAYER.xp + 75
       print('\nYOU WON\n')
       XP_BAR.XP_BAR()
       break
      
  Shadow_Knight.SHADOW_KNIGHT_AI()

#you really do not need an explanation for that

  if PLAYER.player_hp <= 0:
      print('YOU DIED!')
      break
  
  
    
