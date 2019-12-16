from random import randint
from time import sleep
import random

# ============== Primeira parte do jogo =================

print("\33[1m= = = = = = = = = = = = = = = = = = = = = = = = = =  =   ")
print("\33[1m= =================================== =")
print("\33[1m= ========\33[1;36m DUNGEON OF SOULENN\33[1m ========= =")
print("\33[1m= =================================== =")
print("\33[1m= = = = = = = = = = = = = = = = = = = = = = = = = =  =    \n\33[m ")
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

Dungeon1 = {'floor': 15}  # Quantidade de pisos da masmorra

# ============== Lista de espadas vendidas em lojas =================

Swd_ferro = {'nome': 'Espada de Ferro', 'attack': 2, 'id': 0, 'qtd': 1, 'use': 0, 'preço': 15}
Swd_bronze = {'nome': 'Espada de Bronze', 'attack': 3, 'id': 0, 'qtd': 1, 'use': 0, 'preço': 25}
Swd_prata = {'nome': 'Espada de Prata', 'attack': 5, 'id': 0, 'qtd': 1, 'use': 0, 'preço': 55}
Swd_ouro = {'nome': 'Espada de Ouro', 'attack': 8, 'id': 0, 'qtd': 1, 'use': 0, 'preço': 105}

# ============== Lista de espadas obtidas de monstros =================

Swd_slime = {'nome': 'Espada de Slime', 'attack': 2, 'id': 0, 'qtd': 1, 'use': 0, 'preço': 20}
Swd_fogo = {'nome': '\33[1;31mEspada de Fogo', 'attack': 7, 'id': 0, 'qtd': 1, 'use': 0, 'preço': 80}
Swd_arcana = {'nome': '\33[1;31mEspada Arcana', 'attack': 7, 'id': 0, 'qtd': 1, 'use': 0, 'preço': 100}
Swd_osso = {'nome': '\33[1mOsso', 'attack': 3, 'id': 0, 'qtd': 1, 'use': 0, 'preço': 35}

# ============== Lista de poções =================

pot_life = {'nome': 'Poção de vida +25', 'id': 0, 'qtd': 3, 'use': 0, 'preço': 15}

# ============== Cidades e Lojas =================

# --------- Akhato ----------

Akhato = {'floor': 0, 'nome': 'Akhato', 'max_floor': 10}  # Quantidade de pisos da primeira cidade

akh_swd = [Swd_ferro, Swd_bronze, Swd_prata, Swd_ouro]  # Lista de itens da loja de Akhato
akh_pot = [pot_life]

# ============== Sypher =================

sypher = {'max_hp': 100, 'hp': 100, 'attack min': 4, 'attack max': 8, 'xp': 0, 'lv': 1, 'max_xp': 20,
          'coin': 1000}  # Personagem principal(Sypher)

# ============== Lista de inimigos =================

slime = {'max_hp': 10, 'hp': 10, 'attack min': 2, 'attack max': 5, 'coin': 3, 'xp': 5, 'lv': 1, 'max_xp': 20,
         'loot': Swd_slime}  # Slime

skeleton = {'max_hp': 20, 'hp': 20, 'attack min': 3, 'attack max': 7, 'coin': 5, 'xp': 10, 'lv': 1, 'max_xp': 40,
            'loot': Swd_osso}  # Esqueleto

# ============== Inventário do personagem  =================

espadas = [Swd_fogo]  # Inventario para espadas

pocoes = [pot_life]  # Invetário para poções

# ================ Lista de Variáveis (algumas) =====================

monsters = [slime, skeleton]  # lista de monstros

enemy = random.choice(monsters)  # Inimigo aleatório

dead = 0  # Personagem vivo

e_dead = 0  # Inimigo vivo

dgwin = 0  # Masmorra ainda não terminou

dmg = 0  # Variavel para o dano da espada

cdfim = 0  # Cidade ainda não acabou


# ================ Lista de Funções =====================

def move_city(city):  # Função para movimento na cidade

    global cdfim

    if city['floor'] < city['max_floor']:
        city['floor'] += 1
    else:
        print("\33[1;36m=== Você saiu da cidade de {} ===\33[m".format(city['nome']))
        cdfim = 1

    return cdfim


