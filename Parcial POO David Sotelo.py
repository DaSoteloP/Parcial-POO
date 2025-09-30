#Autor: David Sotelo
#parcial POO



#TODOASAP
            #registro de nuevos libros
                #admin
                    #preguntar (nombre, categoria, )
                        #agregar a la base de datos """

            #registro de nuevos ususarios
                #admin y usuario ( AUNQUE EN TEORIA EL USUARIO SE DEBE DE PODER REGISTRAR EL SOLO )
                    #preguntar (nombre, correo)
                        #si ya esta guardado
                            #mostrar "este usuario ya existe"
                        #else
                            #agregar a la base de datos """ + mostrar OK

Categorias_Libros = ["Novela", "infantil", "arte"]
Usuarios =["pepe"]
libros =["Momo","Constitucion"]
a=0

class Seres:
    def __init__(self,admin,persona):
        self._admin = admin
        self._persona = persona

    def RegPersona(persona):
        if persona != Usuarios:
            Usuarios.append


def iniciar(a):
    a = input("\n\nIniciar sesion:\n (1) = Usuario \n\n (2) = Administrador\n\n:")
    if a=="1":
        print("Usuario")
    elif a == "2":
        print("Administrador")
    else:
        print("No valido")



class libro:
    def __init__(self, estado):
        self._estado = estado

    def agregar(libro):
        #si libro x no está en la lista libros, pedir categoria y agregarlo
        return



    #VVV si el libro existe en la lista de libros, VVV
    def Prestado(self):
        if self._estado == "Disp":
            Retirar = input("¿desea retirar el libro?: ")
            if Retirar == 1:
                self._estado = "NoDisp"
                print("Ha retirado el libro")
            elif Retirar != 1:
                return
        elif self._estado == "NoDisp":
            print("El libro no está disponible")



Libro = libro("Disp")

def main():
    iniciar(a)
    Libro.agregar()
   
   
   
   #VVV primero elegir el libro y ver su disponibilidad, y que de ahi llame a VVV
    Libro.Prestado()



if __name__ == "__main__":
    main()
