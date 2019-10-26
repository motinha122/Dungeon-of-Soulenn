from random import randint
from time import sleep
import random

# ============== Primeira parte do jogo =================

print("\33[1;33m= = = = = = = = = = = = = = = = = = = = = = = = = = ")
print("\33[1;33m= ====================================== =")
print("\33[1;33m= ========\33[1;36m DUNGEON OF SOULENN\33[1;33m ======== =")
print("\33[1;33m= ====================================== =")
print("\33[1;33m= = = = = = = = = = = = = = = = = = = = = = = = = =\n\33[m ")

sleep(0.7)
print("\33[1;35mVocê acordou em um lugar misterioso ...\33[m\n")
for c in range(1, 4):
    sleep(0.7)
    print("...\n")
print("\33[1;35m\"Há algo estranho por aqui\"\33[m\n")
sleep(0.5)
print("...\n")
sleep(0.5)
print("...")

# ============== Masmorra =================

Dungeon1 = {'floor': 20}  # Quantidade de pisos da masmorra

# ============== Sypher =================

main_char = {'max_hp': 100, 'hp': 100, 'attack min': 4, 'attack max': 8, 'xp': 0, 'lv': 1, 'max_xp': 20, 'coin': 10}  # Personagem principal(Sypher)

# ============== Lista de inimigos =================

slime = {'max_hp': 10, 'hp': 10, 'attack min': 2, 'attack max': 5, 'coin': 3, 'xp': 5, 'lv': 1, 'max_xp': 20}  # Slime

skeleton = {'max_hp': 20, 'hp': 20, 'attack min': 3, 'attack max': 7, 'coin': 5, 'xp': 10, 'lv': 1, 'max_xp': 40}  # Esqueleto

# ============== Lista de espadas =================

Swd_slime = {'nome': 'Espada de Slime', 'attack': 4, 'id': 0, 'qtd': 1, 'use': 0}
Swd_ferro = {'nome': 'Espada de Ferro', 'attack': 3, 'id': 0, 'qtd': 1, 'use': 0}
Swd_arcana = {'nome': '\33[1;31mEspada Arcana\33[m', 'attack': 7, 'id': 0, 'qtd': 1, 'use': 0}
Swd_osso = {'nome': '\33[1mOsso\33[m', 'attack': 2, 'id': 0, 'qtd': 1, 'use': 0}

# ============== Lista de poções =================

pot_life = {'nome': 'Poção de vida +25', 'id': 0, 'qtd': 1, 'use': 0}

# ============== Inventário do personagem  =================

espadas = [Swd_slime, Swd_ferro]  # Inventario para espadas

pocoes = [pot_life]  # Inventário para poções

# ================ Lista de Variáveis (algumas) =====================

monsters = [slime, skeleton]  # lista de monstros

enemy = random.choice(monsters)  # Inimigo aleatório

dead = 0  # Personagem vivo

e_dead = 0  # Inimigo vivo

floor = {'floor': 0}  # Casas ou pisos da masmorra

dgwin = 0  # Masmorra ainda não terminou

#def pot_delete(pot):
#    for p in pot:
#        if p['use'] == 1 and p['qtd'] == 1:
#            print('2')


def item_show(item):  # Função para mostrar os itens do inventário
    nm = 1
    for m in item:
        print('\33[1;36m{}.{} (x{})'.format(nm, m['nome'], m['qtd']), end='  ')
        nm += 1

    print('\n')


def item_select(it_sl1):  # Função que seleciona o item do inventário
    #    global Atk_Dif
    if it_sl1 == espadas:
        print('\33[1;36mQual espada deseja usar? \33[m')
        it_id = 1
        for itt in it_sl1:  # Atribui pra cada item no inventário um id temporario Ex:'id':1,'id':2...
            itt['id'] = it_id  # Atribui o id para o item
            itt['use'] = 0  # Uso sempre será 0, sendo ativado na escolha( 1 por vez ativo)
            it_id += 1  # Id sempre será de 1 até o final da lista

        it_sl = int(input('\33[1;36m> \33[m'))  # Recebe um número informado q corresponda ao número do item no inventário
        x = 0
        for itt in it_sl1:  # Para procurar nos itens se o número escolhido pelo jogador é igual a um id de um item
            if it_sl == itt['id']:
                x += 1  # Caso encontre um valor igual, atribuirá 1 para uma variavel x

        if x == 1:      # Se x for verdadeiro (há id igual ao numero inserido pelo usuario), ele mostrá o item correspondente
            it_sl += -1  # Como o número é um indice, tem q ser retirado 1 do valor
            print('\33[1;35mUsando > {}\33[m'.format(it_sl1[it_sl]['nome']))   # Indice e chave [index][key]
            it_sl1[it_sl]['use'] = 1    # Variavel para denominar o item que está sendo usado(1 item só ativo)
        else:
            item_select(it_sl1)   # Caso o jogador insira um número fora do id, ele repete a função

    if it_sl1 == pocoes:
        print('\33[1;36mQual poção deseja usar? \33[m')

#def item_select_pot():  # Função para selecionar poções



