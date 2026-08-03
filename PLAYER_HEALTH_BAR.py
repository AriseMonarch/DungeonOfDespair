import PLAYER

def player_health_bar():

    if PLAYER.player_hp == 100:
        print('🩸 HP  ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ ', PLAYER.player_hp, '/100')
    elif PLAYER.player_hp >= 70 and PLAYER.player_hp <= 99:
        print('🩸 HP  ▰▰▰▰▰▰▰▰▰▰▰▱▱▱▱ ', PLAYER.player_hp, '/100')
    elif PLAYER.player_hp >= 50 and PLAYER.player_hp < 70:
        print('🩸 HP  ▰▰▰▰▰▰▰▱▱▱▱▱▱▱▱ ', PLAYER.player_hp, '/100')
    elif PLAYER.player_hp >= 25 and PLAYER.player_hp < 50:
        print('🩸 HP  ▰▰▰▱▱▱▱▱▱▱▱▱▱▱▱ ', PLAYER.player_hp, '/100')
    elif PLAYER.player_hp <= 25:
        print('🩸 HP  ▰▱▱▱▱▱▱▱▱▱▱▱▱▱▱ ', PLAYER.player_hp, '/100')
    elif PLAYER.player_hp <= 0:
        print('🩸 HP ▱╱̸▱╲̸▱╱̸▱╲̸▱▱╱̸▱╲▱╱̸▱╲̸▱╱̸  ', PLAYER.player_hp, '/100')