# Autor: Alex Serrano Durán
# Este programa usa ciclo while para hacer divisiones o para encontrar el mayor número en una lista


def dividir():
    print("""
Calculando divisiones""")
    dividendo = int(input(""
                        "Dividendo: """))
    divisor = int(input("Divisor: "))
    dividendoOriginal = dividendo
    cociente = 0
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente += 1
    print("""%d / %d = %d, sobra %d
    
    """ % (dividendoOriginal, divisor, cociente, dividendo))


def encontrarMayor():
    print("""
Teclea una serie de números para encontrar el mayor""")
    nuevaOpcion = -2
    mayor = -2
    while nuevaOpcion != -1:
        nuevaOpcion = int(input("Teclea un número [-1 para salir]: "))
        if nuevaOpcion > mayor:
            mayor = nuevaOpcion
        else:
            pass

    if mayor != -1:
        print("El mayor es:", mayor, """
        
        """)
    else:
        print("""No hay valor mayor
        """)


def main():
    accion = -1
    while accion != 3:
        print("""Misión 07. Ciclos while
Autor: Alex Serrano Durán
Matrícula: A01376364.
1. Calcular divisiones
2. Encontrar el mayor
3. Salir""")
        accion = int(input("Teclea tu opción: "))
        if accion == 1:
            dividir()
        elif accion == 2:
            encontrarMayor()
        elif accion != 1 and accion != 2 and accion !=3:
            print("""ERROR, teclea 1, 2 o 3
            
            """)
    print("""
Gracias por usar este programa, regresa pronto.""")


main()
