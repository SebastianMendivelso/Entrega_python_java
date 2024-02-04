from main import informacion, alerta, error, negrita, texto_es_numero
def calcular_tiempo(seg: int) -> tuple:
    if seg == 0:
        print("El cálculo no se puede realizar")
        return 0, 0, 0
    else:
        horas = seg // 3600
        minutos = seg // 60 
        seg = seg
        return horas, minutos, seg
def menu_tiempo():
    print("")
    print("Se validará cuáles son los segundos, minutos, horas")
    seg = texto_es_numero(input("Ingrese el número del cual deseas hacer el cálculo para saber cuánto se gasta en el examen\n"))
    horas, minutos, segundos = calcular_tiempo(seg)
    print(f"El resultado de la operación es:\nHoras: {horas}\nMinutos: {minutos}\nSegundos: {segundos}")
if __name__ == "__main__":
    a = 5
    menu_tiempo()