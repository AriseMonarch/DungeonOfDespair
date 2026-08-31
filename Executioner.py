import random
import PLAYER
import CRIT
import ENEMY_HEALTH_BAR
import time
import ENEMY_RNG
import PLAYER_HEALTH_BAR


Enemy_name = '\nExecutioner:'

def Executioner():

    ENEMY_RNG.move = random.randint(0, 2)
    CRIT.critical_hit = random.randint(7, 10)


    if ENEMY_RNG.move == 0 and PLAYER.player_turn == 0:
        print('\nThe Executioner Threw His Axe And Cut Your Leg Tendon 🩸🩸\n')
        time.sleep(1)
        PLAYER.player_hp = PLAYER.player_hp - 10
        PLAYER.Bleed = PLAYER.Bleed + 1
        PLAYER.player_turn = PLAYER.player_turn + 1
    
    elif ENEMY_RNG.move == 0 and PLAYER.player_turn == 0 and CRIT.critical_hit == 10:
         print('\nThe Executioner Grabbed You And Forced His Axe In Your Abdoment\n')
         time.sleep(1)
         PLAYER.player_hp = PLAYER.player_hp - 20
         PLAYER.Bleed = PLAYER.Bleed + 1
         time.sleep(1)
         print('\nYou Pushed Him Off\n')
         PLAYER.player_turn = PLAYER.player_turn + 1

    elif ENEMY_RNG.move == 1 and PLAYER.player_turn == 0 and PLAYER.defend == 1:
         print('\nThe Executioner Took Off His Mask?\n')
         time.sleep(1)
         print('\nYou Looked At His Face\n')
         time.sleep(1)
         print('\nYou Vommit🤮 Your Movements Slowed Down\n')
         PLAYER.slow = PLAYER.slow + 1
         PLAYER.player_turn = PLAYER.player_turn + 1 
         
    if PLAYER.player_turn == 0 and CRIT.critical_hit != 10 and PLAYER.defend == 1:
       print('\nThe Executioner Attacked You And Broke Your Shield?! 🔪\n')
       time.sleep(1)
       print('\nYou Managed To Get Out Without A Scratch, Your shield? Not So Much\n')
       PLAYER.player_turn = PLAYER.player_turn + 1
       PLAYER.defend = PLAYER.defend - 1

    elif CRIT.critical_hit == 10 and PLAYER.player_turn == 0 and PLAYER.defend == 1:
        time.sleep(1)
        print('The Executioner Threw His Spinning Axe At You But You Raised Your Hands!? 🛡️\n')
        time.sleep(0.5)
        print(PLAYER_HEALTH_BAR())
        PLAYER.player_hp = PLAYER.player_hp - 4
        print(PLAYER_HEALTH_BAR())
        time.sleep(0.3)
        PLAYER.player_hp = PLAYER.player_hp - 3
        print(PLAYER_HEALTH_BAR())
        time.sleep(0.3)
        PLAYER.player_hp = PLAYER.player_hp - 2
        print(PLAYER_HEALTH_BAR())
        time.sleep(0.3)
        PLAYER.player_hp = PLAYER.player_hp - 1
        print('You Looked At Your Forearms And They Are Badly Injured💪🩸')
        PLAYER.defend = PLAYER.defend - 1
        PLAYER.player_turn = PLAYER.player_turn + 1

  
    elif PLAYER.player_hp <= 10:
       print('\nThe Executioner Decapited You ⚔️\n')
       time.sleep(1)
       PLAYER.player_hp = PLAYER.player_hp - 100
       print('\nYou Saw Your Life Flash Before Your Eyes👀\n')
       PLAYER.player_turn = PLAYER.player_turn + 1
  
    elif CRIT.critical_hit == 10 and PLAYER.player_turn == 0:
        print('\nThe Executioner Planted His Axe Into The Ground And It Formed A Showave! 🪨')
        time.sleep(1)
        PLAYER.player_hp = PLAYER.player_hp - 15
        print('You Fell On Your Knees And Cracked Your Shins\n')
        PLAYER.player_turn = PLAYER.player_turn + 1

    if PLAYER.Bleed >= 1:
        PLAYER.player_hp = PLAYER.player_hp - 5

    if PLAYER.Bleed > 3:
        PLAYER.Bleed = 0