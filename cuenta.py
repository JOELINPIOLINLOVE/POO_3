class Cuenta:
    def _init_(self, numero, titular, saldo, limite):
        print('Construyendo el Objeto...{}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    def extracto(self):
        print("saldo {} del titular {}  ".format(self.__saldo,self.__titular))
    
    def depositar(self,valor):
        self.__saldo += valor
        
    def retirar (self,valor):
        if(valor<= self.saldo):
            self.__saldo -= valor
        else:
            print("No tiene suficiente saldo")