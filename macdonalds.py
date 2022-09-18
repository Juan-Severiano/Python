cardapio = """
Nosso cardápio de Hamburger

[1] Hamburger de Carne
[2] Hamburger de Queijo
[3] Hamburger Vegetariano

"""
burgercarne = 0
burgerqueijo = 0
burgerveg = 0



i = input('Voce quer fazer um pedido? S/N: \n').upper()

if i == 'S':
    while True:
        print(cardapio)
        
        f = int(input('Qual será seu pedido? '))
        if (f == 1)or(f == 2)or(f == 3):
            if f == 1:
                print('Voce escolheu um Burger de Carne')
                burgercarne += 1
                J = input('Voce quer pedir mais alguma coisa? S/N\n').upper()
                if J == 'N':
                    break
            elif f == 2:
                print('Voce escolheu um Burger de Queijo')
                burgerqueijo += 1
                J = input('Voce quer pedir mais alguma coisa? S/N\n').upper()
                if J == 'N':
                    break
            elif f == 3:
                print('Voce escolheu um BUrger Vegetariano')
                burgerveg += 1
                J = input('Voce quer pedir mais alguma coisa? S/N\n').upper()
                if J == 'N':
                    break
        else:
            print('Digite um valor valido')
    print(f'Voce pediu {burgercarne} Hamburger(s) de Carne\nVoce pediu {burgerqueijo} Hamburger(s) de Queijo\nVoce pediu {burgerveg} Hamburger(s) Vegetarianos')
    print('Obrigado pela preferencia, volte sempre')
else :
        print('Ate mais')