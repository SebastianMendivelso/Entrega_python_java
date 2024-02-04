from main import informacion, alerta, error, negrita, texto_es_numero
def calcular_Caracter_num(cadena: str, caracter: str) -> int:
    contar = 0
    for caracteres in cadena:
        if caracteres == caracter:
            contar += 1
    return contar
def menu_Caracter_num():
    print("Se validara un carácter en el cual se ingresara una cadena para contar las ocurrencias o veces que se repita el mismo caracter.")
    cadena = input("Ingrese la cadena de caracteres en donde se validara:\n")
    caracter = input("Ingrese el caracter a contar en la cadena:\n")
    if len(caracter) == 1:
        validar = calcular_Caracter_num(cadena, caracter)
        print(f"El caracter {caracter} aparece {validar} veces en la cadena.")
    else:
        print("Ingrese un caracter valido 😣")
if __name__ == "__main__":
    menu_Caracter_num()

