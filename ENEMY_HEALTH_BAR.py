import ENEMY_RNG

enemy_hp = (100/100) * 100
enemy_hp2 = (100/100) * 100
enemy_hp3 = (100/100) * 100

def BLACK_HEALTH_BAR():

    if enemy_hp >= 100:
        print(ENEMY_RNG.current_enemy, '🖤  HP  ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰', enemy_hp,'/','100\n')
    elif enemy_hp >= 70 and enemy_hp <= 99:
        print(ENEMY_RNG.current_enemy, '🖤  HP  ▰▰▰▰▰▰▰▰▰▰▰▰▱▱▱', enemy_hp,'/','100\n')
    elif enemy_hp >= 50 and enemy_hp < 70:
        print(ENEMY_RNG.current_enemy, '🖤  HP  ▰▰▰▰▰▰▰▰▰▱▱▱▱▱▱', enemy_hp,'/','100\n')
    elif enemy_hp >= 25 and enemy_hp < 50:
        print(ENEMY_RNG.current_enemy, '🖤  HP  ▰▰▰▰▱▱▱▱▱▱▱▱▱▱▱', enemy_hp,'/','100\n')
    elif enemy_hp <= 25:
        print(ENEMY_RNG.current_enemy, '🖤  HP  ▰▰▱▱▱▱▱▱▱▱▱▱▱▱▱', enemy_hp,'/','100\n')
    elif enemy_hp <= 0:
        print(ENEMY_RNG.current_enemy, '🖤  HP  ▱╱̸▱╲̸▱╱̸▱╲̸▱▱╱̸▱╲▱╱̸▱╲̸▱╱̸', enemy_hp,'/','100\n')

def enemy_health_bar2():

    if enemy_hp >= 100:
        print(ENEMY_RNG.current_enemy, '🖤  HP  ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰', enemy_hp2,'/','100\n')
    elif enemy_hp >= 70 and enemy_hp <= 99:
        print(ENEMY_RNG.current_enemy, '🖤  HP  ▰▰▰▰▰▰▰▰▰▰▰▰▱▱▱', enemy_hp2,'/','100\n')
    elif enemy_hp >= 50 and enemy_hp < 70:
        print(ENEMY_RNG.current_enemy, '🖤  HP  ▰▰▰▰▰▰▰▰▰▱▱▱▱▱▱', enemy_hp2,'/','100\n')
    elif enemy_hp >= 25 and enemy_hp < 50:
        print(ENEMY_RNG.current_enemy, '🖤  HP  ▰▰▰▰▱▱▱▱▱▱▱▱▱▱▱', enemy_hp2,'/','100\n')
    elif enemy_hp <= 25:
        print(ENEMY_RNG.current_enemy, '🖤  HP  ▰▰▱▱▱▱▱▱▱▱▱▱▱▱▱', enemy_hp2,'/','100\n')
    elif enemy_hp <= 0:
        print(ENEMY_RNG.current_enemy, '🖤  HP  ▱╱̸▱╲̸▱╱̸▱╲̸▱▱╱̸▱╲▱╱̸▱╲̸▱╱̸', enemy_hp2,'/','100\n')

def enemy_health_bar3():

    if enemy_hp >= 100:
        print(ENEMY_RNG.current_enemy, '🖤  HP  ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰', enemy_hp3,'/','100\n')
    elif enemy_hp >= 70 and enemy_hp <= 99:
        print(ENEMY_RNG.current_enemy, '🖤  HP  ▰▰▰▰▰▰▰▰▰▰▰▰▱▱▱', enemy_hp3,'/','100\n')
    elif enemy_hp >= 50 and enemy_hp < 70:
        print(ENEMY_RNG.current_enemy, '🖤  HP  ▰▰▰▰▰▰▰▰▰▱▱▱▱▱▱', enemy_hp3,'/','100\n')
    elif enemy_hp >= 25 and enemy_hp < 50:
        print(ENEMY_RNG.current_enemy, '🖤  HP  ▰▰▰▰▱▱▱▱▱▱▱▱▱▱▱', enemy_hp3,'/','100\n')
    elif enemy_hp <= 25:
        print(ENEMY_RNG.current_enemy, '🖤  HP  ▰▰▱▱▱▱▱▱▱▱▱▱▱▱▱', enemy_hp3,'/','100\n')
    elif enemy_hp <= 0:
        print(ENEMY_RNG.current_enemy, '🖤  HP  ▱╱̸▱╲̸▱╱̸▱╲̸▱▱╱̸▱╲▱╱̸▱╲̸▱╱̸', enemy_hp3,'/','100\n')