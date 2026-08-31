import random

#ender of days is a boss

move = random.randint(0, 2)
def enemy_select():
 global rng, current_enemy, ENEMY_VARIETY
 ENEMY_VARIETY = ['Shadow_Knight', 'Goblin' ,'Executioner' ,'Eraser' ,'Motion' ,'Devider' , 'Terror', 'ENDER OF DAYS']

        
 rng = random.randint(0,len(ENEMY_VARIETY)- 1)
 current_enemy = ENEMY_VARIETY[rng]
 return(current_enemy)

