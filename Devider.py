import random
import PLAYER
import CRIT
import ENEMY_HEALTH_BAR
import time
import ENEMY_RNG
import PLAYER_HEALTH_BAR


Enemy_name = '\nDevider:'

def Devider():

    ENEMY_RNG.move = random.randint(0, 2)
    CRIT.critical_hit = random.randint(7, 10)


    if ENEMY_RNG.move == 0 and PLAYER.player_turn == 0:
        print('\nA Devider Devided Into Place\n')
        time.sleep(1)
        print('A Loud Buzz Echoed In Your Ears📣')
        time.sleep(1)
        print('You Felt Dizzy And Your Ears Popped')
        time.sleep(1)
        PLAYER.player_hp = PLAYER.player_hp - 5
        print('You Already Hate This Creature')
        PLAYER.player_turn = 0
    
    elif ENEMY_RNG.move == 0 and PLAYER.player_turn == 0 and CRIT.critical_hit == 10:
         print('\nA Devider Made A Screaching Sound That Shattered Your Nerves\n')
         time.sleep(1)
         print('\nYou Want To Punch Them In The Face, Despite Them Not Having One\n')
         time.sleep(1)
         PLAYER.player_hp = PLAYER.player_hp - 5
         PLAYER.player_turn = PLAYER.player_turn + 1

    elif ENEMY_RNG.move == 1 and PLAYER.player_turn == 0 and PLAYER.defend == 1:
         print('\nThe Deviders Surrounded You And Screamed In Unison\n')
         time.sleep(1)
         print('\nNow You Are Starting To Get Mad\n')
         time.sleep(1)
         PLAYER.player_hp = PLAYER.player_hp - 10
         PLAYER.player_turn = PLAYER.player_turn + 1
         
    elif ENEMY_RNG.move == 1 and PLAYER.player_turn == 0:
         print('\nThey Devided Into More And More\n')
         time.sleep(1)
         print('\nThe Room Is Filled With Deviders\n')
         time.sleep(0.5)
         print('\nYou Had No Time To React As They Started To Scream\n')
         time.sleep(1)
         print('\nThey Screamed Louder And Louder As You Felt Your Will To Live Slip Away\n')
         time.sleep(0.5)
         print('\nYou Pressed Your Own Sword Into Your Stomach\n')
         PLAYER.player_hp = PLAYER.player_hp - 8
         PLAYER.player_turn = PLAYER.player_turn + 1
         
    if PLAYER.player_turn == 0 and CRIT.critical_hit != 10 and PLAYER.defend == 1:
       print('\nThey Made Fun Of Your Pain\n')
       time.sleep(1)
       print('\nThey Screamed But Your Shield Reflected Their Echoes\n')
       time.sleep(1)
       ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp - 5
       ENEMY_HEALTH_BAR.enemy_hp2 = ENEMY_HEALTH_BAR.enemy_hp2 - 5
       ENEMY_HEALTH_BAR.enemy_hp3 = ENEMY_HEALTH_BAR.enemy_hp3 - 5
       PLAYER.player_turn = PLAYER.player_turn + 1
       PLAYER.defend = PLAYER.defend - 1

    elif CRIT.critical_hit == 10 and PLAYER.player_turn == 0 and PLAYER.defend == 1:
        time.sleep(1)
        print('\nThey Look Mad, their Nonexistant Faces Are twitching\n')
        PLAYER.defend = PLAYER.defend - 1
        PLAYER.player_turn = 0

  
    elif PLAYER.player_turn == 0 and CRIT.critical_hit != 10:
       print('\nThey Seem Sad? You Decided That It Is Best Not To Provoke Them\n')
       time.sleep(1)
       PLAYER.player_turn = PLAYER.player_turn + 0
  
    elif CRIT.critical_hit == 10 and PLAYER.player_turn == 0:
        print('\nThe Deviders Took Advantage Of You Being Sensitive To Noise\n')
        time.sleep(1)
        print('\nThey Echoed At The Silverware Around And Made A Screaching Sound\n')
        PLAYER.player_hp = PLAYER.player_hp - 20
        print('Your Ears Bleeded Heavily\n')
        PLAYER.Bleed = PLAYER.Bleed + 1
        PLAYER.player_turn = PLAYER.player_turn + 1