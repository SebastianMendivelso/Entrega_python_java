'''En este problema tenemos un único dato de entrada: un valor numérico entero que deberá ingresar el usuario. 
La salida del algoritmo será informar si el usuario ingresó un valor par o impar. 
Sabemos que un número par es aquel que es divisible por 2 o, también, que un número es par si el valor 
residual que se obtiene al dividirlo por 2 es cero. 
Según lo anterior, podremos informar que el número ingresado por el usuario es par si al dividirlo por 2 obtenemos un resto igual a cero.
De lo contrario, informaremos que el número es impar. '''

from main import informacion,alerta,error,titulo,negrita,magenta,imprimir_texto_centralizado,texto_es_numero
def calcular_par(numero:int)->bool:
    if numero ==0:
        print("la división es una indeterminación")
        return 0
    else:
        return numero % 2 == 0
def menu_par():
    print("")
    print("Validar el numero par o impar")
    numero = texto_es_numero(input("Ingrese el numero:\n"))
    resultado = calcular_par(numero)
    print("El numero es par" if resultado else "El numero es impar")    

if __name__ == "__main__":
    a = 7
    print(calcular_par(a))
    a = 8
    print(calcular_par(a))
    menu_par()