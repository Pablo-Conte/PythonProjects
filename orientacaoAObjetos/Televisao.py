class Televisao:
    polegadas = None
    marca = None
    status = 'Desligada'
    volume = None
    canal = None
    def __init__(self, polegadas, marca, volume, canal):
        self.polegadas = polegadas
        self.marca = marca
        self.volume = volume
        self.canal = canal
onOff = True
tv1 = Televisao(50, 'Sansung', '1', 20)
tv2 = Televisao(50, 'LG', '1', 20)
while onOff == True: 
    try: 
        print("1 - Televisao 1")
        print("2 - Televisao 2")
        print("0 - Sair")
        choice = int(input("Opcao numero: "))

        if choice == 1:
            print("opcao 1")
        elif choice == 2:
            print("opcao 2")
        elif choice == 0:
            onOff = False
        else:
            print("Opcao invalida!")

    except:
        print("Ah não, algo deu errado, tente novamente, se atente ao que foi pedido!")
