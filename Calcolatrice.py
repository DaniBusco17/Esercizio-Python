from os import system

class Calcolatrice:
    def sottrazione(self):
        return self.__n1 - self.__n2
    
    def divisione(self):
        try:
            nr = self.__n1/self.__n2
            return nr
        except ZeroDivisionError:
            return "ERRORE: impossibile dividere per 0"
        
    def radice(self):
        return self.__n1**(1/self.__n2)

def menu():
    menu = """
    +----------------------+
    | 1) Somma             |
    | 2) Sottrazione       |
    | 3) Moltiplicazione   |
    | 4) Divisione         |
    | 5) Potenza           |
    | 6) Radice            |
    +----------------------+
    | 0) Fine              |
    +----------------------+
    """
    print(menu)
    while True:
        try:
            scelta = int(input("Scegli:"))
            if scelta == 0 or scelta <= 6:
                break
            else:
                print("Input Invalido!")
        except:
            print("Input Inesistente!")
    return scelta

def main():
    print("\nCalcolatrice\n")
    calc = Calcolatrice()
    n1 = ""
    n2 = ""
    while True:
        lista = menu()
        match lista:
            case 1:
                pass
            case 2:
                calc.sottrazione(n1,n2)
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                calc.radice(n1,n2)
            case 0:
                print("\nProgramma terminato. Arrivederci!\n")
                break
        input("\nPremi INVIO per continuare...")
        system("cls")               
main()