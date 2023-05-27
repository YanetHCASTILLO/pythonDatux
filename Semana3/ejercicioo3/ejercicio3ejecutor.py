from ejercicio3.funcion import*

a=float(input("Introduzca el primer numero \n"))
b=float(input("Introduzca el segundo numero \n")) 
print("Bienvenido al menú interactivo")
while True:
    print("""¿Qué quieres hacer? Escribe una opción
    1) sumar
    2) restar
    3) multiplicar
    4) dividir
    5) salir""")
    
    opcion = input() # me devuelve un string ''
    if opcion == '1':
        sumar(a,b)
    elif opcion == '2':
        restar(a,b)
    elif opcion == '3':
        multiplicar(a,b)
    elif opcion == '4':
        dividir(a,b)
    elif opcion =='5':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