def move():  # Função para movimento baseado em floors, cada floor randomiza o algoritmo evento
    global dgwin
    if Dungeon1['floor'] >= 1:
        floor['floor'] += 1
        Dungeon1['floor'] -= 1
    else:
        print("\33[1;36m=== Você venceu a Dungeon ===\33[m")
        dgwin = 1
    return floor, Dungeon1, dgwin


def monster():  # Função aleatória para escolher um inimigo e a chance de aparecer
    global enemy, m_s
    m_s = 0
    m_e = randint(0, 5)
    if m_e == 5:
        print("\33[1;31m=== Um inimigo aparece sorrateiramente ===\33[m")
        m_s = randint(1, 2)
        if m_s == 1:
            enemy = skeleton
            print("\33[1;31m=== Um Esqueleto com seu tremendo arco nórdico ===\n\33[m")
            game()
        if m_s == 2:
            enemy = slime
            print("\33[1;31m=== Um pequeno Slime roxo ===\n\33[m")
            game()

    return m_s, enemy


def menu_items():
    itt2 = int(input("1.Espadas - 2.Poções > "))
    if itt2 != 1 and itt2 != 2:
        menu_items()
    if itt2 == 1:
        if len(espadas) == 0:
            print("\n\33[1;31m===== Não há nada no inventário =====\33[m")
        else:
            item_show(espadas)
            item_select(espadas)
    if itt2 == 2:
        if len(pocoes) == 0:
            print("\n\33[1;31m===== Não há nada no inventário =====\33[m")
        else:
            item_show(pocoes)
            item_select(pocoes)


def menu():  # Menu principal
    print('\33[1m==========================================================\33[m')
    x = int(input("\33[1m1.Inventário - 2.Status - 3.Andar > \33[m"))
    print('\33[1m==========================================================\33[m')
    #  x=int(input("\n\33[1m1.Inventário - 2.Status - 3.Andar - 4.Salvar > \33[m"))

    if x == 1:  # Inventário
        menu_items()

    if x == 2:  # Status
        print(
            "\33[1;36m Vida: \33[1;32m{}\33[m/\33[1;32m{}\33[m\t\t\t\33[1;36mAtaque: \33[1;32m{}\33[m~\33[1;32m{}\33[m".format(
                main_char['hp'], main_char['max_hp'], main_char['attack min'], main_char['attack max']))
        print("\33[1;36m Nível: \33[1;32m{}\33[m\t\t\t\t\33[1;36mXp: \33[1;32m{}\33[m/\33[1;32m{}\33[m".format(
            main_char['lv'], main_char['xp'], main_char['max_xp']))
        print("\33[1;36m Moedas: \33[1;32m{}\33[m\t\t\t\t".format(main_char['coin']))

    if x == 3:  # Movimento de andar
        move()
        if dgwin != 1:
            print("\n\33[1;36m=== Você deu um passo adentro da masmorra ===\n\33[m")
            monster()

    if x != 1 and x != 2 and x != 3:  # Caso não seja 1,2 e 3 repete a função
        menu()

    # if menu1 == 4:   função salvar ainda não implementada ;-;
    return x


def kill_event():  # Recompensa ao matar um inimigo
    print(
        '\n\33[1;34m=== Você matou um monstro e ganhou {} moeda(s) + {} xp ===\33[m'.format(enemy['coin'], enemy['xp']))
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


def enemy_attack():  # Função de dano de cada ataque do inimigo
    e_a = randint(-enemy['attack max'], -enemy['attack min'])
    main_char['hp'] += e_a
    return e_a


def random_attack():  # Função de dano de cada ataque de Sypher
    c_a = randint(-main_char['attack max'], -main_char['attack min'])
    enemy['hp'] += c_a
    return c_a


def atacar():  # Função ataque de Sypher
    global e_dead
    print("\n>> Você causou \33[1;32m{}\33[m de dano<<".format(-1 * random_attack()))
    if enemy['hp'] <= 0:
        print("\33[1;31m> Vida do monstro:0 X-X <\33[m")
        e_dead = 1  # Var que declara o inimigo como morto
    else:
        print("\33[1;31m> Vida do monstro:{}/{} <\33[m".format(enemy['hp'], enemy['max_hp']))
        sleep(0.5)
    return e_dead


def monstro_atacar():  # Função para o ataque do inimigo
    global dead
    print("\n## Você sofreu \33[1;31m{}\33[m de dano ##".format(-1 * enemy_attack()))
    if main_char['hp'] <= 0:
        print('\n\33[1;31m===== Você morreu =====\33[m')
        dead = 1  # Var que declara Sypher como morto
    else:
        print("\33[1;36m# Vida Atual:{}/{} #\33[m\n".format(main_char['hp'], main_char['max_hp']))
    return dead


def game():  # Inicia uma batalha com um inimigo
    global e_dead
    e_dead = 0  # Reseta a morte do inimigo
    enemy['hp'] = enemy['max_hp']  # Reseta a vida do inimigo
    while enemy['hp'] > 0 and dead != 1:
        x = str(input("\33[2;34m1.Atacar - 2.Usar item \33[m\33[1;37m>\33[m"))

        if x == '1':
            atacar()
            if e_dead == 1:
                kill_event()
                break
            else:
                monstro_atacar()

        if x == '2':
            menu_items()


# ============== Jogo =================

while dead != 1:  # Enquanto Sypher não morre, o jogo roda o menu
    menu()