def item_show(item):  # Função para mostrar os itens do inventário

    nm = 1
    for m in item:
        print('\33[1;36m{}.{} (x{})\33[m'.format(nm, m['nome'], m['qtd']), end='  ')
        nm += 1

    print('\n')


def item_select(inv):  # Função que seleciona o item do inventário

    global dmg

    if inv == espadas:

        print('\33[1;36mQual espada deseja usar? \33[m')

        it_id = 1
        for itt in inv:  # Atribui pra cada item no inventário um id temporario Ex:'id':1,'id':2...
            itt['id'] = it_id  # Atribui o id para o item
            itt['use'] = 0  # Uso sempre será 0, sendo ativado na escolha( 1 por vez ativo)
            it_id += 1  # Id sempre será de 1 até o final da lista0

        item = int(
            input('\33[1;36m> \33[m'))  # Recebe um número informado q corresponda ao número do item no inventário

        id_r = 0  # Variavel para indicar id verdadeiro ou não

        for itt in inv:  # Para procurar nos itens se o número escolhido pelo jogador é igual a um id de um item
            if item == itt['id']:
                id_r = 1  # Caso encontre um valor igual, atribuirá 1 para uma variavel x

        if id_r == 1:  # Se x for verdadeiro (há id igual ao numero inserido pelo usuario), ele mostrá o item correspondente
            item -= 1  # Como o número é um indice, tem q ser retirado 1 do valor
            print('\33[1;35mUsando > {}\33[m'.format(inv[item]['nome']))  # Indice e chave [index][key]
            dmg = inv[item]['attack']  # Variavel para receber o dano da espada
            inv[item]['use'] = 1  # Variavel para denominar o item que está sendo usado(1 item só ativo)

        else:
            item_select(inv)

    if inv == pocoes:  # Poções

        print('\33[1;36mQual poção deseja usar? \33[m')

        it_id = 1
        for itt in inv:  # Atribui pra cada item no inventário um id temporario Ex:'id':1,'id':2...
            itt['id'] = it_id  # Atribui o id para o item
            itt['use'] = 0  # Uso sempre será 0, sendo ativado na escolha( 1 por vez ativo)
            it_id += 1  # Id sempre será de 1 até o final da lista

        item = int(
            input('\33[1;36m> \33[m'))  # Recebe um número informado q corresponda ao número do item no inventário

        id_r = 0  # Variavel para indicar id verdadeiro ou não

        for itt in inv:  # Para procurar nos itens se o número escolhido pelo jogador é igual a um id de um item
            if item == itt['id']:
                id_r = 1  # Caso encontre um valor igual, atribuirá 1 para uma variavel xd

        if id_r == 1:  # Se x for verdadeiro (há id igual ao numero inserido pelo usuario), ele mostrá o item correspondente
            item -= 1  # Como o número é um indice, tem q ser retirado 1 do valor

            if inv[item]['nome'] == 'Poção de vida +25':  # Seleciona poção de vida
                if sypher['hp'] < sypher['max_hp']:  # Caso a vida atual seja menor que a maxima
                    sypher['hp'] += 25  # Cura o Sypher em 25 pontos
                    if sypher['hp'] > sypher['max_hp']:  # Em alguns casos a vida atual pode ser maior q a maxima
                        sypher['hp'] = sypher['max_hp']  # Mantem como vida maxima para não ultrapassar o valor
                    print('\33[1;35mUsou > {}\33[m'.format(inv[item]['nome']))  # Indice e chave [index][key]
                    inv[item]['qtd'] -= 1  # Retira 1 da quantidade da poção que foi usada
                    if inv[item]['qtd'] == 0:  # Caso a quantidade da poção seja 1 ou menor
                        inv.remove(inv[item])  # Remove a poção do inventário
                else:
                    print(
                        '\n\33[1;31mVida Máxima,poção não foi usada\33[m')  # Caso a vida já esteja maximo, a poção não é usada


        else:
            item_select(inv)


# === Funções Loja ===

def c_item_show(item):  # Função para mostrar os itens da Loja

    nm = 1
    for m in item:
        print('\n{}\33[1;34m.{}\33[m {} moedas'.format(nm, m['nome'], m['preço']), end='  ')
        nm += 1

    print('\n')


