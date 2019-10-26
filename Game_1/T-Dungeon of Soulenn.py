from random import randint
from time import sleep
import random

# Versão do jogo para rodar em terminal

# ============== Primeira parte do jogo =================

print("= = = = = = = = = = = = = = = = = = = = = =  ")
print("= ======================================= =")
print("= ======== DUNGEON OF SOULENN =========== =")
print("= ======================================= =")
print("= = = = = = = = = = = = = = = = = = = = = = \n")

sleep(0.7)
print("Você acordou em um lugar misterioso ...\n")
for c in range(1, 4):
    sleep(0.7)
    print("...\n")
print("\"Há algo estranho por aqui\"\n")
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
Swd_arcana = {'nome': 'Espada Arcana', 'attack': 7, 'id': 0, 'qtd': 1, 'use': 0}
Swd_osso = {'nome': 'Osso', 'attack': 2, 'id': 0, 'qtd': 1, 'use': 0}

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
        print('{}.{} (x{})'.format(nm, m['nome'], m['qtd']), end='  ')
        nm += 1

    print('\n')


def item_select(it_sl1):  # Função que seleciona o item do inventário
    #    global Atk_Dif
    if it_sl1 == espadas:
        print('Qual espada deseja usar? ')
        it_id = 1
        for itt in it_sl1:  # Atribui pra cada item no inventário um id temporario Ex:'id':1,'id':2...
            itt['id'] = it_id  # Atribui o id para o item
            itt['use'] = 0  # Uso sempre será 0, sendo ativado na escolha( 1 por vez ativo)
            it_id += 1  # Id sempre será de 1 até o final da lista

        it_sl = int(input('> '))  # Recebe um número informado q corresponda ao número do item no inventário
        x = 0
        for itt in it_sl1:  # Para procurar nos itens se o número escolhido pelo jogador é igual a um id de um item
            if it_sl == itt['id']:
                x += 1  # Caso encontre um valor igual, atribuirá 1 para uma variavel x

        if x == 1:      # Se x for verdadeiro (há id igual ao numero inserido pelo usuario), ele mostrá o item correspondente
            it_sl += -1  # Como o número é um indice, tem q ser retirado 1 do valor
            print('Usando > {}'.format(it_sl1[it_sl]['nome']))   # Indice e chave [index][key]
            it_sl1[it_sl]['use'] = 1    # Variavel para denominar o item que está sendo usado(1 item só ativo)
        else:
            item_select(it_sl1)   # Caso o jogador insira um número fora do id, ele repete a função

    if it_sl1 == pocoes:
        print('Qual poção deseja usar? ')

#def item_select_pot():  # Função para selecionar poções



def move():  # Função para movimento baseado em floors, cada floor randomiza o algoritmo evento
    global dgwin
    if Dungeon1['floor'] >= 1:
        floor['floor'] += 1
        Dungeon1['floor'] -= 1
    else:
        print("=== Você venceu a Dungeon ===")
        dgwin = 1
    return floor, Dungeon1, dgwin


def monster():  # Função aleatória para escolher um inimigo e a chance de aparecer
    global enemy, m_s
    m_s = 0
    m_e = randint(0, 5)
    if m_e == 5:
        print("=== Um inimigo aparece sorrateiramente ===")
        m_s = randint(1, 2)
        if m_s == 1:
            enemy = skeleton
            print("=== Um Esqueleto com seu tremendo arco nórdico ===\n")
            game()
        if m_s == 2:
            enemy = slime
            print("=== Um pequeno Slime roxo ===\n")
            game()

    return m_s, enemy


def menu_items():
    itt2 = int(input("1.Espadas - 2.Poções > "))
    if itt2 != 1 and itt2 != 2:
        menu_items()
    if itt2 == 1:
        if len(espadas) == 0:
            print("\n===== Não há nada no inventário =====")
        else:
            item_show(espadas)
            item_select(espadas)
    if itt2 == 2:
        if len(pocoes) == 0:
            print("\n===== Não há nada no inventário =====")
        else:
            item_show(pocoes)
            item_select(pocoes)


def menu():  # Menu principal
    print('==========================================================')
    x = int(input("1.Inventário - 2.Status - 3.Andar > "))
    print('==========================================================')
    #  x=int(input("\n1.Inventário - 2.Status - 3.Andar - 4.Salvar > "))

    if x == 1:  # Inventário
        menu_items()

    if x == 2:  # Status
        print(
            " Vida: {}/{}\t\t\tAtaque: {}~{}".format(
                main_char['hp'], main_char['max_hp'], main_char['attack min'], main_char['attack max']))
        print(" Nível: {}\t\t\t\t\tXp: {}/{}".format(
            main_char['lv'], main_char['xp'], main_char['max_xp']))
        print(" Moedas: {}\t\t\t\t".format(main_char['coin']))

    if x == 3:  # Movimento de andar
        move()
        if dgwin != 1:
            print("\n=== Você deu um passo adentro da masmorra ===\n")
            monster()

    if x != 1 and x != 2 and x != 3:  # Caso não seja 1,2 e 3 repete a função
        menu()

    # if menu1 == 4:   função salvar ainda não implementada ;-;
    return x


def kill_event():  # Recompensa ao matar um inimigo
    print(
        '\n=== Você matou um monstro e ganhou {} moeda(s) + {} xp ==='.format(enemy['coin'], enemy['xp']))
    main_char['xp'] += enemy['xp']
    main_char['coin'] += enemy['coin']
    dif = main_char['xp'] - main_char['max_xp']
    if main_char['xp'] > main_char['max_xp']:
        main_char['lv'] += 1
        main_char['xp'] = dif
        print('\n=== Você subiu para o nível {} ==='.format(main_char['lv']))
    if main_char['xp'] == main_char['max_xp']:
        main_char['xp'] = 0
        main_char['lv'] += 1
        print('\n=== Você subiu para o nível {} ==='.format(main_char['lv']))


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
    print("\n>> Você causou {} de dano<<".format(-1 * random_attack()))
    if enemy['hp'] <= 0:
        print("> Vida do monstro:0 X-X <")
        e_dead = 1  # Var que declara o inimigo como morto
    else:
        print("> Vida do monstro:{}/{} <".format(enemy['hp'], enemy['max_hp']))
        sleep(0.5)
    return e_dead


def monstro_atacar():  # Função para o ataque do inimigo
    global dead
    print("\n## Você sofreu {} de dano ##".format(-1 * enemy_attack()))
    if main_char['hp'] <= 0:
        print('\n===== Você morreu =====')
        dead = 1  # Var que declara Sypher como morto
    else:
        print("# Vida Atual:{}/{} #\n".format(main_char['hp'], main_char['max_hp']))
    return dead


def game():  # Inicia uma batalha com um inimigo
    global e_dead
    e_dead = 0  # Reseta a morte do inimigo
    enemy['hp'] = enemy['max_hp']  # Reseta a vida do inimigo
    while enemy['hp'] > 0 and dead != 1:
        x = str(input("1.Atacar - 2.Usar item >"))

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
