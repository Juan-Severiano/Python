import random
start = """
Digite

[1] Pedra
[2] Papel
[3] Tesoura
"""
while True:
    print(start)
    a = int(input('Sua escolha:'))
    computador = random.randrange(1, 4)
    if a == computador:
        print(f'''Voce escolheu {a} e o Computador escolheu {computador}\nEMPATE''')

    elif a == 1 and computador == 2:
        print(f'''Voce escolheu {a} e o Computador escolheu {computador}''')
        print('Papel GANHA de Pedra, o Computador venceu')
    elif a == 1 and computador == 3:
        print(f'''Voce escolheu {a} e o Computador escolheu {computador}''')
        print('Pedra GANHA de Tesoura, Voce venceu')
    elif a == 2 and computador == 3:
        print(f'''Voce escolheu {a} e o Computador escolheu {computador}''')
        print('Tesoura VENCE Papel, Voce Perdeu')



