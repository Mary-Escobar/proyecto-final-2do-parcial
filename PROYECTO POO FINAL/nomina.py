import colorama
from colorama import Fore, Back, Style
from componentes import Menu,Valida
from helpers import borrarPantalla,gotoxy
from crudArhivos import Archivo
from entidadesRol import *
from datetime import date

import time

validar = Valida()
# Procesos de las Opciones del Menu Mantenimiento
def empAdministrativos():
    borrarPantalla()
    gotoxy(17,1);print(f"{Fore.YELLOW}******* ADMINISTRATIVO *******")
    archiEmpleado = Archivo("./archivos/administrativo.txt","|")
    archiDepartamento = Archivo("./archivos/departamento.txt","|")
    archiCargo = Archivo("./archivos/cargo.txt","|")
    empleados = archiEmpleado.leer()
    if empleados : idSig = int(empleados[-1][0][1:])+1
    else: idSig=1
    idSig = f'A{idSig}'
    gotoxy(14,2);print(f"{Fore.BLUE}Codigo: {Fore.GREEN}{idSig}")
    nombre=validar.solo_letras_posiciones("Nombre: ",14,3)
    apellido=validar.solo_letras_posiciones(f"Apellidos: ",14,4)
    cedula=validar.cedula(f"Cedula: ",archiEmpleado,14,5)
    telefono=validar.telefono(f"Telefono: ",14,6)
    direccion=validar.campo_no_vacio_acepte_numeros(f"Direccion: ",14,7)
    cargo=validar.relacion_externa(f"Cargo: ",14,8,archiCargo,)
    departamento=validar.relacion_externa(f"Departamento: ",14,9,archiDepartamento)
    sueldo=float(validar.campo_decimal(f"Sueldo: ",14,10))
    fechaIngreso=validar.fecha("Fecha Ingreso: ",14,11)
    comision=validar.campo_opcion("Comision: ",14,12)
    
    nombre += ' ' +apellido
    gotoxy(15,14);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,14);grabar = input().lower()
    if grabar == "s":
        entDepartamento = Departamento(departamento[0],departamento[1])
        entCargo = Cargo(cargo[0],cargo[1])
        entEmpleado = Administrativo(nombre,entDepartamento,entCargo, direccion, cedula, telefono, fechaIngreso, sueldo,idSig,comision)
        datos =entEmpleado.getEmpleado()
        
        datos = '|'.join(datos)
        archiEmpleado.escribir([datos],"a")                 
        gotoxy(10,16);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
       gotoxy(10,16);input("Registro No fue Grabado\n presione una tecla para continuar...")
    
  
def empObreros():
    borrarPantalla()
    gotoxy(17,1);print(f"{Fore.YELLOW}******* OBRERO *******")
    archiEmpleado = Archivo("./archivos/obrero.txt","|")
    archiDepartamento = Archivo("./archivos/departamento.txt","|")
    archiCargo = Archivo("./archivos/cargo.txt","|")
    empleados = archiEmpleado.leer()
    if empleados : idSig = int(empleados[-1][0][1:])+1
    else: idSig=1
    idSig = f'O{idSig}'
    gotoxy(14,2);print(f"{Fore.BLUE}Codigo: {Fore.GREEN}{idSig}")
    nombre=validar.solo_letras_posiciones("Nombre: ",14,3)
    apellido=validar.solo_letras_posiciones(f"Apellidos: ",14,4)
    cedula=validar.cedula(f"Cedula: ",archiEmpleado,14,5)
    telefono=validar.telefono(f"Telefono: ",14,6)
    direccion=validar.campo_no_vacio_acepte_numeros(f"Direccion: ",14,7)
    cargo=validar.relacion_externa(f"Cargo: ",14,8,archiCargo,)
    departamento=validar.relacion_externa(f"Departamento: ",14,9,archiDepartamento)
    sueldo=float(validar.campo_decimal(f"Sueldo: ",14,10))
    fechaIngreso=validar.fecha("Fecha Ingreso: ",14,11)
    contrato=validar.campo_opcion("Con. Colectivo: ",14,12)
    
    nombre += ' ' +apellido
    gotoxy(15,14);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,14);grabar = input().lower()
    if grabar == "s":
        entDepartamento = Departamento(departamento[0],departamento[1])
        entCargo = Cargo(cargo[0],cargo[1])
        entEmpleado = Obrero(nombre,entDepartamento,entCargo, direccion, cedula, telefono, fechaIngreso, sueldo,idSig,contrato)
        datos =entEmpleado.getEmpleado()
        
        datos = '|'.join(datos)
        archiEmpleado.escribir([datos],"a")                 
        gotoxy(10,16);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
       gotoxy(10,16);input("Registro No fue Grabado\n presione una tecla para continuar...")
    
    
