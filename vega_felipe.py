import funciones as fn
1
while True:
    fn.mostrar_menu()
    opcion = fn.validar_opcion()
    if opcion == 1:
        fn.datos_guardados()
    elif opcion == 2:
        fn.buscar_mascota
    elif opcion == 3:
        pass
    else:
        print("ADIÓS")
        break
