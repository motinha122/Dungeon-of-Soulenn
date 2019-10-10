from random import randint
from time import sleep
import random

print("\33[1;33m==================================")
print("\33[1;33m=======\33[1;36m DUNGEON OF SOULENN\33[1;33m =======")
print("\33[1;33m==================================\n")
print("\33[m")

sleep(1)
print("Você acordou em um lugar misterioso...\n")
for c in range(1,5):
    sleep(1)
    print("...\n")
print("\33[1;35m*Paft*\33[m um bicho te ataca\n")
sleep(1)
print("...\n")
sleep(1)
print("...\n")

Dungeon1 = {'floor':70} #Quantidade de pisos na masmorra

main_char ={'max_hp':50,'hp':50,'attack min':2,'attack max':5,'defense':3,'xp':0,'lv':1,'max_xp':20,'coin':10} #Personagem principal

slime = {'max_hp':10,'hp':10,'attack min':2,'attack max':5,'coin':3,'xp':5,'lv':1,'max_xp':20} #Slime

skeleton = {'max_hp':20,'hp':20,'attack min':3,'attack max':7,'coin':5,'xp':10,'lv':1,'max_xp':40} #Esqueleto

inventario = {} #Inventário para guardar itens

monsters = [slime,skeleton]

enemy = random.choice(monsters)

dead = 0    #Personagem vivo

e_dead = 0  #Inimigo vivo

floor = {'floor':0}

def move():         #Função para movimento baseado em floors, cada floor randomiza o algoritmo evento
    if Dungeon1['floor']>=1:
        floor['floor']+=1
        Dungeon1['floor']-=1
    else:
        print("\33[1;36m=== Você venceu a Dungeon ===\33[m")
    return floor,Dungeon1

def monster():  #Função aleatória para gerar um inimigo
    global enemy
    m_s = 0
    m_e = randint(0,5)
    if m_e == 5:
        print("\33[1;31m=== Um inimigo aparece sorrateiramente ===\33[m")
        m_s = randint(1,2)
        if m_s == 1:
            enemy = skeleton
            print("\33[1;31m=== Um Esqueleto com seu tremendo arco nórdico ===\33[m")
            game()
        if m_s == 2:
            enemy = slime
            print("\33[1;31m=== Um pequeno Slime roxo ===\33[m")
            game()

    return m_s,enemy


def menu():
    global x
    x=int(input("\n\33[1m1.Inventário - 2.Status - 3.Andar - 4.Salvar > \33[m"))

    if x == 1:
        print("\n\33[1m === Você possui {} moeda(s) ===\33[m".format(main_char['coin']))
        if len(inventario) == 0:
            print("\n\33[1;31m===== Não há nada no inventário =====\33[m")

    if x == 2:
        print("\n\33[1;36m Vida: {}\33[m".format(main_char['hp']))
        print("\33[1;36m Nível: {}  Xp: {} \n\33[m".format(main_char['lv'],main_char['xp']))

    if x == 3:
        move()
        print("\n\33[1;36m=== Você deu um passo adentro da masmorra ===\33[m")
        monster()

    if x!= 1 and x!= 2 and x!= 3:
        menu()

    #if menu1 == 4:   função salvar ainda não implementada ;-;
    return x

#def slime_attack():
#    s_a = randint(-slime['attack max'],-slime['attack min'])
#    main_char['hp'] += s_a
#    return s_a

def kill_event():
    print('\n\33[1;34m=== Você matou um monstro e ganhou {} moeda(s) + {} xp ===\33[m'.format(enemy['coin'],enemy['xp']))
    main_char['xp'] += enemy['xp']
    main_char['coin'] += enemy['coin']
    if main_char['xp'] >= main_char['max_xp']:
        main_char['xp'] = 0
        main_char['lv'] += 1
        print('\n\33[1;34m=== Você subiu para o nível {} ===\33[m'.format(main_char['lv']))
        enemy['hp'] = enemy['max_hp']

def enemy_attack():
    e_a = randint(-enemy['attack max'],-enemy['attack min'])
    main_char['hp'] += e_a
    return e_a

def random_attack():
    c_a = randint(-main_char['attack max'],-main_char['attack min'])
    enemy['hp'] += c_a
    return c_a

#def use_items():
def atacar():
    global e_dead
    print("Dano causado:\33[1;32m{}\33[m".format(-1*random_attack()))
    if enemy['hp']<=0:
        print("\33[1;31m Vida do bicho:0 X-X \33[m")
        e_dead = 1
    else:
        print("\33[1;31m Vida do bicho:{} \33[m".format(enemy['hp']))
        sleep(0.5)
    return e_dead

def monstro_atacar():
    global dead
    print("\nVocê sofreu \33[1;31m{}\33[m de dano".format(-1*enemy_attack()))
    if main_char['hp'] <= 0:
        print('\n\33[1;31m===== Você morreu =====\33[m')
        dead = 1
    else:
        print("\n\33[1;36m Vida Atual:{} \33[m".format(main_char['hp']))
    return dead

def game():
    while enemy['hp'] >0 and dead != 1:
        global x
        x=str(input("\33[2;34m1.Atacar - 2.Usar item \33[m\33[1;37m>\33[m"))
        print('\n')

        if x == '1':
            atacar()
            if e_dead == 1:
                kill_event()
            else:
                monstro_atacar()

        if x == '2':
            if len(inventario) == 0:
                print("\n===== Não há nada no inventário =====\n")
            else:
                print("potato")


while enemy['hp'] > 0:
#    select_act()
    x=str(input("\33[2;34m1.Atacar - 2.Usar item \33[m\33[1;37m>\33[m"))
    print('\n')
    if x == '1':
        print("Dano causado:\33[1;32m{}\33[m".format(-1*random_attack()))
        if enemy['hp']<=0:
            print("\33[1;31m Vida do bicho:0 X-X \33[m")
        else:
            print("\33[1;31m Vida do bicho:{} \33[m".format(enemy['hp']))
            sleep(0.5)
            print("\nVocê sofreu \33[1;31m{}\33[m de dano".format(-1*enemy_attack()))
            print("\n\33[1;36m Vida Atual:{} \33[m".format(main_char['hp']))

    if x == '2':
        if len(inventario) == 0:
            print("\n===== Não há nada no inventário =====\n")
        else:
            print("potato")

    if main_char['hp'] <= 0:
        print('\n\33[1;31m===== Você morreu =====\33[m')
        break
    if enemy['hp'] <= 0:
        print('\n\33[1;34m=== Você matou um monstro e ganhou {} moeda(s) + {} xp ===\33[m'.format(enemy['coin'],enemy['xp']))
        main_char['coin'] += enemy['coin']
        main_char['xp'] += enemy['xp']
        if main_char['xp'] >= main_char['max_xp']:
            main_char['xp'] = 0
            main_char['lv'] += 1
            print('\n\33[1;34m=== Você subiu para o nível {} ===\33[m'.format(main_char['lv']))
        enemy['hp'] = enemy['max_hp']
        break
    #slime

while dead !=1:
    menu()