def cargos():
    borrarPantalla()  
    archiCargo = Archivo("./archivos/cargo.txt","|")
    cargos = archiCargo.leer()
    if cargos : idSig = int(cargos[-1][0])+1
    else: idSig=1   
    gotoxy(20,2);print(f"{Fore.YELLOW}******* CARGOS *******")
    gotoxy(15,4);print(f"{Fore.BLUE}Codigo: {Fore.GREEN}{idSig}")
    desCargo=validar.solo_letras_posiciones("Descripcion Cargo: ",15,5)
    gotoxy(15,6);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,6);grabar = input().lower()
    if grabar == "s":
        cargo = Cargo(desCargo,idSig)
        datos = cargo.getCargo()
        datos = '|'.join(datos)
        archiCargo.escribir([datos],"a")
        gotoxy(10,8);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
       gotoxy(10,8);input("Registro No fue Grabado\n presione una tecla para continuar...")


def departamento():
    borrarPantalla()  
    archiDepartamento = Archivo("./archivos/departamento.txt","|")
    departamentos = archiDepartamento.leer()
    if departamentos : idSig = int(departamentos[-1][0])+1
    else: idSig=1   
    gotoxy(20,2);print(f"{Fore.YELLOW}******* DEPARTAMENTO *******")
    gotoxy(15,4);print(f"{Fore.BLUE}Codigo: {Fore.GREEN}{idSig}")
    desDepartamento=validar.solo_letras_posiciones("Descripcion Departamento: ",15,5)
    gotoxy(15,6);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,6);grabar = input().lower()
    if grabar == "s":
        departamento = Departamento(desDepartamento,idSig)
        datos = departamento.getDepartamento()
        datos = '|'.join(datos)
        archiDepartamento.escribir([datos],"a")
        gotoxy(10,8);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
       gotoxy(10,8);input("Registro No fue Grabado\n presione una tecla para continuar...")


def empresa():
    borrarPantalla()
    archiEmpresa= Archivo("./archivos/empresa.txt","|")
    gotoxy(20,2);print(f"{Fore.YELLOW}******* EMPRESA *******")
    nombreE = validar.solo_letras_posiciones("Descripcion Empresa: ",14,3)
    rucE =validar.ruc(f"Ruc: ",archiEmpresa,14,4)
    dirE =validar.campo_no_vacio_acepte_numeros(f"Direccion: ",14,5)
    telefono = validar.telefono("Telefono: ",14,6)
    gotoxy(15,7);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,7);grabar = input().lower()
    if grabar == "s":
        entEmpresa = Empresa(nombreE,dirE,telefono,rucE)
        datos = entEmpresa.getEmpresa()
        datos = '|'.join(datos)
        archiEmpresa.escribir([datos],"a")
        gotoxy(10,8);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
       gotoxy(10,8);input("Registro No fue Grabado\n presione una tecla para continuar...")


def deducciones():
    borrarPantalla()
    archiDeduccion= Archivo("./archivos/deducciones.txt","|")     
    gotoxy(17,2);print(f"{Fore.YELLOW}******* DEDUCCIONES *******")
    ies=float(validar.campo_decimal(f"Iess: ",15,4))
    comi=float(validar.campo_decimal(f"Comisión: ",15,5))
    anti = int(validar.campo_entero(f"Antiguedad: ",15,6))
    gotoxy(15,7);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,7);grabar = input().lower()
    if grabar == "s":
        entDeduccion= Deduccion(ies,comi,anti)
        datos = entDeduccion.getDeduccion()
        datos = '|'.join(datos)
        archiDeduccion.escribir([datos],"a")
        gotoxy(10,8);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
       gotoxy(10,8);input("Registro No fue Grabado\n presione una tecla para continuar...") 


