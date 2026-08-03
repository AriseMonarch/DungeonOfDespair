import PLAYER
import ENEMY_HEALTH_BAR
import time


def DEFEND():


    PLAYER.defend = 1
    PLAYER.player_turn = PLAYER.player_turn - 1
    PLAYER.stamina = PLAYER.stamina + 10
    print('YOU DEFEND 🛡️\n')
    time.sleep(1)



    if PLAYER.Doom > 3:
        PLAYER.Doom = 0
        return
    
    elif PLAYER.Doom >= 1:
        ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp - 20
        PLAYER.Doom = PLAYER.Doom + 1
        return

    