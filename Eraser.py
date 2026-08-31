import random
import PLAYER
import CRIT
import ENEMY_HEALTH_BAR
import time
import ENEMY_RNG
import PLAYER_HEALTH_BAR


Enemy_name = '\nEraser:'

def Executioner():

    ENEMY_RNG.move = random.randint(0, 2)
    CRIT.critical_hit = random.randint(7, 10)


    if ENEMY_RNG.move == 0 and PLAYER.player_turn == 0:
        print('\nThe Eraser Erased Your Combat IQ\n')
        time.sleep(1)
        PLAYER.player_hp = PLAYER.player_hp - 10
        PLAYER.player_turn = PLAYER.player_turn + 1
    
    elif ENEMY_RNG.move == 0 and PLAYER.player_turn == 0 and CRIT.critical_hit == 10:
         print('\nThe Eraser Erased Your Thoughts\n')
         time.sleep(1)
         PLAYER.player_turn = 0

    elif ENEMY_RNG.move == 1 and PLAYER.player_turn == 0 and PLAYER.defend == 1:
         print('\nThe Eraser Flew And Bumped Its Head In The Ceiling\n')
         time.sleep(1)
         ENEMY_HEALTH_BAR.enemy_hp - 2
         time.sleep(1)
         print('It Looked Confused So It Ate Itself Too')
         ENEMY_HEALTH_BAR.enemy_hp = 10
         PLAYER.player_turn = PLAYER.player_turn + 1 
         
    if PLAYER.player_turn == 0 and CRIT.critical_hit != 10 and PLAYER.defend == 1:
       print('\nThe Eraser Bobbed Its Head Everywhere At The Same Time?!🙂‍↔️\n')
       time.sleep(1)
       PLAYER.player_turn = PLAYER.player_turn + 1
       PLAYER.defend = PLAYER.defend - 1

    elif CRIT.critical_hit == 10 and PLAYER.player_turn == 0 and PLAYER.defend == 1:
       print('\nThe Eraser Bobbed Its Head Everywhere At The Same Time?!🙂‍↔️\n')
       time.sleep(1)
       PLAYER.player_turn = PLAYER.player_turn + 1
       PLAYER.defend = PLAYER.defend - 1

  
    elif PLAYER.player_hp <= 10:
       print('\nThe Eraser Hugged You\n')
       time.sleep(1)
       print('\nYou Hugged It Back\n')
       PLAYER.player_turn = PLAYER.player_turn + 1
  
    elif CRIT.critical_hit == 10 and PLAYER.player_turn == 0:
        print('\nThe Eraser Said T&YBNUYg678hmcs90q8jdo-+')
        time.sleep(1)
        print('You Said....Thanks?\n')
        time.sleep(1)
        PLAYER.player_turn = PLAYER.player_turn + 1

    