class email:
    __idcuenta = ''
    __dominio = ''
    __tipo_dom = ''
    __password = ''
    def __init__(self, idc, dom, tdom, pasw="temppasw"):   #CONSTRUCTOR
        self.__idcuenta = idc
        self.__dominio = dom
        self.__tipo_dom = tdom
        self.__password = pasw
    def __str__(self):                          #RETORNA EMAIL
        return '({}@{}.{})'.format(self.__idcuenta, self.__dominio, self.__tipo_dom)
    def getdominio(self):                       #RETORNA DOMINIO
        return (self.__dominio)
    def getpassword(self):                      #RETORNA PASSWORD
        return self.__password
    def changepassword(self, np):               #RETORNA PASSWORD
        self.__password = np
    @classmethod
    def crearcuenta(cls, c):                    #CREA UNA INSTANCIA CON UN PARAMETRO
        a1 = c.find('@')
        a2 = c.find('.')
        sli_id = c[:a1]
        if a1 > a2:                             #COMPARA A1 Y A2 EN BUSCA DE PUNTOS PREVIO AL @
            str_aux = c[a1+1:]
            a2 = str_aux.find('.')
            sli_dom = str_aux[:a2]
            sli_tipo = str_aux[a2+1:]
        else:
            sli_dom = c[a1+1:a2]
            sli_tipo = c[a2+1:]
        return cls(sli_id, sli_dom, sli_tipo)