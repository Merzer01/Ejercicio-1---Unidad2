import csv
from classEmail import email

class manejador:
    __lista = []
    def __init__(self):
        self.__lista = []
    def readarchivo(self):
        with open ('mails.csv') as archivo:
            lector = csv.reader(archivo, delimiter=',')
            next(lector)

            for row in lector:
                dato = row[1]
                if ((dato.count('@') == 1) and ((dato.count('.com')) == 1 or (dato.count('.edu')) == 1)):
                    print("CORREO VALIDO -> {}".format(dato))
                    em = email.crearcuenta(dato)
                    self.__lista.append(em)
                else:
                    print("EL CORREO {} ES INVALIDO \n".format(dato))
    def cantdom(self, dom):
        cont = 0
        for i in range(len(self.__lista)):
            if (dom == self.__lista[i].getdominio()):
                cont += 1
        print("El dominio {} esta en {} objetos de la clase Email \n".format(dom, cont))