import Shadow_Knight


enemy_hp = 100

def BLACK_HEALTH_BAR():

    if enemy_hp >= 100:
        print(Shadow_Knight.Enemy_name, '🖤  HP  ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰', enemy_hp,'/','100\n')
    elif enemy_hp >= 70 and enemy_hp <= 99:
        print(Shadow_Knight.Enemy_name, '🖤  HP  ▰▰▰▰▰▰▰▰▰▰▰▰▱▱▱', enemy_hp,'/','100\n')
    elif enemy_hp >= 50 and enemy_hp < 70:
        print(Shadow_Knight.Enemy_name, '🖤  HP  ▰▰▰▰▰▰▰▰▰▱▱▱▱▱▱', enemy_hp,'/','100\n')
    elif enemy_hp >= 25 and enemy_hp < 50:
        print(Shadow_Knight.Enemy_name, '🖤  HP  ▰▰▰▰▱▱▱▱▱▱▱▱▱▱▱', enemy_hp,'/','100\n')
    elif enemy_hp <= 25:
        print(Shadow_Knight.Enemy_name, '🖤  HP  ▰▰▱▱▱▱▱▱▱▱▱▱▱▱▱', enemy_hp,'/','100\n')
    elif enemy_hp <= 0:
        print(Shadow_Knight.Enemy_name, '🖤  HP  ▱╱̸▱╲̸▱╱̸▱╲̸▱▱╱̸▱╲▱╱̸▱╲̸▱╱̸', enemy_hp,'/','100\n')