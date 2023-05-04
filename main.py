from classEmail import email
from classManejador import manejador

def test(m):
    print("---------->TEST<----------")
    strtest1 = "testemail@gmail.com"
    mailtest1 = email.crearcuenta(strtest1)
    print(mailtest1)
    d1 = "gmail"    #dato existente en el archivo
    d2 = "fi-unjs"  #dato inexistente en el archivo
    m.cantdom(d1)
    m.cantdom(d2)
    mod_pasw(mailtest1)
'''Para el primer ingreso (dato erroneo) ingrese "temporal"
Para el segundo ingreso (dato correcto) ingrese "temppasw"
De esta forma se prueba si la contraseña es la correcta o no.'''


def mod_pasw(n):                                 #MODIFICA LA CONTRASEÑA DEL OBJETO
    band = False
    comp = str(input("Ingrese su contraseña -> "))
    while (band != True):
        if (comp == n.getpassword()):
            print("CONTRASEÑA CORRECTA")
            npasw = str(input("Ingrese su nueva contraseña -> "))
            n.changepassword(npasw)
            band = True
        else:
            print("CONTRASEÑA INCORRECTA")
            comp = str(input("Ingrese su contraseña -> "))

if __name__ == '__main__':
    m = manejador()
    m.readarchivo()    
    comp = str(input("Desea ejecutar la funcion test? (Si o No)-> "))
    if comp == "Si":
        test(m)
    else:
        nomb = nombre = str(input("Ingrese su nombre -> "))
        dir = str(input("Ingrese su direccion de mail -> "))
        nmail = email.crearcuenta(dir)
        print("Estimado {} te enviaremos tus mensajes a la direccion {}\n".format(nombre, nmail))
        print("Su contraseña temporal es ''temppasw''")
        mod_pasw(nmail)
        print("\n")
        d = str(input("Ingrese el dominio -> "))
        m.cantdom(d)