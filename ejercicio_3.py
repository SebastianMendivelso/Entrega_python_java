''' En este problema debemos de definir una constante con el valor de PI como 3,1416 y tenemos un único dato de entrada
dado por el usuario: un valor numérico que puede ser entero o flotante que indicara el radio de un círculo. 
La salida del algoritmo será el área del circulo teniendo en cuenta que A=PI*r^2.
Si el usuario ingresó valor negativo o cero tendremos que emitir
un mensaje informando las causas por las cuales no se podrá efectuar la operación. • '''

from main import informacion,alerta,error,negrita,texto_es_numero
import math
def calcular_hipotenusa(numero:int|float|str)->bool|float: #es para recibir los datos sean los que sea y se convierten 
    PI=3.1416
    if numero <0:
        print(negrita(error("no se puede calcular la operación")))
        return False
    else:
        return (math.pi *(numero **2),2)
def menu_hipotenusa():
    print("")
    print("Ingrese el valor numerico en donde se le devolvera el area de el circulo")
    numero = texto_es_numero(input("Ingrese el número a validar:\n"))
    resultado = calcular_hipotenusa(numero)
    print("El resultado de la hipotenusa es:",resultado)
if __name__ == "__main__":
    a = 9
    print(calcular_hipotenusa(a))
    menu_hipotenusa(a)