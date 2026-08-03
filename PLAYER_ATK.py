import Shadow_Knight
import PLAYER
import CRIT
import random
import time
import ENEMY_HEALTH_BAR

CRIT.critical_hit = random.randint(7, 10)


def attacking():

    print('YOU SWUNG YOUR SWORD AT THE ENEMY! 🗡️')
    ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp - 10
    PLAYER.player_turn = PLAYER.player_turn - 1
    PLAYER.stamina = PLAYER.stamina - 15
    time.sleep(1)

    if PLAYER.stamina < 0:
        PLAYER.stamina = 0


    if PLAYER.Doom > 3:
        PLAYER.Doom = 0
        return
    
    elif PLAYER.Doom >= 1:
         ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp - 20
         PLAYER.Doom = PLAYER.Doom + 1
         return 

    
def critical_atk():

    print('YOU SWUNG YOUR SWORD AT THE ENEMY WITH DEADLY PRECISION! 💥💥')
    ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp - 25
    PLAYER.player_turn = PLAYER.player_turn - 1
    PLAYER.stamina = PLAYER.stamina - 15
    time.sleep(1)

    if PLAYER.stamina < 0:
        PLAYER.stamina = 0

    if PLAYER.Doom >= 1:
         ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp - 20
         PLAYER.Doom = PLAYER.Doom + 1
         return 