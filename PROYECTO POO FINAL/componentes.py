from entidadesRol import Departamento
from os import terminal_size
from helpers import borrarPantalla, gotoxy, mensaje
from colorama import Fore, Back, Style
import time
from datetime import datetime
class Menu:
    def __init__(self,titulo="",opciones=[],col=6,fil=1):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil
        
    def menu(self):
        gotoxy(self.col,self.fil);print(self.titulo)
        self.col-=5
        for opcion in self.opciones:
            self.fil +=1
            gotoxy(self.col,self.fil);print(opcion)
        gotoxy(self.col+5,self.fil+2)
        opc = input("Elija opcion[1...{}]:".format(len(self.opciones))) 
        return opc   

class Valida:
    def solo_numeros(self,mensajeError,col,fil):
        while True: 
            gotoxy(col,fil)            
            valor = input(f"{Fore.GREEN}")
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*20)
        return valor

    def solo_letras(self,mensaje,mensajeError): 
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            if valor.isalpha():
                break
            else:
                print("          ------><  | {} ".format(mensajeError))
        return valor

    def solo_decimales(self,mensaje,mensajeError):
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                print("          ------><  | {} ".format(mensajeError))
        return valor


    def esta_vacio(self,valor):
        if not valor:
            return True
        return False

    def contiene_solo_numeros(self,valor,menor=0):
        valido = False
        try:
            valor  =  valor.replace('0','') if valor.count("0") else valor
            if int(valor) > menor:
                valido = True
        except:
            pass
        return valido

    def contiene_solo_numeros2(self,valor,menor=0):
        valido = False
        try:
            if int(valor) > menor:
                valido = True
        except:
            pass
        return valido

    def contiene_solo_decimal(self,valor):
        valido = False
        try:
            valor = float(valor)
            if valor > float(0):
                valido = True
        except:
            pass
        return valido 

    def cedula(self,campo,archivo,col,fil):
        mensajeError = ''
        while True:
            gotoxy(col,fil);valor = str(input(f'{Fore.BLUE}{campo}{Fore.GREEN}'))
            gotoxy(col+len(campo)+30,fil);print(' '*len(mensajeError))
            if not (self.esta_vacio(valor)):
                if self.contiene_solo_numeros(valor):
                    if len(valor) == 10:
                        dato = archivo.buscar(valor,5)
                        if not dato:
                            break
                        else:
                           mensajeError =f'{Fore.RED} {valor} ya se Encuentra Registrado' 
                    else:
                        mensajeError =f'{Fore.RED} Debe Contener  10 caracteres, No {len(valor)}'
                else:
                    mensajeError =f'{Fore.RED} Debe Contener Solo Numeros'
            else:
                mensajeError =f'{Fore.RED} No puede quedar Vacio'
            gotoxy(col+len(campo)+30,fil); print(mensajeError)
            gotoxy(col+len(campo),fil);print(' '*len(str(valor)))
        return valor
           
    def telefono(self,campo,col,fil):
        mensajeError = ''
        while True:
            gotoxy(col,fil);valor = str(input(f'{Fore.BLUE}{campo}{Fore.GREEN}'))
            gotoxy(col+len(campo)+40,fil);print(' '*len(mensajeError))
            if not (self.esta_vacio(valor)):
                if self.contiene_solo_numeros(valor):
                    if len(valor) == 10:
                        break
                    else:
                        mensajeError =f'{Fore.RED} Debe Contener  10 caracteres, No {len(valor)}'
                else:
                    mensajeError =f'{Fore.RED} Debe Contener Solo Numeros'
            else:
                mensajeError =f'{Fore.RED} No puede quedar Vacio'
            gotoxy(col+len(campo)+40,fil); print(mensajeError)
            gotoxy(col+len(campo),fil);print(' '*len(str(valor)))
        return valor

    def relacion_externa(self,campo,col,fil,archivo,pos =0):
        mensajeError = ''
        while True:
            gotoxy(col,fil); valor = str(input(f'{Fore.BLUE}{campo}{Fore.GREEN}'))
            gotoxy(col+len(campo)+30,fil);print(' '*len(mensajeError))
            dato = archivo.buscar(str(valor),pos)
            if not (self.esta_vacio(valor)):
                if self.contiene_solo_numeros2(valor,-1):
                    dato = archivo.buscar(str(valor),pos)
                    if int(valor) == 0:
                        nombr_campo =campo.replace(':','')
                        gotoxy(col+len(campo),fil);print(f'Sin {nombr_campo}')
                        valor = (f'Sin {nombr_campo}',0,)
                        break
                    elif dato:
                        gotoxy(col+len(campo),fil);print(dato[1])
                        valor = (dato[1],dato[0],)
                        break
                    else:
                        mensajeError =f'{Fore.RED} No existe id {valor} en {campo}'
                else:
                    mensajeError =f'{Fore.RED} Debe Contener Solo Numeros'
            else:
                mensajeError =f'{Fore.RED} No puede quedar Vacio'
            gotoxy(col+len(campo)+30,fil); print(mensajeError)
            gotoxy(col+len(campo),fil);print(' '*len(str(valor)))
        return valor

    def solo_letras_posiciones(self,campo,col,fil):
        mensajeError = ''
        while True:
            gotoxy(col,fil);valor = str(input(f'{Fore.BLUE}{campo}{Fore.GREEN}'))
            gotoxy(col+len(campo)+30,fil);print(' '*len(mensajeError))
            valor = valor.replace(' ','')
            if self.esta_vacio(valor):
                mensajeError =f'{Fore.RED} No puede quedar Vacio'
            elif valor.isalpha():
                break
            else:
                mensajeError =f'{Fore.RED} Debe Contener solo Letras'
            gotoxy(col+len(campo)+30,fil); print(mensajeError)
            gotoxy(col+len(campo),fil);print(' '*len(str(valor)))
        return valor
    
    def campo_no_vacio_acepte_numerosdd(self,campo,col,fil):
        mensajeError = ''
        while True:
            gotoxy(col,fil);valor = str(input(f'{Fore.BLUE}{campo}{Fore.GREEN}'))
            gotoxy(col+len(campo)+30,fil);print(' '*len(mensajeError))
            if self.esta_vacio(valor):
                mensajeError =f'{Fore.RED} No puede quedar Vacio'
            else:
                break
            gotoxy(col+len(campo)+30,fil); print(mensajeError)
            gotoxy(col+len(campo),fil);print(' '*len(str(valor)))
        return valor

    def campo_no_vacio_acepte_numeros(self,campo,col,fil):
        mensajeError = ''
        while True:
            gotoxy(col,fil);valor = str(input(f'{Fore.BLUE}{campo}{Fore.GREEN}'))
            gotoxy(col+len(campo)+30,fil);print(' '*len(mensajeError))
            if self.esta_vacio(valor):
                mensajeError =f'{Fore.RED} No puede quedar Vacio'
            else:
                break
            gotoxy(col+len(campo)+30,fil); print(mensajeError)
            gotoxy(col+len(campo),fil);print(' '*len(str(valor)))
        return valor

    def fecha(self,campo,col,fil):
        mensajeError = ' '
        while True: 
            gotoxy(col,fil);valor = str(input(f'{Fore.BLUE}{campo}{Fore.GREEN}'))
            gotoxy(col+len(campo)+30,fil);print(' '*len(mensajeError))
            try:
                valor = datetime.strptime(valor, '%Y-%m-%d').date()
                break
            except:
                mensajeError = f'{Fore.RED}El formato ingreado es Invalido, formato Correcto es ["aaaa-mm-dd"]'
                time.sleep(1)
            gotoxy(col+len(campo)+30,fil);print(mensajeError)
            gotoxy(col+len(campo),fil);print(' '*len(str(valor)))
        return valor

    def campo_decimal(self,campo,col,fil):
        mensajeError = ''
        while True:
            gotoxy(col,fil);valor = str(input(f'{Fore.BLUE}{campo}{Fore.GREEN}'))
            gotoxy(col+len(campo)+30,fil);print(' '*len(mensajeError))
            if self.esta_vacio(valor):
                mensajeError =f'{Fore.RED} No puede quedar Vacio'
            elif not self.contiene_solo_decimal(valor):
                mensajeError =f'{Fore.RED} No es un Decimal'
            else:
                break
            gotoxy(col+len(campo)+30,fil); print(mensajeError)
            gotoxy(col+len(campo),fil);print(' '*len(str(valor)))
        return valor

    def campo_entero(self,campo,col,fil):
        mensajeError = ''
        while True:
            gotoxy(col,fil);valor = str(input(f'{Fore.BLUE}{campo}{Fore.GREEN}'))
            gotoxy(col+len(campo)+30,fil);print(' '*len(mensajeError))
            if self.esta_vacio(valor):
                mensajeError =f'{Fore.RED} No puede quedar Vacio'
            elif not self.contiene_solo_numeros(valor):
                mensajeError =f'{Fore.RED} No es un Entero'
            else:
                break
            gotoxy(col+len(campo)+30,fil); print(mensajeError)
            gotoxy(col+len(campo),fil);print(' '*len(str(valor)))
        return valor

    def campo_opcion(self,campo,col,fil):
        mensajeError = ' '
        while True:
            gotoxy(col,fil);valor = str(input(f'{Fore.BLUE}{campo}{Fore.GREEN}'))
            gotoxy(col+len(campo)+30,fil);print(' '*len(mensajeError))
            valor = valor.lower()
            if valor == 's' or valor == 'n' :
                valor= True if valor == 's' else False
                break
            else:
                mensajeError= f'{Fore.RED}Invalido, formas de  opcion caracter ["s","S"] o ["n","N") ' 
            gotoxy(col+len(campo)+30,fil); print(mensajeError)
            gotoxy(col+len(campo),fil);print(' '*len(str(valor)))
        return valor

    def ruc(self,campo,archivo,col,fil):
        mensajeError = ''
        while True:
            gotoxy(col,fil);valor = str(input(f'{Fore.BLUE}{campo}{Fore.GREEN}'))
            gotoxy(col+len(campo)+30,fil);print(' '*len(mensajeError))
            if not (self.esta_vacio(valor)):
                if self.contiene_solo_numeros(valor):
                    if len(valor) == 13:
                        dato = archivo.buscar(valor)
                        if not dato:
                            break
                        else:
                           mensajeError =f'{Fore.RED} {valor} ya se Encuentra Registrado' 
                    else:
                        mensajeError =f'{Fore.RED} Debe Contener  13 caracteres, No {len(valor)}'
                else:
                    mensajeError =f'{Fore.RED} Debe Contener Solo Numeros'
            else:
                mensajeError =f'{Fore.RED} No puede quedar Vacio'
            gotoxy(col+len(campo)+30,fil); print(mensajeError)
            gotoxy(col+len(campo),fil);print(' '*len(str(valor)))
        return valor
class otra:
    pass    


