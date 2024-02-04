''' Dado un número entero leído por pantalla, muestre cada uno 
de los dígitos del número en orden inverso. Ej: Si el número es 324, se debe mostrar 4, 2, 3. '''

from main import informacion, alerta, error, negrita, texto_es_numero
def calcular_Inversa_Numero(inversa: int ) -> tuple:
    if inversa == 0:
        print("El cálculo no se puede realizar")
        return 0
    else:
        inversa= (str(inversa) [::-1])
        return inversa
def menu_Inversa_Numero():
    print("")
    print("Se validará un número en el cual se mostrara en el orden inverso")
    inversa = texto_es_numero(input("Ingrese un número en el cual se mostrara en su orden inverso\n"))
    cambio_numero = calcular_Inversa_Numero(inversa)
    print(f"El resultado de su operación en la cual se va a calcular:{cambio_numero}")
if __name__ == "__main__":
    menu_Inversa_Numero()