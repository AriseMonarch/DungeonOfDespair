import PLAYER


def SHOW_MP():

    if PLAYER.mana == 100:
        print('💧 MP  ⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢ ', PLAYER.mana,'/100')
    elif PLAYER.mana >= 70:
        print('💧 MP  ⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬡⬡⬡⬡ ', PLAYER.mana,'/100')
    elif PLAYER.mana >= 50:
        print('💧 MP  ⬢⬢⬢⬢⬢⬢⬢⬡⬡⬡⬡⬡⬡⬡ ', PLAYER.mana,'/100')
    elif PLAYER.mana >= 25:
        print('💧 MP  ⬢⬢⬢⬢⬡⬡⬡⬡⬡⬡⬡⬡⬡⬡ ', PLAYER.mana,'/100')
    elif PLAYER.mana >= 1:
        print('💧 MP  ⬢⬡⬡⬡⬡⬡⬡⬡⬡⬡⬡⬡⬡⬡ ', PLAYER.mana,'/100')
    else:
        print('💧 MP  ⬡⬡⬡⬡⬡⬡⬡⬡⬡⬡⬡⬡⬡⬡ ', PLAYER.mana,'/100')    
