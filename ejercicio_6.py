''' Leer tres valores numéricos enteros, indicar cuál es el mayor, cuál es el del medio y cuál, el menor. 
Considerar que los tres valores serán diferentes. '''

from main import informacion, alerta, error, negrita, texto_es_numero
import math
def calcular_numeros_dif(numero1: int, numero2: int, numero3: int) -> tuple:
    if numero2 == 0:
        print("La división es una indeterminación")
        return 0, 0, 0
    else:
        if numero1 >= 0 and numero2 >= 0 and numero3 >= 0:
            Mayor = max(numero1, numero2, numero3)
            Menor = min(numero1, numero2, numero3)
            if (numero1 == Mayor or numero1 == Menor) and (numero2 == Menor or numero2 == Mayor):
                Medio = numero3
            elif (numero1 == Mayor or numero1 == Menor) and (numero3 == Menor or numero3 == Mayor):
                Medio = numero2
            elif (numero2 == Mayor or numero2 == Menor) and (numero3 == Menor or numero3 == Mayor):
                Medio = numero1
            return Mayor, Medio, Menor
def menu_numeros_dif():
    print("")
    print("Se validara cual es el mayor, menor, medio entre tres numeros")
    numero1 = texto_es_numero(input("Ingrese el primer número:\n"))
    numero2 = texto_es_numero(input("Ingrese el segundo número:\n"))
    numero3 = texto_es_numero(input("Ingrese el tercer número:\n"))
    Mayor, Medio, Menor = calcular_numeros_dif(numero1, numero2, numero3)
    print(f"El resultado de la operación es:\nMayor: {Mayor}\nMedio: {Medio}\nMenor: {Menor}")
if __name__ == "__main__":
    a = 5
    b = 6
    c = 7
    menu_numeros_dif()
