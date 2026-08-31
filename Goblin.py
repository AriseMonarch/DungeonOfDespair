import random
import PLAYER
import CRIT
import ENEMY_HEALTH_BAR
import time
import ENEMY_RNG
import PLAYER_HEALTH_BAR


Enemy_name = '\nGoblin:'

def Goblin():

    ENEMY_RNG.move = random.randint(0, 2)
    CRIT.critical_hit = random.randint(7, 10)


    if ENEMY_RNG.move == 0 and PLAYER.player_turn == 0:
        print('\nThe Goblin Tripped And Stabbed Itself?\n')
        time.sleep(1)
        ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp - 10
        PLAYER.player_turn = PLAYER.player_turn + 1
    
    elif ENEMY_RNG.move == 0 and PLAYER.player_turn == 0 and CRIT.critical_hit == 10:
         print('\nThe Goblin Forgot What It Was Doing?\n')
         time.sleep(1)
         print('\nIt Looked Confused\n')
         PLAYER.player_turn = PLAYER.player_turn + 1

    elif ENEMY_RNG.move == 1 and PLAYER.player_turn == 0 and PLAYER.defend == 1:
         print('\nThe Goblin Jumped Around Giggling\n')
         time.sleep(1)
         print('\nIts Movements Sped Up?!\n')
         PLAYER.player_turn = 0 
         
    elif ENEMY_RNG.move == 1 and PLAYER.player_turn == 0:
         print('\nThe Goblin Started Running And Slashed Furiously')
         time.sleep(1)
         print('\nIt Hit You Multiple time')
         time.sleep(0.5)
         PLAYER.player_hp = PLAYER.player_hp - 8
         print(PLAYER_HEALTH_BAR)
         time.sleep(0.5)
         PLAYER.player_hp = PLAYER.player_hp - 8
         print(PLAYER_HEALTH_BAR)
         PLAYER.player_turn = PLAYER.player_turn + 1
         
    if PLAYER.player_turn == 0 and CRIT.critical_hit != 10 and PLAYER.defend == 1:
       print('\nThe Goblin Tried To Stab You 🔪\n')
       time.sleep(1)
       print('\nDespite Its Speed You Managed To Parry It 🛡️\n')
       PLAYER.player_turn = PLAYER.player_turn + 1
       PLAYER.defend = PLAYER.defend - 1

    elif CRIT.critical_hit == 10 and PLAYER.player_turn == 0 and PLAYER.defend == 1:
        time.sleep(1)
        PLAYER.player_hp = PLAYER.player_hp - 5
        print('The Goblin Slashed At You But You Deflected!? 🛡️\n')
        PLAYER.defend = PLAYER.defend - 1
        PLAYER.player_turn = PLAYER.player_turn + 1

  
    elif PLAYER.player_turn == 0 and CRIT.critical_hit != 10:
       print('\nThe Goblin Slashed At You! ⚔️')
       time.sleep(1)
       PLAYER.player_hp = PLAYER.player_hp - 10
       print('YOU GOT HIT!\n')
       PLAYER.player_turn = PLAYER.player_turn + 1
  
    elif CRIT.critical_hit == 10 and PLAYER.player_turn == 0:
        print('\nThe Goblin Sneaked And Stabbed You 🔪')
        time.sleep(1)
        PLAYER.player_hp = PLAYER.player_hp - 20
        print('You Started Bleeding Heavily 🩸🩸\n')
        PLAYER.Bleed = PLAYER.Bleed + 1
        PLAYER.player_turn = PLAYER.player_turn + 1

    if PLAYER.Bleed >= 1:
        PLAYER.player_hp = PLAYER.player_hp - 5

    if PLAYER.Bleed > 3:
        PLAYER.Bleed = 0