# ...........................................................
# Opciones del Menu Novedades
def sobretiempos():
   borrarPantalla()     
   gotoxy(20,2);print(f"{Fore.YELLOW}INGRESO DE HORAS EXTRAS")
   empleado,entEmpleado = [],None
   aamm,h50,h100=0,0,0
   while not empleado:
      gotoxy(15,5);print(f"{Fore.BLUE}Empleado ID[    ]: ")
      gotoxy(27,5);id = input(f"{Fore.GREEN}").upper()
      archiEmpleado = Archivo("./archivos/obrero.txt","|")
      empleado = archiEmpleado.buscar(id)
      if empleado:
          entEmpleado = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0]) 
          gotoxy(35,5);print(f"{Fore.GREEN}{entEmpleado.nombre}")
      else: 
         gotoxy(27,5);print(f"{Fore.RED}No existe Empleado con ese codigo[{id}]:")
         time.sleep(2);gotoxy(27,5);print(" "*40)
   gotoxy(15,6);print(f"{Fore.BLUE}Periodo[{Fore.GREEN}aaaamm{Fore.BLUE}]")
   aamm=validar.solo_numeros(f"{Fore.RED}Error: Solo numeros",23,6)
   #gotoxy(23,6);aamm = input()
   h50 = int(validar.campo_entero(f"{Fore.BLUE}Horas50: ",15,7))
   h100 = int(validar.campo_entero(f"{Fore.BLUE}Horas100: ",15,8))
   gotoxy(15,9);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,9);grabar = input().lower()
   if grabar == "s":
        archiSobretiempo = Archivo("./archivos/sobretiempo.txt","|")
        sobretiempos = archiSobretiempo.leer()
        if sobretiempos : idSig = int(sobretiempos[-1][0])+1
        else: idSig=1
        sobretiempo = Sobretiempo(entEmpleado,aamm,h50,h100,True,idSig)
        datos = sobretiempo.getSobretiempo()
        datos = '|'.join(datos)
        archiSobretiempo.escribir([datos],"a")                 
        gotoxy(10,10);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(10,10);input("Registro No fue Grabado\n presione una tecla para continuar...")     
     
   
def prestamos():
   borrarPantalla()     
   gotoxy(20,2);print(f"{Fore.YELLOW}******* PRESTAMO ****")
   empleado,entEmpleado = [],None
   aamm,numPagos,cuotas=0,0,0
   while not empleado:
      gotoxy(15,5);print(f"{Fore.BLUE}Empleado ID[    ]: ")
      gotoxy(27,5);id = input(f"{Fore.GREEN}").upper()
      ruta = "./archivos/administrativo.txt"
      if(id[0]=='O'):
          ruta = "./archivos/obrero.txt"
    
      archiEmpleado = Archivo(ruta,"|")
      empleado = archiEmpleado.buscar(id)
      if empleado:
          gotoxy(35,5);print(f"{Fore.GREEN} {empleado[1]}") 
          break
      gotoxy(27,5);print(f"{Fore.RED}No existe Empleado con ese codigo[{id}]:")
      time.sleep(2);gotoxy(27,5);print(" "*40)
   gotoxy(15,6);print(f"{Fore.BLUE}Periodo[aaaamm]")
   aamm=validar.solo_numeros(f"{Fore.RED}Error: Solo numeros",23,6)
   valor=float(validar.campo_decimal('Valor: ',15,7))
   numPagos=int(validar.campo_entero('Numero de pagos: ',15,8))
   saldo=float(validar.campo_decimal('Saldo: ',15,9))
   gotoxy(15,11);grabar = input("Desea guardar el registro(s/n):")
   grabar=grabar.lower()
   if grabar == "s":
        entEmpleado = Administrativo(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0])
        if(id[0]=='O'):
            entEmpleado = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0]) 
        archiSobretiempo = Archivo("./archivos/prestamo.txt","|")
        sobretiempos = archiSobretiempo.leer()
        if sobretiempos : idSig = int(sobretiempos[-1][0])+1
        else: idSig=1
        sobretiempo = Prestamo(entEmpleado,aamm,valor,numPagos,saldo,True,idSig)
        datos = sobretiempo.getPrestamo()
        datos = '|'.join(datos)
        archiSobretiempo.escribir([datos],"a")                 
        gotoxy(14,12);input("Registro Grabado Satisfactoriamente \n Presione una tecla para continuar...")
   else:
       gotoxy(10,12);input("El registro No fue Grabado\n presione una tecla para continuar...")


