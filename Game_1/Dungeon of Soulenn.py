from random import randint
from time import sleep
import random

print("\33[1;33m= = = = = = = = = = = = = = = = = = = = ")
print("\33[1;33m= =================================== =")
print("\33[1;33m= =======\33[1;36m DUNGEON OF SOULENN\33[1;33m ======== =")
print("\33[1;33m= =================================== =")
print("\33[1;33m= = = = = = = = = = = = = = = = = = = =\n\33[m ")

sleep(0.7)
print("\33[1;35mVocê acordou em um lugar misterioso ...\33[m\n")
for c in range(1,4):
    sleep(0.7)
    print("...\n")
print("\33[1;35m\"Há algo estranho por aqui\"\33[m\n")
sleep(0.5)
print("...\n")
sleep(0.5)
print("...")

Dungeon1 = {'floor':70} #Quantidade de pisos na masmorra

main_char ={'max_hp':100,'hp':100,'attack min':4,'attack max':8,'xp':0,'lv':1,'max_xp':20,'coin':10} #Personagem principal

slime = {'max_hp':10,'hp':10,'attack min':2,'attack max':5,'coin':3,'xp':5,'lv':1,'max_xp':20} #Slime

skeleton = {'max_hp':20,'hp':20,'attack min':3,'attack max':7,'coin':5,'xp':10,'lv':1,'max_xp':40} #Esqueleto

inventario = {'Poção de vida','Faca de manteiga'} #Inventário para guardar itens

monsters = [slime,skeleton]         #lista de monstros

enemy = random.choice(monsters)     #Inimigo aleatório

dead = 0    #Personagem vivo

e_dead = 0  #Inimigo vivo

floor = {'floor':0}

def item_show(item):    #Função para mostrar os itens do inventário
    print('\n')
    nm = 1
    for m in item:
        print('\33[1;36m{}.{}'.format(nm,m),end=' ')
        nm += 1
    print('\n')

def move():        #Função para movimento baseado em floors, cada floor randomiza o algoritmo evento
    if Dungeon1['floor']>=1:
        floor['floor']+=1
        Dungeon1['floor']-=1
    else:
        print("\33[1;36m=== Você venceu a Dungeon ===\33[m")
    return floor,Dungeon1

def monster():  #Função aleatória para escolher um inimigo e a chance de aparecer
    global enemy,m_s
    m_s = 0
    m_e = randint(0,5)
    if m_e == 5:
        print("\n\33[1;31m=== Um inimigo aparece sorrateiramente ===\33[m")
        m_s = randint(1,2)
        if m_s == 1:
            enemy = skeleton
            print("\33[1;31m=== Um Esqueleto com seu tremendo arco nórdico ===\n\33[m")
            game()
        if m_s == 2:
            enemy = slime
            print("\33[1;31m=== Um pequeno Slime roxo ===\n\33[m")
            game()

    return m_s,enemy


def menu():         #Menu principal
    global x
    x=int(input("\n\33[1m1.Inventário - 2.Status - 3.Andar > \33[m"))
  #  x=int(input("\n\33[1m1.Inventário - 2.Status - 3.Andar - 4.Salvar > \33[m"))

    if x == 1:  #Inventário
        item_show(inventario)
        print("\33[1m === Você possui {} moeda(s) ===\33[m".format(main_char['coin']))
        if len(inventario) == 0:
            print("\n\33[1;31m===== Não há nada no inventário =====\33[m")

    if x == 2:  #Status
        print("\n\33[1;36m Vida: {}\33[m".format(main_char['hp']))
        print("\33[1;36m Nível: {}  Xp: {} \n\33[m".format(main_char['lv'],main_char['xp']))

    if x == 3:  #Movimento de andar
        move()
        print("\n\33[1;36m=== Você deu um passo adentro da masmorra ===\33[m")
        monster()

    if x!= 1 and x!= 2 and x!= 3:   #Caso não seja 1,2 e 3 repete a função
        menu()

    #if menu1 == 4:   função salvar ainda não implementada ;-;
    return x

#def slime_attack():
#    s_a = randint(-slime['attack max'],-slime['attack min'])
#    main_char['hp'] += s_a
#    return s_a

def kill_event():       #Recompensa ao matar um inimigo
    global dif
    print('\n\33[1;34m=== Você matou um monstro e ganhou {} moeda(s) + {} xp ===\33[m'.format(enemy['coin'],enemy['xp']))
    main_char['xp'] += enemy['xp']
    main_char['coin'] += enemy['coin']
    dif = main_char['xp'] - main_char['max_xp']
    if main_char['xp'] > main_char['max_xp']:
        main_char['lv'] += 1
        main_char['xp'] = dif
        print('\n\33[1;34m=== Você subiu para o nível {} ===\33[m'.format(main_char['lv']))
    if main_char['xp'] == main_char['max_xp']:
        main_char['xp'] = 0
        main_char['lv'] += 1
        print('\n\33[1;34m=== Você subiu para o nível {} ===\33[m'.format(main_char['lv']))

def enemy_attack():         #Função de dano de cada ataque do inimigo
    e_a = randint(-enemy['attack max'],-enemy['attack min'])
    main_char['hp'] += e_a
    return e_a

def random_attack():        #Função de dano de cada ataque de Sypher
    c_a = randint(-main_char['attack max'],-main_char['attack min'])
    enemy['hp'] += c_a
    return c_a

#def use_items():
def atacar():           #Função ataque de Sypher
    global e_dead
    print("Dano causado:\33[1;32m{}\33[m".format(-1*random_attack()))
    if enemy['hp']<=0:
        print("\33[1;31m Vida do monstro:0 X-X \33[m")
        e_dead = 1      #Var que declara o inimigo como morto
    else:
        print("\33[1;31m Vida do monstro:{} \33[m".format(enemy['hp']))
        sleep(0.5)
    return e_dead

def monstro_atacar():       #Função para o ataque do inimigo
    global dead
    print("\nVocê sofreu \33[1;31m{}\33[m de dano".format(-1*enemy_attack()))
    if main_char['hp'] <= 0:
        print('\n\33[1;31m===== Você morreu =====\33[m')
        dead = 1       #Var que declara Sypher como morto
    else:
        print("\n\33[1;36m Vida Atual:{} \33[m".format(main_char['hp']))
    return dead

def game():            #Inicia uma batalha com um inimigo
    global e_dead
    e_dead =0           #Reseta a morte do inimigo
    enemy['hp'] = enemy['max_hp']       #Reseta a vida do inimigo
    while enemy['hp'] >0 and dead != 1:
        global x,c
        x=str(input("\33[2;34m1.Atacar - 2.Usar item \33[m\33[1;37m>\33[m"))
        print("\n")
        if x == '1':
            atacar()
            if e_dead == 1:
                kill_event()
                break
            else:
                monstro_atacar()

        if x == '2':
            if len(inventario) == 0:
                print("\n===== Não há nada no inventário =====\n")
            else:
                item_show(inventario)

#while dead !=1:
#    menu()
#    enemy['hp'] = enemy['max_hp']

while dead!=1:  #Enquanto Sypher não morre, o jogo roda o menu
    menu()


