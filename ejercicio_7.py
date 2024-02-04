''' Calcular la hipotenusa de un triángulo, teniendo como base el valor del cateto 1 y 2 que serán dados por el usuario. 
Para esto debe de hacer uso del Teorema de Pitágoras en el cálculo de la hipotenusa teniendo los catetos.
(h= √(a^2 )+b^2) no se debe hacer uso de la librería Math.hypot '''

from main import informacion, alerta, error, negrita, texto_es_numero
import math
def calcular_catetos(cateto1: int, cateto2: int) -> tuple:
    if cateto2 == 0:
        print("La división es una indeterminación")
        return 0, 0
    else:
        return math.hypot(cateto1, cateto2)
def menu_catetos():
    print("")
    print("Se validara cual la hipotenusa donde se piden los dos catetos")
    cateto1 = texto_es_numero(input("Ingrese el primer cateto:\n"))
    cateto2 = texto_es_numero(input("Ingrese el segundo cateto:\n"))
    resultado = calcular_catetos(cateto1, cateto2)
    print(f"El resultado de los dos catetos a la hipotenusa es:{resultado}")
if __name__ == "__main__":
    a = 5
    b = 6
    menu_catetos()