# ...........................................................
# opciones de Rol de Pago
def rolAdministrativo():
   borrarPantalla()
   # Se ingresa los datos del rol a procesar     
   gotoxy(20,2);print("ROL ADMINISTRATIVO")
   aamm=0
   gotoxy(15,6);print("Periodo[aaaamm]")
   validar = Valida()
   aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   gotoxy(15,7);print("Esta seguro de Procesar el Rol(s/n):")
   gotoxy(54,7);grabar = input().lower()
   entEmpAdm = None
   # Se procesa el rol con la confirmacion del usuario
   if grabar == "s":
        # Obtener lista de empleados a procesar el rol
        archiEmp = Archivo("./archivos/administrativo.txt","|")
        ListaEmpAdm = archiEmp.leer()
        if ListaEmpAdm : 
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            archiDeducciones = Archivo("./archivos/deducciones.txt","|")
            deducciones = archiDeducciones.leer()[0]
            entDeduccion = Deduccion(float(deducciones[0]),float(deducciones[1]),float(deducciones[2]))
            #print(entDeduccion.getIess(),entDeduccion.getComision(),entDeduccion.getAntiguedad())
            nomina = Nomina(date.today(),aamm)
            for empleado in ListaEmpAdm:
              #print(empleado)
              entEmpAdm = Administrativo(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],float(empleado[8]),empleado[0]) 
              #print(entEmpAdm.nombre,entEmpAdm.sueldo)
              nomina.calcularNominaDetalle(entEmpAdm,entDeduccion)
            # grabar cabecera del rol
            datosCab = nomina.getNomina()
            datosCab = '|'.join(datosCab)
            archiRol = Archivo("./archivos/rolCabAdm.txt","|")
            archiRol.escribir([datosCab],"a")
            # grabar detalle del rol
            archiDet = Archivo("./archivos/rolDetAdm.txt","|")
            datosDet = nomina.getDetalle()
            # se graba en el detalle empleado por empleado           
            for dt in datosDet:
                dt = nomina.aamm+'|'+'|'.join(dt)
                archiDet.escribir([dt],"a")
            # imprimir rol
          
            nomina.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,"A D M I N I S T R A T I V O S")
            nomina.mostrarDetalleNomina()
    
   else:
       gotoxy(10,10);input("Rol No fue Procesado\n presione una tecla para continuar...")     

   input("               Presione una tecla continuar...")  

def consultaRol():
   borrarPantalla()
   validar = Valida()
   # Se ingresa los datos del rol a Consultar     
   gotoxy(20,2);print("CONSULTA DE ROL OBRERO - ADMINISTRATIVO")
   rol=0
   aamm=""
   gotoxy(15,4);print(f"{Fore.BLUE}Obrero-Administrativo(O/A): ")
   gotoxy(15,6);print(f"{Fore.BLUE}Periodo[aaaamm]")
   gotoxy(44,4)
   rol=input(f"{Fore.GREEN}").upper()
   aamm=validar.solo_numeros(f"{Fore.RED}Error: Solo numeros",23,6)
   gotoxy(15,7);print("Esta seguro de consultar el Rol(s/n):")
   gotoxy(54,7);procesar = input().lower()
   if procesar == "s":
        if rol == "A": 
            tit = "A D M I N I S T R A T I V O"
            archiRolCab = Archivo("./archivos/rolCabAdm.txt","|")
            archiRolDet = Archivo("./archivos/rolDetAdm.txt","|")
        else: 
            tit = "O B R E R O"
            archiRolCab = Archivo("./archivos/rolCabObr.txt","|")
            archiRolDet = Archivo("./archivos/rolDetObr.txt","|")
        cabrol = archiRolCab.buscar(aamm)
        if cabrol:
            entCabRol = Nomina(cabrol[1],cabrol[0])
            entCabRol.totIngresos=float(cabrol[2])
            entCabRol.totDescuentos=float(cabrol[3])
            entCabRol.totPagoNeto=float(cabrol[4])
            detalle= archiRolDet.buscarLista(aamm)
            for det in detalle:
                entCabRol.detalleNomina.append(det[1:])    
            # print(entCabRol.getNomina())
            # print(entCabRol.getDetalle())
            # input()
            # imprimir rol    
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            entCabRol.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,tit)
            entCabRol.mostrarDetalleNomina()
        else:
            gotoxy(10,10);input(f"{Fore.RED}No existe rol con ese periodo\n presione una tecla para continuar...")     
            
   else:
       gotoxy(10,10);input("Consulta Cancelada\n presione una tecla para continuar...")     
   input("               Presione una tecla continuar...")  

