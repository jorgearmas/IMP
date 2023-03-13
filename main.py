
import os

#dictionaries
production_dict = {}
cx_data_dict = {}

#global vars
nif = 0
cx_name = ""
cx_adress = ""
cx_phone = ""

#write_in_file
def write_in_file(new_record):
    f = open("prod.txt", "a")
    f.write(new_record)
    f.close()

#read_file
def read_file():
    with open('prod.txt') as f:
        lines = f.readlines()
        print(lines)
        f.close()

#add customer
def add_cx():
    print("-"*42)
    print("Agregar un nuevo cliente")
    print("-"*42)
    session_add_cx = 1
    global production_dict
    global nif
    global cx_name
    global cx_adress
    global cx_phone

    while session_add_cx == 1:
        pass
        nif = int(input("\nIngrese el NIF / NIT del cliente: "))
        cx_name = input("Ingrese ingrese un nombre y un apellido: ")
        cx_data_dict['name'] = cx_name
        cx_adress = input("Ingrese ingrese direccion del cliente/empresa: ")
        cx_data_dict['address'] = cx_adress      
        cx_phone = input("Ingrese numero de telefono del cliente: ")
        cx_data_dict['phone'] = cx_phone
        production_dict[nif] = cx_data_dict
        
        write_in_file(str(nif)+": "+"{"+"name: "+cx_name+", "+"adress: "+cx_adress+", "+"phone: "+cx_phone+"}"+" | ")
        session_add_cx = int(input("Le gustaria agregar otro cliente? "))
        if session_add_cx != 1:
            os.system('CLS')
            menu()

def del_cx():
    print("-"*42)
    print("Borrar cliente")
    print("-"*42)
    print("Ingrese NIT del cliente a borrar: ")
    read_file()

def menu():
    menu_option = 0
    print("-"*42)
    print("Invoice Management Program - (IMP)")
    print("-"*42)
    print("1 .......... Agregar Cliente")
    print("2 .......... Borrar Cliente")
    print("3 .......... Buscar Cliente")
    print("4 .......... Agregar Factura")
    print("5 .......... Pagar Factura")
    print("6 .......... Salir") 
    print("-"*42)
    menu_option = int(input("Seleccione una opcion: "))
    print("-"*42)
    if menu_option == 1:
        os.system('CLS')
        add_cx()
    elif menu_option == 2:
        del_cx()


#entry point
if __name__ == "__main__":
    menu()