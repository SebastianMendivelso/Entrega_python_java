from main import informacion, alerta, error, negrita, texto_es_numero
def calcular_mes(mes: int):
    meses = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    if mes >= 1 and mes <= 12:
        return meses[mes]
def menu_mes():
    print("")
    print("Se nos dara como resultado el numero que indiques segun el mes")
    mes = texto_es_numero(input("Ingrese el numero de 1 al 12:\n"))
    resultado = calcular_mes(mes)
    print( f"El mes el cual se digito el numero fue el: {resultado}" if resultado else "El número debe estar en el rango de 1 a 12")
if __name__ == "__main__":
    a = 5
    menu_mes()
