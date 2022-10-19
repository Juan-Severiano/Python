cardapio = """
Nosso cardápio de Hamburger

[1] Hamburger de Carne
[2] Hamburger de Queijo
[3] Hamburger Vegetariano

"""
cardapio_refri =  """
Nossas opçoes de Refrigerante:

[1] Coca  Cola
[2] Fanta
[3] Guaraná

"""

burgercarne = 0
burgerqueijo = 0
burgerveg = 0
coca = 0
fanta = 0
guarana = 0



i = input('Voce quer fazer um pedido? S/N: \n').upper()

if (i == 'S') or ( i == 'SIM') or (i == 'YES'):
    while True:
        s = input("""
            Voce vai querer 
            [1] Hamburger
            [2] Refrigerante
            [3] Nenhum dos dois
        """)
        if s == "1":
            while True:
                print(cardapio)
                f = input('Qual será seu pedido? ')
                if (f == '1')or(f == '2')or(f == '3'):
                    if f == '1':
                        print('Voce escolheu um Burger de Carne')
                        burgercarne += 1
                        J = input('Voce quer mais hamburgers? S/N\n').upper()
                        if J == 'N':
                            break

                    elif f == '2':
                        print('Voce escolheu um Burger de Queijo')
                        burgerqueijo += 1
                        J = input('Voce quer mais hamburgers? S/N\n').upper()
                        if J == 'N':
                            break
                    elif f == '3':
                        print('Voce escolheu um BUrger Vegetariano')
                        burgerveg += 1
                        J = input('Voce quer mais hamburgers? S/N\n').upper()
                        if J == 'N':
                            break

        elif s == "2" :
            while True:
                print (cardapio_refri)
                f = input('Qual será seu pedido? ')
                if (f == '1')or(f == '2')or(f == '3'):
                    if f == '1':
                        print('Voce escolheu uma Coca Cola')
                        coca += 1
                        J = input('Voce quer mais algum refrigerante? S/N\n').upper()
                        if J == 'N':
                            break


                    elif f == '2':
                        print('Voce escolheu uma Fanta')
                        fanta += 1
                        J = input('Voce quer mais algum refrigerante? S/N\n').upper()
                        if J == 'N':
                            break
                    elif f == '3':
                        print('Voce escolheu o Guaraná')
                        guarana += 1
                        J = input('Voce quer mais algum refrigerante? S/N\n').upper()
                        if J == 'N':
                            break
                else:
                    print('Digite um valor valido')

        elif s =='3':
            break  
    print(f"""
        Voce pediu {burgercarne} Hamburger(s) de Carne
        Voce pediu {burgerqueijo} Hamburger(s) de Queijo
        Voce pediu {burgerveg} Hamburger(s) Vegetarianos
        Voce pediu {coca} Refrigerante(s) de Coca
        Voce pediu {fanta} Refrigerantess de Fanta
        Voce pediu {guarana} Refrigerantes de Guaraná
    
    """)
elif (i == 'N') or (i == 'NAO') or (i == 'NÃO') or (i == 'NAOP') or (i == 'QUERO NAO BB') :
    print('Ate mais')

else:
    print('é só sim ou nao espertinho')