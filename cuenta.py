class Cuenta:
    def __init__(self, numero, titular, saldo, limite):
        print('Construyendo el Objeto...{}'.format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite