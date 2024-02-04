''' Pedir un número de 0 a 99 y mostrarlo escrito. Por ejemplo, para 56 mostrar: cincuenta y seis. '''

from main import informacion, alerta, error, negrita, texto_es_numero
def num_a_palabras(numero1: int) -> str:
    if 0 <= numero1 <= 99:
        unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
        decenas = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
        centenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"] 
        if numero1 < 10:
            return unidades[numero1]
        elif 10 <= numero1 < 20:
            return decenas[numero1 - 10]
        else:
            decena = numero1 // 10
            unidad = numero1 % 10
            if unidad == 0:
                return centenas[decena]
            else:
                return f"{centenas[decena]} y {unidades[unidad]}"# en este codigo tome como guia los que hice en java en la interfaz grafica y tambien de internet
    else:
        return "Digite un numero que este dentro de el rango de 0 a 99🤔"
def menu_Num_Caracter():
    print("Se validara un numero de 0 a 99 y se mostrar como se escribe en palabra.")
    numero_pedido = int(input("Ingrese un numero: \n"))
    resultado = num_a_palabras(numero_pedido)
    print(f"{resultado}")
if __name__ == "__main__":
    menu_Num_Caracter() 