def v_item_show(item):  # Função para mostrar os itens da Loja

    nm = 1
    for m in item:
        print('\n{}\33[1;34m.{}\33[m {} moedas(x{})'.format(nm, m['nome'], m['preço'], m['qtd']), end='  ')
        nm += 1

    print('\n')


def v_item_select(inv, city, city_swd, city_pot):  # Função que seleciona o item do inventário

    if inv == espadas:
        print('\33[1;36mQual espada deseja vender? \33[m')
    if inv == pocoes:
        print('\33[1;36mQual poção deseja vender? \33[m')

    it_id = 1
    for itt in inv:  # Atribui pra cada item no inventário um id temporario Ex:'id':1,'id':2...
        itt['id'] = it_id  # Atribui o id para o item
        it_id += 1  # Id sempre será de 1 até o final da lista0

    item = int(input('\33[1;36m> \33[m'))  # Recebe um número informado q corresponda ao número do item no inventário

    id_r = 0  # Variavel para indicar id verdadeiro ou não

    for itt in inv:  # Para procurar nos itens se o número escolhido pelo jogador é igual a um id de um item
        if item == itt['id']:
            id_r = 1  # Caso encontre um valor igual, atribuirá 1 para uma variavel x

    if id_r == 1:  # Se x for verdadeiro (há id igual ao numero inserido pelo usuario), ele mostrá o item correspondente
        item -= 1  # Como o número é um indice, tem q ser retirado 1 do valor
        print(('\33[1;35mDeseja vender > {}\33[m'.format(inv[item]['nome'])))
        z = int(input('\33[1;35m1.Sim    2.Não >\33[m'))  # Indice e chave [index][key]
        if z == 1:

            sypher['coin'] += inv[item]['preço']
            inv[item]['qtd'] -= 1  # Retira 1 da quantidade do item que foi vendido
            if inv[item]['qtd'] == 0:  # Caso a quantidade do item seja 1 ou menor
                inv.remove(inv[item])  # Remove o item do inventário
        else:
            loja(city, city_swd, city_pot)
    else:
        loja(city, city_swd, city_pot)


def c_item_select(inv, city, city_swd, city_pot):  # Função para seleção de item da loja

    global item

    it_id = 1
    for itt in inv:  # Atribui pra cada item no inventário um id temporario Ex:'id':1,'id':2...
        itt['id'] = it_id  # Atribui o id para o item
        it_id += 1  # Id sempre será de 1 até o final da lista

    item = int(input('\33[1;36m> \33[m'))  # Recebe um número informado q corresponda ao número do item no inventário

    id_r = 0  # Variavel para indicar id verdadeiro ou não

    for itt in inv:  # Para procurar nos itens se o número escolhido pelo jogador é igual a um id de um item
        if item == itt['id']:
            id_r = 1  # Caso encontre um valor igual, atribuirá 1 para uma variavel x

    if id_r == 1:  # Se x for verdadeiro (há id igual ao numero inserido pelo usuario), ele mostrá o item correspondente
        item -= 1  # Como o número é um indice, tem q ser retirado 1 do valor
        print('\33[1;35mDeseja Comprar > {}\33[m'.format(inv[item]['nome']))  # Indice e chave [index][key]
    else:
        loja(city, city_swd, city_pot)

    return item


def c_item_buy(inv, s_inv, city, city_swd, city_pot):  # Recebe o atributo do inventário da loja e do personagem

    flag = 0

    if inv[item]['preço'] <= sypher['coin']:  # Caso o preço seja menor ou igual a quantidade de moedas
        sypher['coin'] -= inv[item]['preço']  # Subtrai o preço
        for itt in s_inv:  # Checka o inventário de sypher para saber se ele já tem ou não o item
            if itt == inv[item]:
                itt['qtd'] += 1  # Se tiver adiciona 1 na quantidade
                flag = 1
        if flag == 0:
            s_inv.append(inv[item])  # Se n tiver adiciona o item ao inventário
        print('\33[1;32m=== Comprou {} ==='.format(inv[item]['nome']))
        print('\n\33[1m Você possui {} moedas\33[m'.format(sypher['coin']))
    else:
        print("\n\33[1;32m=== Moedas Insuficientes ===")
        loja(city, city_swd, city_pot)


