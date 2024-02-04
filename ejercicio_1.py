''' En este problema, los datos de entrada son los dos valores enteros que ingresará el usuario a través del teclado
(los llamaremos a y b) y la salida será su cociente (un número flotante).
Ahora bien, existe la posibilidad de que el usuario ingrese como segundo valor el número 0 (cero). 
En este caso, no podremos mostrar el cociente ya que la división por cero es una indeterminación, así que tendremos que emitir 
un mensaje informando las causas por las cuales no se podrá efectuar la operación. '''

from main import informacion,alerta,error,titulo,negrita,magenta,imprimir_texto_centralizado,texto_es_numero
def calcular_cociente(numero1:int, numero2:int)->float:
    if numero2 ==0:
        print("la división es una indeterminación")
        return 0
    else:
        return numero1/numero2
def menu_cociente():
    print("")
    print(negrita(informacion("Validar el cociente de dos números ")))
    numero1 = texto_es_numero(input("Ingrese el primer número a validar\n"))
    numero2 = texto_es_numero(input("Ingrese el segundo número a validar:\n"))
    resultado = calcular_cociente(numero1, numero2)
    print("el resultado de el cociente es:",resultado)
if __name__ == "__main__":
    menu_cociente()