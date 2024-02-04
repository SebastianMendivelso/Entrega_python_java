'''Se debe de ingresar un numero por el usuario, este debe de ser evaluado para verificar 
que el número de cifras sea par y verificar si el número es capicúa o no. '''

from main import informacion, alerta, error, negrita, texto_es_numero
def calcular_Capicua(capicua: int) :
    if capicua > 0:
        conversion_letra = str(capicua)
        if conversion_letra == conversion_letra[::-1]:
            print(f"El número {capicua} es capicua")
        else:
            print(f"El número {capicua} no es capicua")
        numero_alreves = int(conversion_letra[::-1])
        print(f"El número {capicua} en orden inverso es: {numero_alreves}")
    else:
        print("El número no es positivo")
def menu_Capicua():
    print("Se validará un número en el cual se mostrará en el orden inverso")
    capicua = texto_es_numero(input("Ingrese un número en el cual se mostrará en su orden inverso:\n"))
    calcular_Capicua(capicua)
if __name__ == "__main__":
    menu_Capicua()