def loja(city, city_swd, city_pot):  # Loja

    print("\n\33[1;35m=== Bem vindo a loja de {} ===\33[m\n".format(city['nome']))
    print("\33[1;34mGostaria de comprar ou vender um item?")
    sel = int(input("\33[1;34m1.Comprar - 2.Vender > "))

    if sel == 1:  # Caso o jogador queira comprar um item
        cop = int(input("\33[1m1.Espadas - 2.Poções > "))
        print('\n\33[1m Você possui {} moedas\33[m'.format(sypher['coin']))
        if cop == 1:
            c_item_show(city_swd)
            c_item_select(city_swd, city, city_swd, city_pot)
            c_item_buy(city_swd, espadas, city, city_swd, city_pot)
        if cop == 2:
            c_item_show(city_pot)
            c_item_select(city_pot, city, city_swd, city_pot)
            c_item_buy(city_pot, pocoes, city, city_swd, city_pot)
        else:
            menu_cd(city, city_swd, city_pot)  # Caso  não seja um número da lista, retorna ao menu

    if sel == 2:  # Caso o jogador queira vender um item
        cop = int(input("\33[1m1.Espadas - 2.Poções > "))
        print('\n\33[1m Você possui {} moedas\33[m'.format(sypher['coin']))
        if cop == 1 and len(espadas) != 0:
            v_item_show(espadas)
            v_item_select(espadas, city, city_swd, city_pot)
        if cop == 2 and len(pocoes) != 0:
            v_item_show(pocoes)
            v_item_select(pocoes, city, city_swd, city_pot)
        else:
            print("\33[1;31mNão há nada neste inventário para vender\33[m")
    else:
        menu_cd(city, city_swd, city_pot)  # Caso  não seja um número da lista, retorna ao menu


# ======

def move_dg(dg):  # Função para movimento baseado em floors, cada floor randomiza o algoritmo evento

    global dgwin

    if dg['floor'] >= 1:
        dg['floor'] -= 1
    else:
        print("\33[1;36m=== Você escapou da primeira masmorra ===\33[m")
        print('\33[1m==========================================================\33[m')
        for c in range(1, 4):
            sleep(0.7)
            print("...\n")
        dgwin = 1
        print("\33[1;35m\"Seja bem vindo a cidade de Akhato\"\33[m\n")

    return dgwin


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


def menu_items():  # Menu para exibição de itens

    itt2 = int(input("1.Espadas - 2.Poções > "))
    if itt2 != 1 and itt2 != 2:
        menu_items()
    if itt2 == 1:
        if len(espadas) == 0:  # Caso não tenha itens
            print("\n\33[1;31m===== Não há nada neste inventário =====\33[m")
        else:  # Caso tenha itens
            item_show(espadas)
            item_select(espadas)
    if itt2 == 2:
        if len(pocoes) == 0:  # Caso não tenha itens
            print("\n\33[1;31m===== Não há nada neste inventário =====\33[m")
        else:  # Caso tenha itens
            item_show(pocoes)
            item_select(pocoes)


def status():  # Status (vida,xp,nivel...)

    print(
        "\33[1;36m Vida: \33[1;32m{}\33[m/\33[1;32m{}\33[m\t\t\t\33[1;36mAtaque: \33[1;32m{}\33[m~\33[1;32m{}\33[m+(\33[1;32m{}\33[m)".format(
            sypher['hp'], sypher['max_hp'], sypher['attack min'], sypher['attack max'], dmg))
    print("\33[1;36m Nível: \33[1;32m{}\33[m\t\t\t\t\t\t\33[1;36mXp: \33[1;32m{}\33[m/\33[1;32m{}\33[m".format(
        sypher['lv'], sypher['xp'], sypher['max_xp']))
    print("\33[1;36m Moedas: \33[1;32m{}\33[m\t\t\t\t".format(sypher['coin']))


