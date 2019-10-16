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

Dungeon1 = {'floor':20}     #Quantidade de pisos na masmorra

main_char ={'max_hp':100,'hp':100,'attack min':4,'attack max':8,'xp':0,'lv':1,'max_xp':20,'coin':10} #Personagem principal

slime = {'max_hp':10,'hp':10,'attack min':2,'attack max':5,'coin':3,'xp':5,'lv':1,'max_xp':20} #Slime

skeleton = {'max_hp':20,'hp':20,'attack min':3,'attack max':7,'coin':5,'xp':10,'lv':1,'max_xp':40} #Esqueleto

#inventario = {}  #Inventário para guardar itens

Swd_slime ={'nome':'Espada de Slime','attack':4,'id':0,'qtd':1}
Swd_ferro ={'nome':'Espada de Ferro','attack':3,'id':0,'qtd':1}
Swd_arcana ={'nome':'\33[1;31mEspada Arcana\33[m','attack':7,'id':0,'qtd':1}
Swd_osso ={'nome':'\33[1mOsso\33[m','attack':2,'id':0,'qtd':1}

espadas = [Swd_slime,Swd_ferro]     #Inventario para espadas

pocoes = {}      #Inventário para poções

monsters = [slime,skeleton]         #lista de monstros

enemy = random.choice(monsters)     #Inimigo aleatório

dead = 0    #Personagem vivo

e_dead = 0  #Inimigo vivo

floor = {'floor':0}

dgwin = 0

def item_show(item):    #Função para mostrar os itens do inventário
    nm = 1
    for m in item:
        print('\33[1;36m{}.{}'.format(nm,m['nome']),end=' ')
        nm += 1
    print('\n')

def item_select_sword(it_sl1):  #Função que seleciona o item do inventário
#    global Atk_Dif
    print('\33[1;36mQual item deseja usar? \33[m')
    it_id = 1
    for itt in it_sl1:          #Atribui pra cada item no inventário um id temporario Ex:'id':1,'id':2...
        itt['id']=it_id
        it_id+=1

    it_sl=int(input('\33[1;36m> \33[m'))    #Recebe um número informado q corresponda ao número do item no inventário
    it_sl+=-1                               #Como o número é um indice, tem q ser retirado 1 do valor
    print('\33[1;35mUsando > {}\33[m'.format(it_sl1[it_sl]['nome']))



#def item_select2():

def move():#Função para movimento baseado em floors, cada floor randomiza o algoritmo evento
    global dgwin
    if Dungeon1['floor']>=1:
        floor['floor']+=1
        Dungeon1['floor']-=1
    else:
        print("\33[1;36m=== Você venceu a Dungeon ===\33[m")
        dgwin=1
    return floor,Dungeon1,dgwin

def monster():  #Função aleatória para escolher um inimigo e a chance de aparecer
    global enemy,m_s
    m_s = 0
    m_e = randint(0,5)
    if m_e == 5:
        print("\33[1;31m=== Um inimigo aparece sorrateiramente ===\33[m")
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

def menu_items():
    itt2=int(input("1.Espadas - 2.Poções > "))
    if itt2 != 1 and itt2 != 2:
        menu_items()
    if itt2 == 1:
        if len(espadas) == 0:
            print("\33[1;31m===== Não há nada no inventário =====\33[m")
        else:
            print('\n')
            item_show(espadas)
            item_select_sword(espadas)
    if itt2 == 2:
        if len(pocoes) == 0:
            print("\33[1;31m===== Não há nada no inventário =====\33[m")
        else:
            print('\n')
            item_show(pocoes)
            print('\33[1;36mQual item deseja usar ou excluir? \33[m\n')


def menu():         #Menu principal
    print('\33[1m==========================================================\33[m')
    x=int(input("\33[1m1.Inventário - 2.Status - 3.Andar > \33[m"))
    print('\33[1m==========================================================\33[m')
  #  x=int(input("\n\33[1m1.Inventário - 2.Status - 3.Andar - 4.Salvar > \33[m"))

    if x == 1:  #Inventário
        menu_items()

    if x == 2:  #Status
        print("\33[1;36m Vida: \33[1;32m{}\33[m/\33[1;32m{}\33[m".format(main_char['hp'],main_char['max_hp']))
        print("\33[1;36m Nível: \33[1;32m{}\33[m\n \33[1;36mXp: \33[1;32m{}\33[m/\33[1;32m{}\33[m".format(main_char['lv'],main_char['xp'],main_char['max_xp']))
        print("\33[1;36m Ataque: \33[1;32m{}\33[m~\33[1;32m{}\33[m".format(main_char['attack min'],main_char['attack max']))
        print("\33[1;36m Moedas: \33[1;32m{}\33[m".format(main_char['coin']))

    if x == 3:#Movimento de andar
        move()
        if dgwin!=1:
            print("\n\33[1;36m=== Você deu um passo adentro da masmorra ===\n\33[m")
            monster()

    if x!= 1 and x!= 2 and x!= 3:   #Caso não seja 1,2 e 3 repete a função
        menu()

    #if menu1 == 4:   função salvar ainda não implementada ;-;
    return x

def kill_event():       #Recompensa ao matar um inimigo
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
    print("\n>> Você causou \33[1;32m{}\33[m de dano<<".format(-1*random_attack()))
    if enemy['hp']<=0:
        print("\33[1;31m> Vida do monstro:0 X-X <\33[m")
        e_dead = 1      #Var que declara o inimigo como morto
    else:
        print("\33[1;31m> Vida do monstro:{}/{} <\33[m".format(enemy['hp'],enemy['max_hp']))
        sleep(0.5)
    return e_dead

def monstro_atacar():       #Função para o ataque do inimigo
    global dead
    print("\n## Você sofreu \33[1;31m{}\33[m de dano ##".format(-1*enemy_attack()))
    if main_char['hp'] <= 0:
        print('\n\33[1;31m===== Você morreu =====\33[m')
        dead = 1       #Var que declara Sypher como morto
    else:
        print("\33[1;36m# Vida Atual:{}/{} #\33[m\n".format(main_char['hp'],main_char['max_hp']))
    return dead

def game():            #Inicia uma batalha com um inimigo
    global e_dead
    e_dead =0           #Reseta a morte do inimigo
    enemy['hp'] = enemy['max_hp']       #Reseta a vida do inimigo
    while enemy['hp'] >0 and dead != 1:
        global x,c
        x=str(input("\33[2;34m1.Atacar - 2.Usar item \33[m\33[1;37m>\33[m"))
        if x == '1':
            atacar()
            if e_dead == 1:
                kill_event()
                break
            else:
                monstro_atacar()

        if x == '2':
            menu_items()

while dead!=1:  #Enquanto Sypher não morre, o jogo roda o menu
    menu()


