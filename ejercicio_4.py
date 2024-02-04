''' En este problema tenemos un único dato de entrada: un valor numérico entero que deberá ingresar el usuario.
La salida del algoritmo será informar si el numero ingresado por el usuario es múltiplo de 2 y 3. 
Sabemos que un número es múltiplo de otro cuando al dividir estos dos números el residuo sea 0. 
Si el usuario ingresó un valor negativo o cero tendremos que emitir
un mensaje informando las causas por las cuales no se podrá efectuar la operación. '''

from main import informacion,alerta,error,negrita,texto_es_numero
def calcular_multiplo(numero:int):
    if numero <0:
        print(negrita(error("no se puede calcular la operación")))
        return (texto_es_numero)
    else:
        return numero % 2 == 0 and numero % 3 == 0
def menu_multiplo():
    print("")
    print("Ingrese el valor numerico en donde se le dira si es el número es multiplo de 2 y 3")
    print("Ingrese el numero a validar")
    numero = int (texto_es_numero(input()))
    resultado = calcular_multiplo(numero)
    print("El numero es multiplo de 2 y 3" if resultado else "El número no es multiplo de 2 y 3")
if __name__ == "__main__":
    menu_multiplo()