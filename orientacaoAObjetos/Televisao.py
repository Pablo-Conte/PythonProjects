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

    def ligar(self):
        if self.status == 'Desligada':
            self.status = 'Ligada'
            print("\nTelevisao Ligada\n")
        else:
            print("\nTv ja esta ligada!\n")

    def desligar(self):
        if self.status == 'Ligada':
            self.status = 'Desligada'
            print("\nTelevisao Desligada\n")
        else:
            print("\nTv ja esta desligada!\n")

    def getStatus(self):
        print("\nMarca: {}".format(self.marca))
        print("Status: {}".format(self.status))
        print("Canal: {}".format(self.canal))
        print("Volume: {}".format(self.volume))
        print("Polegadas: {}\n".format(self.polegadas))


    def mudarCanal(self, canal):
        if self.status == 'Desligada':
            print("\nTelevisao desligada!\n")
        elif canal >= 1 and canal <= 100:
            self.canal = canal
            print("\nCanal: {}\n".format(canal))
            
        else: 
            print("\nCanal inexistente\n")
    
    def mudarVolume(self, volume):
        if self.status == 'Desligada':
            print("\nTelevisao desligada!\n")
        elif volume >= 0 and volume <= 100:
            self.volume = volume
            print("\nVolume: {}\n".format(volume))
            
        else: 
            print("\nVolume inexistente\n")

onOff = True
tv1 = Televisao(50, 'Sansung', '1', 20)
tv2 = Televisao(50, 'LG', '1', 20)

def menuTv(tv):
    onOff = True
    while onOff == True: 
        try: 
            print("1 - Ligar")
            print("2 - Desligar")
            print("3 - Mudar Canal")
            print("4 - Mudar Volume")
            print("5 - Status")
            print("6 - voltar")
            choice = int(input("Opcao numero: "))

            if choice == 1:
                tv.ligar()
            elif choice == 2:
                tv.desligar()
            elif choice == 3:
                chosen = int(input("Digite o canal que queres colocar (1-100): "))
                tv.mudarCanal(chosen)
            elif choice == 4:
                chosen = int(input("Digite o volume desejado (0-100): "))
                tv.mudarVolume(chosen)
            elif choice == 5:
                tv.getStatus()
            elif choice == 6:
                onOff = False
            else:
                print("Opcao invalida!")

        except:
            print("Ah não, algo deu errado, tente novamente, dados erroneos foram passados!")

while onOff == True: 
    try: 
        print("1 - Televisao 1")
        print("2 - Televisao 2")
        print("0 - Sair")
        choice = int(input("Opcao numero: "))

        if choice == 1:
            menuTv(tv1)
        elif choice == 2:
            menuTv(tv2)
        elif choice == 0:
            onOff = False
        else:
            print("Opcao invalida!")

    except:
        print("Ah não, algo deu errado, tente novamente, se atente ao que foi pedido!")