def rolObrero():
   borrarPantalla()
   # Se ingresa los datos del rol a procesar     
   gotoxy(20,2);print("ROL OBRERO")
   aamm=0
   gotoxy(15,6);print(f"{Fore.BLUE}Periodo[aaaamm]")
   validar = Valida()
   aamm=validar.solo_numeros(f"{Fore.RED}Error: Solo numeros",23,6)
   gotoxy(15,7);print(f"{Fore.GREEN}Esta seguro de Procesar el Rol(s/n):")
   gotoxy(54,7);grabar = input().lower()
   entEmpAdm = None
   # Se procesa el rol con la confirmacion del usuario
   if grabar == "s":
        # Obtener lista de empleados a procesar el rol
        archiEmp = Archivo("./archivos/obrero.txt","|")
        ListaEmpAdm = archiEmp.leer()
        if ListaEmpAdm : 
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            archiDeducciones = Archivo("./archivos/deducciones.txt","|")
            deducciones = archiDeducciones.leer()[0]
            entDeduccion = Deduccion(float(deducciones[0]),float(deducciones[1]),float(deducciones[2]))
            #print(entDeduccion.getIess(),entDeduccion.getComision(),entDeduccion.getAntiguedad())
            nomina = Nomina(date.today(),aamm)
            for empleado in ListaEmpAdm:
              #print(empleado)
              entEmpAdm = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],float(empleado[8]),empleado[0]) 
              #print(entEmpAdm.nombre,entEmpAdm.sueldo)
              nomina.calcularNominaDetalle(entEmpAdm,entDeduccion)
            # grabar cabecera del rol
            datosCab = nomina.getNomina()
            datosCab = '|'.join(datosCab)
            archiRol = Archivo("./archivos/rolCabObr.txt","|")
            archiRol.escribir([datosCab],"a")
            # grabar detalle del rol
            archiDet = Archivo("./archivos/rolDetObr.txt","|")
            datosDet = nomina.getDetalle()
            # se graba en el detalle empleado por empleado           
            for dt in datosDet:
                dt = nomina.aamm+'|'+'|'.join(dt)
                archiDet.escribir([dt],"a")
            # imprimir rol
          
            nomina.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,"O B R E R O S")
            nomina.mostrarDetalleNomina()
    
   else:
       gotoxy(10,10);input("Rol No fue Procesado\n presione una tecla para continuar...")     

   input("               Presione una tecla continuar...")  

# Menu Proceso Principal
opc=''
while opc !='4':  
    borrarPantalla()      
    menu = Menu(f"{Fore.MAGENTA}Menu Principal",[f"{Fore.YELLOW}1) {Fore.CYAN}Mantenimiento",f"{Fore.YELLOW}2) {Fore.CYAN}Novedades",f"{Fore.YELLOW}3){Fore.CYAN} Rol de Pago",f"{Fore.YELLOW}4) {Fore.CYAN}Salir{Fore.YELLOW}"],16,10)
    opc = menu.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='7':
            borrarPantalla()    
            menu1 = Menu(f"{Fore.MAGENTA}Menu Mantenimiento",[f"{Fore.YELLOW}1) {Fore.CYAN}Empleados Administratvos",f"{Fore.YELLOW}2) {Fore.CYAN}Empleados Obreros",f"{Fore.YELLOW}3) {Fore.CYAN}Cargos",f"{Fore.YELLOW}4) {Fore.CYAN}Departamentos",f"{Fore.YELLOW}5) {Fore.CYAN}Empresa",f"{Fore.YELLOW}6) {Fore.CYAN}Parametros",f"{Fore.YELLOW}7) {Fore.CYAN}Salir{Fore.YELLOW}"],20,10)
            opc1 = menu1.menu()
            if opc1 == "1":
                empAdministrativos()
            elif opc1 == "2":
                empObreros()
            elif opc1 == "3":
                cargos()
            elif opc1 == "4":
                departamento()
            elif opc1 == "5":
                empresa()
            elif opc1 == "6":
                deducciones()
            

                        
    elif opc == "2":
            borrarPantalla()
            menu2 = Menu(f"{Fore.MAGENTA}Menu Novedades",[f"{Fore.YELLOW}1) {Fore.CYAN}Sobretiempo",f"{Fore.YELLOW}2) {Fore.CYAN}Prestamos",f"{Fore.YELLOW}3) {Fore.CYAN}Salir{Fore.YELLOW}"],20,10)
            opc2 = menu2.menu()
            if opc2 == "1":
                sobretiempos()
            elif opc2 == "2":
                prestamos()

                
    elif opc == "3":
            borrarPantalla()
            menu3 = Menu(f"{Fore.MAGENTA}Menu Rol",[f"{Fore.YELLOW}1) {Fore.CYAN}Rol Administrativos",f"{Fore.YELLOW}2) {Fore.CYAN}Rol Obreros",f"{Fore.YELLOW}3) {Fore.CYAN}Consulta de rol",f"{Fore.YELLOW}4) {Fore.CYAN}Salir{Fore.YELLOW}"],20,10)
            opc3 = menu3.menu()
            if opc3 == "1":
                rolAdministrativo()
            elif opc3 == "2":
                rolObrero()
            elif opc3 == "3":
                consultaRol()

    elif opc == "4":
           borrarPantalla()
           print("Gracias por su visita....")
    else:
          print("Opcion no valida") 

input("Presione una tecla para salir")
borrarPantalla()

