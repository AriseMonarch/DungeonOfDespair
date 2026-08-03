import PLAYER

def XP_BAR():


    
 if PLAYER.xp_percentage >= 10:

    print('|-------------------|\n'
       '|═                  |'' ' f'{PLAYER.xp}/{PLAYER.Required_xp}' ' XP'
       '\n|-------------------|\n')

 elif PLAYER.xp_percentage >=20:

    print('|-------------------|\n'
       '|══                 |'' ' f'{PLAYER.xp}/{PLAYER.Required_xp}' ' XP'
       '\n|-------------------|\n')
    
 elif PLAYER.xp_percentage >= 25:

    print('|-------------------|\n'
       '|════               |'' ' f'{PLAYER.xp}/{PLAYER.Required_xp}' ' XP'
       '\n|-------------------|\n')
    
 elif PLAYER.xp_percentage >=30:

    print('|-------------------|\n'
       '|══════             |'' ' f'{PLAYER.xp}/{PLAYER.Required_xp}' ' XP'
       '\n|-------------------|\n')

 elif PLAYER.xp_percentage >= 40:

    print('|-------------------|\n'
       '|════════           |'' ' f'{PLAYER.xp}/{PLAYER.Required_xp}' ' XP'
       '\n|-------------------|\n')

 elif PLAYER.xp_percentage >= 50:

    print('|-------------------|\n'
       '|══════════         |'' ' f'{PLAYER.xp}/{PLAYER.Required_xp}' ' XP'
       '\n|-------------------|\n')

 elif PLAYER.xp_percentage >= 55:


    print('|-------------------|\n'
       '|════════════       |'' ' f'{PLAYER.xp}/{PLAYER.Required_xp}' ' XP'
       '\n|-------------------|\n')

 elif PLAYER.xp_percentage >= 60:

    print('|-------------------|\n'
       '|══════════════     |'' ' f'{PLAYER.xp}/{PLAYER.Required_xp}' ' XP'
       '\n|-------------------|\n')

 elif PLAYER.xp_percentage >= 70:

    print('|-------------------|\n'
       '|════════════════   |'' ' f'{PLAYER.xp}/{PLAYER.Required_xp}' ' XP'
       '\n|-------------------|\n')

 elif PLAYER.xp_percentage >= 90:


    print('|-------------------|\n'
       '|══════════════════ |'' '  f'{PLAYER.xp}/{PLAYER.Required_xp}' ' XP'
       '\n|-------------------|\n')
    
 elif PLAYER.xp_percentage >= 100:

    print('|-------------------|\n'
       '|═══════════════════|'' ' f'{PLAYER.xp}/{PLAYER.Required_xp}' ' XP'
       '\n|-------------------|\n')

 if PLAYER.xp == 0:

    print('|═ ═ ═ ═ ═ ═ ═ ═ ═ ═|\n'
      '|                   ''|'' ' f'{PLAYER.xp}/{PLAYER.Required_xp}' ' XP'
      '\n|═ ═ ═ ═ ═ ═ ═ ═ ═ ═|\n')

 if PLAYER.xp_percentage >= 100:
    PLAYER.level = PLAYER.level + 1