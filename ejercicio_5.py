from main import negrita, error, texto_es_numero
from datetime import datetime

def calcular_fecha_ejr5(cadena: str, formato: str = '%Y%m%d') -> bool:
    try:
        numero = datetime.strptime(cadena, formato)
        return numero
    except ValueError as msg_error:
        return False
def extraer_fecha_ejr5(numero: int) -> (int, int, int):
    if 10000000 <= numero <= 99999999:
        num1 = numero % 100
        numero_sin_dia = numero // 100
        num2 = numero_sin_dia % 100      
        num3 = numero_sin_dia // 100
        return num3, num2, num1
    return False
def menu_fecha_ejr5():
    print("")
    print("Ingrese el valor de ocho dígitos en donde se le dará la fecha ordenada")
    print("Ingrese la fecha que desea validar")
    numero = int(input())
    resultado = calcular_fecha_ejr5(str(numero))
    if resultado:
        num3, num2, num1 = extraer_fecha_ejr5(numero)
        print(f"La fecha que digitaste fue: año {num3}, mes {num2:02d}, día {num1:02d}")
        print("Año:", num3)
        print("Mes:", num2)
        print("Día:", num1)
    else:
        print("La fecha ingresada no es válida.")
if __name__ == "__main__":
    a = 20220128
    resultado = calcular_fecha_ejr5(str(a))
    print(resultado)
    menu_fecha_ejr5()
