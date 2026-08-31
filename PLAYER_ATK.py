import PLAYER
import CRIT
import random
import time
import ENEMY_HEALTH_BAR

CRIT.critical_hit = random.randint(7, 10)
action = input('> \n')

def attacking():

  print(ENEMY_HEALTH_BAR.BLACK_HEALTH_BAR(),'\n', ENEMY_HEALTH_BAR.enemy_health_bar2(), '\n', ENEMY_HEALTH_BAR.enemy_health_bar3())
  print('\nSelect Who To Attack.\n')

  if action == ('1'):
    print('YOU SWUNG YOUR SWORD AT THE ENEMY! 🗡️')
    ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp - 10
    PLAYER.player_turn = PLAYER.player_turn - 1
    PLAYER.stamina = PLAYER.stamina - 15
    time.sleep(1)
    
    if PLAYER.stamina < 0:
        PLAYER.stamina = 0

  elif action == ('2'):
    print('YOU SWUNG YOUR SWORD AT THE ENEMY! 🗡️')
    ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp2 - 10
    PLAYER.player_turn = PLAYER.player_turn - 1
    PLAYER.stamina = PLAYER.stamina - 15
    time.sleep(1)

    if PLAYER.stamina < 0:
        PLAYER.stamina = 0

  elif action == ('3'):
    print('YOU SWUNG YOUR SWORD AT THE ENEMY! 🗡️')
    ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp3 - 10
    PLAYER.player_turn = PLAYER.player_turn - 1
    PLAYER.stamina = PLAYER.stamina - 15
    time.sleep(1)


    if PLAYER.stamina < 0:
            PLAYER.stamina = 0
#-------------------------STATUS EFFECTS---------------------------------
    if PLAYER.Doom > 3:
        PLAYER.Doom = 0
        return
    
    elif PLAYER.Doom >= 1:
         ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp - 20
         PLAYER.Doom = PLAYER.Doom + 1
         return 

    if PLAYER.Bleed >= 1:
          PLAYER.player_hp = PLAYER.player_hp - 5
          PLAYER.Bleed = PLAYER.Bleed + 1
        
    elif PLAYER.Bleed > 3:
        PLAYER.Bleed = 0
        return

    if PLAYER.slow > 2:
        PLAYER.slow = 0
        
    elif PLAYER.slow == 1:
        PLAYER.stamina - 5
#-----------------------------------------------------------------------

def critical_atk():

  print(ENEMY_HEALTH_BAR.BLACK_HEALTH_BAR(),'\n', ENEMY_HEALTH_BAR.enemy_health_bar2(), '\n', ENEMY_HEALTH_BAR.enemy_health_bar3())
  print('\nSelect Who To Attack.\n')

  if action == ('1'):
    print('YOU SWUNG YOUR SWORD AT THE ENEMY WITH DEADLY PRECISION! 💥💥')
    ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp - 25
    PLAYER.player_turn = PLAYER.player_turn - 1
    PLAYER.stamina = PLAYER.stamina - 15
    time.sleep(1)

    if PLAYER.stamina < 0:
        PLAYER.stamina = 0

  if action == ('2'):
    print('YOU SWUNG YOUR SWORD AT THE ENEMY WITH DEADLY PRECISION! 💥💥')
    ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp - 25
    PLAYER.player_turn = PLAYER.player_turn - 1
    PLAYER.stamina = PLAYER.stamina - 15
    time.sleep(1)
     
    if PLAYER.stamina < 0:
        PLAYER.stamina = 0


  if action == ('3'):
    print('YOU SWUNG YOUR SWORD AT THE ENEMY WITH DEADLY PRECISION! 💥💥')
    ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp - 25
    PLAYER.player_turn = PLAYER.player_turn - 1
    PLAYER.stamina = PLAYER.stamina - 15
    time.sleep(1) 
 
    if PLAYER.stamina < 0:
        PLAYER.stamina = 0
#-------------------------STATUS EFFECTS---------------------------------
    if PLAYER.Doom > 3:
            PLAYER.Doom = 0
            return
    
    elif PLAYER.Doom >= 1:
         ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp - 20
         PLAYER.Doom = PLAYER.Doom + 1
         return 
    
    if PLAYER.Bleed >= 1:
         PLAYER.player_hp = PLAYER.player_hp - 5
         PLAYER.Bleed = PLAYER.Bleed + 1
    
    elif PLAYER.Bleed > 3:
        PLAYER.Bleed = 0
        return

    if PLAYER.slow > 2:
         PLAYER.slow = 0
    
    elif PLAYER.slow == 1:
         PLAYER.stamina - 5
    
#------------------------------------------------------------------------
