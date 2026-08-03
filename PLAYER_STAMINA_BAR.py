import PLAYER




def show_stamina():
    
    if PLAYER.stamina > 100:
        PLAYER.stamina = 100

    if PLAYER.stamina == 100:
        print("⚡ STAMINA [██████████]", PLAYER.stamina, '/100')
    elif PLAYER.stamina >= 70:
        print("⚡ STAMINA [████████░░]" ,PLAYER.stamina ,'/100')
    elif PLAYER.stamina >= 40:
        print("⚡ STAMINA [██████░░░░]" ,PLAYER.stamina ,'/100')
    elif PLAYER.stamina >= 20:
        print("⚡ STAMINA [██░░░░░░░░]" ,PLAYER.stamina ,'/100')
    elif PLAYER.stamina > 0:
        print("⚡ STAMINA [░░░░░░░░░░]" ,PLAYER.stamina ,'/100')