def menu_cd(city, city_swd, city_pot):  # Menu da cidade

    print('\33[1m==========================================================')
    x = int(input("1.Inventário - 2.Status - 3.Andar - 4.Loja > "))
    print('==========================================================\33[m')

    if x == 1:  # Inventário
        menu_items()

    if x == 2:  # Status
        status()

    if x == 3:  # Andar pela cidade
        move_city(city)
        print("\n\33[1;36m=== Você deu um passo na cidade de {} {}/10 ===\n\33[m".format(city['nome'], city['floor']))

    if x == 4:  # Loja de espadas e poções
        loja(city, city_swd, city_pot)

    if x != 1 and x != 2 and x != 3 and x != 4:  # Caso não seja 1,2,3 e 4 repete a função
        menu_cd(city, city_swd, city_pot)


def menu():  # Menu principal

    print('\33[1m==========================================================')
    x = int(input("1.Inventário - 2.Status - 3.Andar > "))
    print('==========================================================\33[m')
    #  x=int(input("\n\33[1m1.Inventário - 2.Status - 3.Andar - 4.Salvar > \33[m"))

    if x == 1:  # Inventário
        menu_items()

    if x == 2:  # Status
        status()

    if x == 3:  # Movimento de andar
        move_dg(Dungeon1)
        if dgwin != 1:
            print("\n\33[1;36m=== Você deu um passo adentro da masmorra ===\n\33[m")
            monster()

    if x != 1 and x != 2 and x != 3:  # Caso não seja 1,2 e 3 repete a função
        menu()

    # if menu1 == 4:   função salvar ainda não implementada ;-;


def kill_event():  # Recompensa ao matar um inimigo

    print(
        '\n\33[1;34m=== Você matou um monstro e ganhou {} moeda(s) + {} xp ===\33[m'.format(enemy['coin'], enemy['xp']))

    sypher['xp'] += enemy['xp']
    sypher['coin'] += enemy['coin']
    dif = sypher['xp'] - sypher['max_xp']

    loot = randint(1, 10)
    flag = 0

    if loot == 10:  # Função para loot
        for itt in espadas:
            if itt == enemy['loot']:
                itt['qtd'] += 1
                flag = 1
        if flag == 0:
            espadas.append(enemy['loot'])

    if sypher['xp'] > sypher['max_xp']:
        sypher['lv'] += 1
        sypher['xp'] = dif
        print('\n\33[1;34m=== Você subiu para o nível {} ===\33[m'.format(sypher['lv']))

    if sypher['xp'] == sypher['max_xp']:
        sypher['xp'] = 0
        sypher['lv'] += 1
        print('\n\33[1;34m=== Você subiu para o nível {} ===\33[m'.format(sypher['lv']))


def enemy_attack():  # Função de dano de cada ataque do inimigo

    e_a = randint(-enemy['attack max'], -enemy['attack min'])
    sypher['hp'] += e_a

    return e_a


def random_attack():  # Função de dano de cada ataque de Sypher

    c_a = randint(-sypher['attack max'], -sypher['attack min'])
    c_a += (-1 * dmg)  # O attack de Sypher recebe o dano adicional da espada
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
    if sypher['hp'] <= 0:
        print('\n\33[1;31m===== Você morreu =====\33[m')
        dead = 1  # Var que declara Sypher como morto
    else:
        print("\33[1;36m# Vida Atual:{}/{} #\33[m\n".format(sypher['hp'], sypher['max_hp']))

    return dead


def game():  # Inicia uma batalha com um inimigo

    global e_dead

    e_dead = 0  # Reseta a morte do inimigo
    enemy['hp'] = enemy['max_hp']  # Reseta a vida do inimigo
    while enemy['hp'] > 0 and dead != 1:
        x = str(input("\33[2;34m1.Atacar - 2.Usar item \33[m\33[1;37m>\33[m"))

        if x == '1':  # 1 para atacar
            atacar()
            if e_dead == 1:
                kill_event()
                break
            else:
                monstro_atacar()

        if x == '2':  # 2 para usar item
            menu_items()


# ============== Jogo =================

while dead != 1:  # Enquanto Sypher não morre, o jogo roda o menu
    if dgwin != 1:
        menu()
    else:
        menu_cd(Akhato, akh_swd, akh_pot)
