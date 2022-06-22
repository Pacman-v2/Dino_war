def bem_vindo():
    print('-' * 30)
    print(f'{"Bem vindo ao Dino Wars":^30}')
    print('-' * 30)


def filtro_Num(valor):

    while True:

        try:
            valor.isnumeric()

        except:
            print("Digite um valor válido")


def escolha():

    dino = input("Escolha seu dino")

    return dino





