from abc import ABC, abstractmethod
from datetime import datetime
import mysql.connector as mysql
import os

#configuracion de la base de datos.
configuracion = {
    "host":"localhost",
    "user":"root", 
    "password":"",
    "port":3306,
    "database":"empresa"
}


class BdConectar(ABC):
    @abstractmethod
    def conectar(self):
        #logica para conectarnos a la base de datos.
        pass
    

class BdEstado(ABC):
    @abstractmethod
    def estado(self):
        #logica para verificar el estado de la conexion.
        pass




class BdConsultaIngresoEmpleado(ABC):
    @abstractmethod
    def consultar_ingreso_de_empleado():
        #logica para consultar el ingreso de un empleado.
        pass

class BdConsultaSalidaEmpleado(ABC):
    @abstractmethod
    def consultar_salida_de_empleado():
        #logica para consultar el salida de un empleado.
        pass
    
class BdInsertarIngreso(ABC):
    @abstractmethod
    def insertar_ingreso_empleado():
        #logica para ingresar el ingreso de un empleado.
        pass

class BdInsertarSalida(ABC):
    @abstractmethod
    def insertar_salida_empleado():
        #logica para insertar la salida de un empleado.
        pass

#Nos conectamos a la base de datos con la configuracion que definimos previamente.
class ConectarBaseDeDatos(BdConectar):
    def __init__(self, **kwargs):
        self.configuracion = kwargs
        self.conexion = None

    def conectar(self):
        self.conexion = mysql.connect(**self.configuracion)
        return self.conexion
        


#mostrar el estado de la conexion a la base de datos.
class ImprimirEstado(BdEstado):
    def __init__(self, conexion):
        self.conexion = conexion

    def estado(self):
        print(self.conexion.is_connected())



#Mostramos el ingreso de los empleados.
class MostrarIngresoDeEmpleado(BdConsultaIngresoEmpleado):
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()
    def consultar_ingreso_de_empleado(self):
        query = """
                SELECT * FROM asistencia_ingreso;
                """
        self.cursor.execute(query)
        datos = self.cursor.fetchall()
        return datos
        """for id,nombre,hora1 in datos:
            print(f"ingreso de {nombre}: {hora1}")

        input("Presionar enter...")"""

#Mostramos la salida de los empleados.
class MostrarSalidaDeEmpleado(BdConsultaSalidaEmpleado):
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()
    def consultar_salida_de_empleado(self):
        query = """
                SELECT * FROM asistencia_salida;
                """
        self.cursor.execute(query)
        datos = self.cursor.fetchall()
        return datos
        """for id,nombre,hora1 in datos:
            print(f"salida de {nombre}: {hora1}")

        input("Presionar enter...")"""

#Ingresamos los datos de ingreso de un empleado a la base de datos.
class InsertarIngresoAsistencia(BdInsertarIngreso):
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()
    def insertar_ingreso_empleado(self, nombre):
        
        hora = datetime.now().time().strftime('%H:%M:%S')
        datos = (nombre, hora)
        query = """INSERT INTO asistencia_ingreso (nombre, hora) VALUES (%s, %s)"""
        self.cursor.execute(query, datos)
        self.conexion.commit()
        print(f"registro de entrada de {nombre} exitoso.")

#Ingresamos los datos de salida de un empleado a la base de datos.
class InsertarSalidaAsistencia(BdInsertarSalida):
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()
    def insertar_salida_empleado(self, nombre):
        
        hora = datetime.now().time().strftime('%H:%M:%S')
        datos = (nombre, hora)
        query = """INSERT INTO asistencia_salida (nombre, hora) VALUES (%s, %s)"""
        self.cursor.execute(query, datos)
        self.conexion.commit()
        print(f"registro de salida de {nombre} exitoso.")
        


#funcion para limpiar la consola.
def limpiar_consola():
    os.system('cls')

#Instancia para conectarnos a la base de datos. (creamos objeto) le pasamos un diccionario como parametro en forma de kwargs
conn = ConectarBaseDeDatos(**configuracion)
#Llamamos al metodo conectar para establecer conexion
conexion = conn.conectar()
#Instanciamos la clase Imprimir estado para verificar que se realizo la conexion con exito.
estado = ImprimirEstado(conexion)
#Mostramos el estado en pantalla.
estado.estado()


ingresar_ingreso = InsertarIngresoAsistencia(conexion)
ingresar_salida = InsertarSalidaAsistencia(conexion)
consultar_ingreso = MostrarIngresoDeEmpleado(conexion)
consultar_salida = MostrarSalidaDeEmpleado(conexion)



