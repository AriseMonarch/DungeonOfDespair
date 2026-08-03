import random
import PLAYER
import CRIT
import ENEMY_HEALTH_BAR
import time
import ENEMY_RNG



Enemy_name = '\nShadow Knight:'

def SHADOW_KNIGHT_AI():

    ENEMY_RNG.rng = random.randint(0, 2)
    CRIT.critical_hit = random.randint(7, 10)


    if ENEMY_RNG.rng == 0 and PLAYER.player_turn == 0:
        print('\nShadow knight Immenses A Glowing Green Light!🟢✨')
        time.sleep(1)
        ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp + 15
        PLAYER.player_turn = PLAYER.player_turn + 1
        if ENEMY_HEALTH_BAR.enemy_hp > 100:
            ENEMY_HEALTH_BAR.enemy_hp = 100
        
            
    
    elif ENEMY_RNG.rng == 0 and PLAYER.player_turn == 0 and CRIT.critical_hit == 10:
         print('\nShadow knight Used A Healing Potion?! 🧪🧪')
         time.sleep(1)
         ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp + 35
         PLAYER.player_turn = PLAYER.player_turn + 1
         if ENEMY_HEALTH_BAR.enemy_hp > 100:
              ENEMY_HEALTH_BAR.enemy_hp = 100
             



    elif ENEMY_RNG.rng == 1 and PLAYER.player_turn == 0 and PLAYER.defend == 1:
         print('\nShadown Knight Rushed Towards You Smashing You To The Ground 💢💢')
         time.sleep(1)
         PLAYER.player_hp = PLAYER.player_hp - 20
         PLAYER.player_turn = PLAYER.player_turn + 1
         
    elif ENEMY_RNG.rng == 1 and PLAYER.player_turn == 0:
         print('\nShadown Knight Rushed Towards You Smashing You To The Ground 💢💢')
         time.sleep(1)
         PLAYER.player_hp = PLAYER.player_hp - 40
         PLAYER.player_turn = PLAYER.player_turn + 1
         
    if PLAYER.player_turn == 0 and CRIT.critical_hit != 10 and PLAYER.defend == 1:
       print('\nShadow knight Is Preparing An Attack ⚔️')
       time.sleep(1)
       PLAYER.player_hp = PLAYER.player_hp - 2
       print('YOU GOT HIT BUT DEFENDED! 🛡️\n')
       PLAYER.player_turn = PLAYER.player_turn + 1
       PLAYER.defend = PLAYER.defend - 1

    elif CRIT.critical_hit == 10 and PLAYER.player_turn == 0 and PLAYER.defend == 1:
        time.sleep(1)
        PLAYER.player_hp = PLAYER.player_hp - 5
        print('YOU GOT HIT HARD BUT DEFENDED! 🛡️\n')
        PLAYER.defend = PLAYER.defend - 1
        PLAYER.player_turn = PLAYER.player_turn + 1

  
    elif PLAYER.player_turn == 0 and CRIT.critical_hit != 10:
       print('\nShadow knight Is Preparing An Attack ⚔️')
       time.sleep(1)
       PLAYER.player_hp = PLAYER.player_hp - 10
       print('YOU GOT HIT!\n')
       PLAYER.player_turn = PLAYER.player_turn + 1
  
    elif CRIT.critical_hit == 10 and PLAYER.player_turn == 0:
        print('\nShadow knight Is Preparing An Attack ⚔️')
        time.sleep(1)
        PLAYER.player_hp = PLAYER.player_hp - 20
        print('YOU GOT HIT HARD!\n')
        PLAYER.player_turn = PLAYER.player_turn + 1

    