class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Buzinando: Bii Bii!")

    def correr(self):
        print("A bicicleta está correndo!")

    def parar(self):
        print("A bicicleta parou.")

    def exibir_informacoes(self):
        print(f"Cor: {self.cor}")
        print(f"Modelo: {self.modelo}")
        print(f"Número: {self.ano}")
        print(f"Valor: R${self.valor:.2f}")

# Criando uma instância da classe Bicicleta
bicicleta1 = Bicicleta("Rosa", "Mountain Bike", 2020, 1500.00)

# Exibindo as informações da bicicleta
bicicleta1.exibir_informacoes()

# Chamando os comportamentos da bicicleta
bicicleta1.buzinar()
bicicleta1.correr()
bicicleta1.parar()
