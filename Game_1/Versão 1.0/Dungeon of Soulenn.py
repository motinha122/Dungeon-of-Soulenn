from random import randint
from time import sleep

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

Dungeon1 = {'floor':70}

main_char ={'hp':50,'attack min':2,'attack max':5,'defense':3,'xp':0,'lv':1,'max_xp':20} #Personagem principal

slime = {'hp':10,'attack min':2,'attack max':5,'coin':3,'xp':5,'lv':1,'max_xp':20} #Slime

skeleton = {'hp':20,'attack min':3,'attack max':7,'coin':5,'xp':10,'lv':1,'max_xp':40} #Esqueleto

inventario = {} #Inventário para guardar itens

Coin_bag = 10   #Bolsa de dinheiro

floor = {'floor':0}

def move():         #Função para movimento baseado em floors, cada floor randomiza o algoritmo evento
    if Dungeon1['floor']>=1:
        floor['floor']+=1
        Dungeon1['floor']-=1
    else:
        print("\33[1;36m=== Você venceu a Dungeon ===\33[m")
    return floor,Dungeon1

def menu(x):

    if x == 1:
        print("\n\33[1m === Você possui {} moeda(s) ===\33[m".format(Coin_bag))
        if len(inventario) == 0:
            print("\n\33[1;31m===== Não há nada no inventário =====\33[m")

    if x == 2:
        print("\n\33[1;36m Vida: {}\33[m".format(main_char['hp']))
        print("\33[1;36m Nível: {}  Xp: {} \n\33[m".format(main_char['lv'],main_char['xp']))

    if x == 3:
        move()


    #if menu1 == 4:   função salvar ainda n implementada ;-;

    return menu1

def slime_attack():
    s_a = randint(-slime['attack max'],-slime['attack min'])
    main_char['hp'] += s_a
    return s_a

def random_attack():
    c_a = randint(-main_char['attack max'],-main_char['attack min'])
    slime['hp'] += c_a
    return c_a

#def use_items():
def atacar():
    print("Dano causado:{}".format(-1*random_attack()))
    print("Vida do bicho:{}".format(slime['hp']))

while slime['hp'] > 0:
#    select_act()
    x=str(input("\33[2;34m 1.Atacar - 2.Usar item \33[m\33[1;37m>\33[m"))
    print('\n')
    if x == '1':
        print("Dano causado:\33[1;32m{}\33[m".format(-1*random_attack()))
        if slime['hp']<=0:
            print("\33[1;31m Vida do bicho:0 X-X \33[m")
        else:
            print("\33[1;31m Vida do bicho:{} \33[m".format(slime['hp']))
        sleep(0.5)
        print("\nVocê sofreu \33[1;31m{}\33[m de dano".format(-1*slime_attack()))
        print("\n\33[1;36m Vida Atual:{} \33[m".format(main_char['hp']))

    if x == '2':
        if len(inventario) == 0:
            print("\n===== Não há nada no inventário =====\n")
        else:
            print("potato")


    if main_char['hp'] <= 0:
        print('\n\33[1;31m===== Você morreu =====\33[m')
        break
    if slime['hp'] <= 0:
        print('\n\33[1;34m=== Você matou um slime e ganhou {} moeda(s) ===\33[m'.format(slime['coin']))
        Coin_bag += slime['coin']
    #slime

menu1=int(input("\n\33[1m1.Inventário - 2.Status - 3.Andar - 4.Salvar > \33[m"))

while menu1!=1 and menu1!=2 and menu1!=3 and menu1!=4:
    menu1=int(input("\n\33[1m1.Inventário - 2.Status - 3.Andar - 4.Salvar > \33[m"))

menu(menu1)
