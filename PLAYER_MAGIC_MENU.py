import PLAYER
import Shadow_Knight
import time
import ENEMY_HEALTH_BAR

def magic():
    
    
    print('MAGIC MENU\n')
    print('Fireball.'," ", 'costs 40 (MP), DEALS 30 DMG' )
    print('Ice Shards.', 'costs 20 (MP), DEALS 15 DMG TO ALL ENEMIES')
    print('Demise.', " ", " ", 'costs 80 (MP), Places A Curse On The Enemy, DEALS 20 DMG EVERY TURN FOR 3 TURNS ')
    action = input('> \n')
  
    if action.lower() == 'fireball':
      print('\nYou Channeled The Power Of Fire!🔥')

      ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp - 30
      PLAYER.stamina = PLAYER.stamina - 20
      PLAYER.player_turn = PLAYER.player_turn - 1
      PLAYER.mana = PLAYER.mana - 40
      time.sleep(1)
    
    elif action.lower() == 'ice shards':
      print('\nYou Channeled The Power Of Frost!❄️')
      
      ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp - 15
      PLAYER.stamina = PLAYER.stamina - 20
      PLAYER.player_turn = PLAYER.player_turn - 1
      PLAYER.mana = PLAYER.mana - 20
      time.sleep(1)

    elif action.lower() == 'demise':
        print('\nYou Channeled The Power Of Doom!💀')
        PLAYER.stamina = PLAYER.stamina - 20
        PLAYER.mana = PLAYER.mana - 80
        PLAYER.Doom = PLAYER.Doom + 1
        PLAYER.player_turn = PLAYER.player_turn + 1
        time.sleep(1)

    if PLAYER.Doom > 3:
       PLAYER.Doom = 0
       return
        
    elif PLAYER.Doom >= 1:
        ENEMY_HEALTH_BAR.enemy_hp = ENEMY_HEALTH_BAR.enemy_hp - 20
        PLAYER.Doom = PLAYER.Doom + 1
        return 

    if PLAYER.stamina < 0:
        PLAYER.stamina = 0