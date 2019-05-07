def menu():
    print("1) Plus + ")
    print("2) Minus - ")
    print("3) Gange * ")
    print("4) Dividere / ")
    print("5) Stop Program ")

def plus():
    print("Du Har Valgt +")
    print()
    tal1 = float(input("Tast Tal Nr 1 "))
    print()
    tal2 = float(input("Tast Tal Nr 2 "))
    print()
    print("Tallet Er =","%4.2f"% (tal1+tal2))
    print()

def minus():
    print("Du Har Valgt -")
    print()
    tal1 = float(input("Tast Tal Nr 1 "))
    print()
    tal2 = float(input("Tast Tal Nr 2 "))
    print()
    print("Tallet Er =","%4.2f"% (tal1-tal2))
    print()

def gange():
    print("Du Har Valgt *")
    print()
    tal1 = float(input("Tast Tal Nr 1 "))
    print()
    tal2 = float(input("Tast Tal Nr 2 "))
    print()
    print("Tallet Er =","%4.2f"% (tal1*tal2))
    print()

def dividere():
    print("Du Har Valgt /")
    print()
    tal1 = float(input("Tast Tal Nr 1 "))
    print()
    tal2 = float(input("Tast Tal Nr 2 "))
    print()
    print("Tallet Er =","%4.2f"% (tal1/tal2))
    print()

menu()
menunr = int(input("Vælg Et Tal "))
print()

wh=1
while wh==1:
    if menunr==1:
        plus()
        menu()
        menunr = int(input("Vælg Et Tal "))

    if menunr==2:
        minus()
        menu()
        menunr = int(input("Vælg Et Tal "))

    if menunr==3:
        gange()
        menu()
        menunr = int(input("Vælg Et Tal "))

    if menunr==4:
        dividere()
        menu()
        menunr = int(input("Vælg Et Tal "))

    if menunr==5:
        print()
        exit("Programmet Stopper Nu")

    else:
        menu()
        menunr = int(input("Vælg Et Tal "))
