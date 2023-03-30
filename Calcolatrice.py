class Calcolatrice():
    def __init__(self,n1,n2) -> None:
        self.__n1=n1
        self.__n2=n2
    def somma(self):
        return self.__n1+self.__n2

def main():
  
    n1=float(input("dammi un numero: "))
    n2=float(input("dammi un  altro numero: "))
    calc=Calcolatrice(n1,n2)
    print("somma: ",calc.somma())
main()