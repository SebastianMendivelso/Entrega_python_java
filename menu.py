from rich.console import Console
from rich.table import Table
from rich.text import Text
from main import informacion,alerta,error,titulo,negrita,magenta,imprimir_texto_centralizado
import ejercicio_1,ejercicio_2,ejercicio_3,ejercicio_4,ejercicio_5,ejercicio_6,ejercicio_7,ejercicio_8, ejercicio_9,ejercicio_10,ejercicio_11,ejercicio_12,ejercicio_13,ejercicio_14,ejercicio_15,ejercicio_16
estilo_negrita = "bold magenta"
estilo_titulo = "bold underline"
estilo_informacion = "italic cyan"
estilo_alerta = "bold yellow"
estilo_error = "bold red"
def menu():
    console = Console()
    while True:
        console.print(Text("_" * 90, estilo_negrita))
        console.print(Text(imprimir_texto_centralizado("MENU PRINCIPAL"), estilo_informacion))
        console.print(Text("_" * 90, estilo_negrita))
        console.print(Text(imprimir_texto_centralizado("Seleccione un ejercicio a ejecutar"), estilo_alerta))
        console.print("")
        tabla = Table(show_header=False)
        tabla.add_column("Opción", justify="center", style="bold cyan")
        tabla.add_column("Ejercicio", justify="left", style="bold white")
        ejercicios = [
            ("1", "COCIENTE DE NUMEROS"),
            ("2", "NUMERO IMPAR O PAR"),
            ("3", "AREA DE UN CIRCULO"),
            ("4", "MULTIPLO DE 3 O 4"),
            ("5", "FECHA CON EL FORMATO AAAAMMDD"),
            ("6", "CALCULA EL MAYOR-MENOR-MEDIO"),
            ("7", "CALCULAR LA HIPOTENUSA"),
            ("8", "FECHA CON EL FORMATO AAAAMMDD"),
            ("9", "INGRESA EL NUMERO Y SE TE DEVOLVERA QUE MES PERTENECE"),
            ("10", "CALCULA LOS SEGUNDOS, HORAS Y MINUTOS"),
            ("11", "INGRESA EL NUMERO Y SE TE DARA EN ORDEN INVERSO"),
            ("12", "SI ES PAR Y SI ES CAPICUA O NO"),
            ("13", "INGRESA CARACTER Y DA SALIDA CUANTAS VECES SE REPITE"),
            ("14", "SI LA CADENA ES PALINDROMA"),
            ("15", "NUMERO DE 0-99, SE DARA EL NUMERO ESCRITO"),
            ("16", "CAPITALIZAR LA FRASE Y LA CADENA"),
            ("17", "SALIR DE EL MENU 😛")
        ]
        for opcion, ejercicio in ejercicios:
            tabla.add_row(opcion, ejercicio)
        console.print(tabla)
        opcion = input()
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 16:
                ejercicio = ejercicios[opcion - 1][1]
            if opcion == 1:
                print(negrita(alerta("El ejercicio 1 ")))
                ejercicio_1.menu_cociente()
            elif opcion ==2:
                print(negrita(alerta("El ejercicio 2 ")))
                ejercicio_2.menu_par()
            elif opcion ==3:
                print(negrita(alerta("El ejercicio 3 ")))
                ejercicio_3.menu_hipotenusa()
            elif opcion ==4:
                print(negrita(alerta("el ejercicio 4 ")))
                ejercicio_4.menu_multiplo()
            elif opcion ==5:
                print(negrita(alerta("el ejercicio 5 ")))
                ejercicio_5.menu_fecha_ejr5()
            elif opcion ==6:
                print(negrita(alerta("el ejercicio 6 ")))
                ejercicio_6.menu_numeros_dif()
            elif opcion ==7:
                print(negrita(alerta("el ejercicio 7 ")))
                ejercicio_7.menu_catetos()
            elif opcion ==8:
                print(negrita(alerta("el ejercicio 8 ")))
                ejercicio_8.menu_fecha_ejr8()
            elif opcion ==9:
                print(negrita(alerta("el ejercicio 9")))
                ejercicio_9.menu_mes()
            elif opcion ==10:
                print(negrita(alerta("el ejercicio 10")))
                ejercicio_10.menu_tiempo()
            elif opcion ==11:
                print(negrita(alerta("el ejercicio 11")))
                ejercicio_11.menu_Inversa_Numero()
            elif opcion ==12:
                print(negrita(alerta("el ejercicio 12 ")))
                ejercicio_12.menu_Capicua()
            elif opcion ==13:
                print(negrita(alerta("el ejercicio 13 ")))
            elif opcion ==14:
                print(negrita(alerta("el ejercicio 14 ")))
            elif opcion ==15:
                print(negrita(alerta("el ejercicio 15 ")))
            elif opcion ==16:
                print(negrita(alerta("el ejercicio 16 ")))
            elif opcion == 17:
                console.print(Text(imprimir_texto_centralizado("El programa ha finalizado, Gracias :3"), estilo_error))
                return 0
            else:
                console.print(Text("Coloque un número válido para que pueda correr el programa 😡", estilo_error))
        else:
            console.print("Digite un caracter válido")
if __name__ == "__main__":
    console = Console()
    console.print(Text(imprimir_texto_centralizado("Bienvenido al desarrollo del taller de lógica de programación", 90), estilo_negrita))
    console.print(Text(imprimir_texto_centralizado("Realizado por: Sebastian Umaña 🙂", 90), estilo_negrita))
    console.print(Text(imprimir_texto_centralizado("Ficha: 2670142", 90), estilo_negrita))
    menu()
