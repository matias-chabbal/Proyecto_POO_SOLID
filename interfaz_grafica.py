import tkinter as tk
import ejercicio_final_poo as bd_programa


def asistencia_ingreso():
    nombre = entrada_registrar_entrada.get()
    
    if nombre.isspace() or nombre == "":
        print("esta vacio")
    else:
        bd_programa.ingresar_ingreso.insertar_ingreso_empleado(nombre)
        entrada_registrar_entrada.delete(0, tk.END)
        print(nombre)

def asistencia_salida():
    nombre = entrada_registrar_salida.get()
    
    if nombre.isspace() or nombre == "":
        print("esta vacio")
    else:
        bd_programa.ingresar_salida.insertar_salida_empleado(nombre)
        entrada_registrar_salida.delete(0, tk.END)
        print(nombre)



color_fondo = "sandybrown"
# crear la ventana principal.
app = tk.Tk()
app.title("Registro de Asistencia Empleados")
app.geometry("700x600+10+10")
app.configure(bg=color_fondo)
#configurar la cuadricula de la ventana para que las filas y columnas tengan peso.
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=2)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

#crear widgets o frames para la primera fila(1 columna)

frame1_col1 = tk.Frame(app, bg=color_fondo)

frame1_col1.grid(row=0, column=0, columnspan=2, sticky="nsew", padx= 5, pady=5)


#crear widgets o frames para la segunda fila(1 columna)
#campos para registrar entrada de un empleado.
etiqueta_registrar_entrada = tk.Label(frame1_col1, text= "Registrar ingreso empleado: ")
etiqueta_registrar_entrada.grid(row=0,column=0, padx=20,pady=50)

entrada_registrar_entrada = tk.Entry(frame1_col1)
entrada_registrar_entrada.grid(row=0, column=1)

boton_registrar_entrada = tk.Button(frame1_col1, text="Cargar", command=asistencia_ingreso)
boton_registrar_entrada.grid(row=0,column=2, padx=10)

#crear widgets o frames para la segunda fila(1 columna)
#campos para registrar salida de un empleado.
etiqueta_registrar_salida = tk.Label(frame1_col1, text= "Registrar Salida empleado: ")
etiqueta_registrar_salida.grid(row=1,column=0, padx=0,pady=10)

entrada_registrar_salida = tk.Entry(frame1_col1)
entrada_registrar_salida.grid(row=1, column=1)

boton_registrar_salida = tk.Button(frame1_col1, text="Cargar", command=asistencia_salida)
boton_registrar_salida.grid(row=1,column=2, padx=10)

# frame 2
frame2_col1 = tk.Frame(app, bg=color_fondo)
frame2_col1.grid(row=1, column=0, columnspan=2, sticky="nsew", padx= 5, pady=5)

lista_resultados = tk.Listbox(frame2_col1, width=60, height=20,bg="white",fg="black")
lista_resultados.grid(row=0,column=0,padx=20,pady=10)

scrollbar = tk.Scrollbar(frame2_col1, orient=tk.VERTICAL, command=lista_resultados.yview)
scrollbar.grid(row=0, column=1)

lista_resultados.config(yscrollcommand=scrollbar.set)

def listar_empleados():
    lista_completa_entrada = bd_programa.consultar_ingreso.consultar_ingreso_de_empleado()
    lista_completa_salida = bd_programa.consultar_salida.consultar_salida_de_empleado()
    lista_resultados.delete(0, tk.END)
    lista_resultados.insert(tk.END, f" ID       |      NOMBRE       |     HORA ENTRADA     |      HORA SALIDA ")
    lista_resultados.insert(tk.END, f"________________________________________________________________________")
    print(len(lista_completa_entrada))
    print(len(lista_completa_salida))
    if len(lista_completa_entrada) != len(lista_completa_salida):
            lista_completa_salida.append(("---","---","---"))
    print(lista_completa_salida)
    for (id_entrada,nombre_entrada,hora_entrada),(id_salida,nombre_salida,hora_salida) in zip(lista_completa_entrada,lista_completa_salida):
        lista_resultados.insert(tk.END, f"  {id_entrada}                {nombre_entrada}                    {hora_entrada}                            {hora_salida}")



boton_listar = tk.Button(frame2_col1, text="Listar Resultados", command=listar_empleados)
boton_listar.grid(row=1,column=0)

# ejecutar el bucle principal de la aplicacion.
app.mainloop()