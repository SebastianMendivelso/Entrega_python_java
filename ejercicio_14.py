''' Desarrollar un algoritmo que determine si una cadena de caracteres es palíndroma. 
Una cadena se dice palíndromo si al invertirla es igual a ella misma. '''

from main import informacion, alerta, error, negrita, texto_es_numero
def es_palindromo(palindromo: str) -> bool:
    palindromo = palindromo.lower().replace(" ", "").replace(",", "").replace(".", "") #en el lower me demore , ya que no entiendo esos terminos y tuve que investigar
    return palindromo == palindromo[::-1]
def menu_palindromo():
    print("Se validará si la cadena es un palíndromo.")
    palabra = input("Ingrese una cadena de caracteres:\n")
    print("El caracter es palindroma" if es_palindromo(palabra) else "El caracter no es palindroma")
if __name__ == "__main__":
    menu_palindromo()