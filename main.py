def menu():
    menu_option = 0
    print("-"*42)
    print("Invoice Management Program - (IMS)")
    print("-"*42)
    print("1 .......... Buscar Cliente")
    print("2 .......... Agregar Cliente")
    print("3 .......... Borrar Cliente")
    print("4 .......... Agregar Factura")
    print("5 .......... Pagar Factura")
    print("6 .......... Salir") 
    print("-"*42)
    menu_option = int(input("Seleccione una opcion: "))
    print("-"*42)

#entry point
if __name__ == "__main__":
    menu()