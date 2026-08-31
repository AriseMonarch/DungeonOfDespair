import PLAYER
import CRITHEAL
import Shadow_Knight
import ENEMY_HEALTH_BAR

def heal():    

    if PLAYER.potions == 0:
        print ('no more potions remaining! 🧪🧪')
    elif PLAYER.potions > 0:

     PLAYER.player_hp = PLAYER.player_hp + 10
     PLAYER.player_turn = PLAYER.player_turn - 1
     print('YOU FEEL BETTER!\n')
     print('HEALED 10 HP!\n')
     PLAYER.potions = PLAYER.potions - 1
     print('Remaining Potions:', PLAYER.potions,'\n')   

#--------------------------STATUS EFFECTS---------------------------
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
#-------------------------------------------------------------------

def crit_heal():
    

    if PLAYER.potions == 0:
        print ('no more potions remaining! 🧪🧪')
        return 
    elif PLAYER.potions > 0:
     
     PLAYER.player_hp = PLAYER.player_hp + 25
     PLAYER.player_turn = PLAYER.player_turn - 1
     print('YOU FEEL HEALED TO THE BRIM!\n')
     print('RECOVERED 25 HP!\n')
     PLAYER.potions = PLAYER.potions - 1
     print('Remaining Potions:', PLAYER.potions,'\n')

#--------------------------STATUS EFFECTS---------------------------
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
#------------------------------------------------------------------