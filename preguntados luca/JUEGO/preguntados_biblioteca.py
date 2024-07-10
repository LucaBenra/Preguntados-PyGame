import pygame
from data import *
import json


#=================================FUNCIONES===========================================
#=OBTENER SUBLISTA CON LA LISTA= 
def obtener_preguntas(lista) ->list:
    """
    Itera sobre una lista de diccionarios que contiene preguntas, sus opciones y respuestas\n
    y retorna una sub_lista estructurada con estos datos\n
    
    Parametros =\n
    `lista` ( list ): Una lista de diccionarios. Caa diccionario debe contener las claves "pregunta", "a", "b", "c", y "correcta".\n
    """
    sub_lista = [] #Creo una lista vacia
    for llave in lista: #Recorro las "llaves" de la lista 
        pregunta = llave["pregunta"]  #Guardo las clves de pregunta
        opciones = [llave["a"], llave["b"], llave["c"]]  #Guardo las claves de opcion a, b, c  (opciones)
        respuesta_correcta = llave["correcta"]  #Guardo las claves de correcta (respuestas)
        lista_temp = [pregunta, opciones, respuesta_correcta]  #Creo una sublista con los datos
        sub_lista.append(lista_temp)  #Añao la lista_temp a la sublista
        
    return sub_lista #Retorna la sublista con los datos

#===================================================================================================
#=MOSTRAR LAS PREGUNTAS SEGUN EL INDICE=
def mostrar_pregunta(indice: int, fuente, ventana, opciones_eliminadas: list):
    """
    Muestra la pregunta y sus opciones en pantalla según el índice proorcionado.\n
    Las renderza como texto utilizando la fuente defnida, y las muestra en la ventana.\n
    \n
    Parámetros =\n
    `indice` (int): Índice de la pregunta dentro de la lista `lista` que se va a mostrar.\n
    `fuente` : Fuente utilizada para renderizar el texto.\n
    `ventana` : Superficie de la ventana en la que se va a mostrar el texto.\n
    `opciones_eliminadas` (list): Lista de opciones eliminadas.\n
    """
                 #(indice indica en cual pregunta se esta)
    pregunta = lista[indice]["pregunta"] # Obtiene la pregunta según el índice
    opcion_a = lista[indice]["a"] # Obtiene la opción "a" de la pregunta
    opcion_b = lista[indice]["b"] # Obtiene la opción "b" de la pregunta
    opcion_c = lista[indice]["c"] # Obtiene la opción "c" de la pregunta

    mostrar_pregunta = fuente.render(pregunta, True, (255, 255, 255)) # Renderizo la pregunta usando la fente
    ventana.blit(mostrar_pregunta, (40, 230)) #Dibuja la pregunta
    
    #   Si "a" no estan en la lista opciones_eliminadas
    if "a" not in opciones_eliminadas:
        mostrar_opcion_a = fuente.render(f"A) {opcion_a}", True, (255, 255, 255)) # Renderiza el texto de la opción a
        ventana.blit(mostrar_opcion_a, (50, 420)) # Dibuja la opción a
            
    #   Si "b" no estan el la lista opciones_eliminadas
    if "b" not in opciones_eliminadas:
        mostrar_opcion_b = fuente.render(f"B) {opcion_b}", True, (255, 255, 255)) # Renderiza el texto de la opción b
        ventana.blit(mostrar_opcion_b, (430, 420)) # Dibuja la opción b
            
        #   Si "c" no estan el la lista opciones_eliminadas
    if "c" not in opciones_eliminadas:
        mostrar_opcion_c = fuente.render(f"C) {opcion_c}", True, (255, 255, 255)) # Renderiza el texto de la opción c
        ventana.blit(mostrar_opcion_c, (795, 420)) # Dibuja la opción c
        
#==============================================================================================================================
# Función para pedir el nombre del jugador
def pedir_nombre(fuente, ventana, imagen, icono)-> str:
    """
    Crea un ventana con los parametros dados en la cual se pide al usuario\n 
    ingresar su nombre, el se retorna en str\n
    \n
    parametros =\n
    `fuente` : Fuente utilizada para renderizar el texto.\n
    `ventana` : Superficie de la ventana donde se muestra la interfaz.\n
    `imagen` : Imagen de fondo que se muestra en la ventana.\n
    `icono` : Imagen/icono secundario
    """
    #                                x, y,  ancho, alto
    rectangulo_nombre = pygame.Rect(420, 300, 300, 50) #Rectangulo donde se escribe el nombre*
    rectangulo_fondo = pygame.Rect(170, 230, 800, 200) #Rectangulo fondo
    
    nombre_ingresado = ""
    running = True

    while running == True:
        # CONTROL DE EVENTOS
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Si se cierra la pestaña
                running = False #deja de mostrar la ventana

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: #Si se apreta enter
                    if len(nombre_ingresado) > 0: #Valido que se haya ingresado almenos una letra
                        running = False #deja de mostrar la ventana
                        
            #si se apreta la tecla de borrar        
                elif event.key == pygame.K_BACKSPACE:
                    nombre_ingresado = nombre_ingresado[:-1]  #Eliminar el último carácter
                    
            #si se apreta cualquier otra    
                else:
                    if len(nombre_ingresado) < 14:
                        nombre_ingresado += event.unicode  #Agregar el carácter al texto

        
        ventana.blit(imagen, (0, 0)) #Dibuja la imagen de fondo

        #Rectangulos                 colorL
        pygame.draw.rect(ventana, (85, 8, 8), rectangulo_fondo, 0, 40, 40, 40, 40) 
        pygame.draw.rect(ventana, (255, 255, 255), rectangulo_nombre) #Se dibuja el rectangulo donde se escribe el nombre
        
        #Textos
        mensaje = fuente.render("INGRESA TU NOMBRE Y APRETA ENTER", True, (0, 0, 0)) #( texto, antialias, color )
        ventana.blit(mensaje, (220, 250)) #Dibujo el mensaje en la (Posicion*)
       
        texto_nombre = fuente.render(nombre_ingresado, True, (0, 0, 0)) #Se dibuja en la pantalla el nombre que se esta ingresando
        ventana.blit(texto_nombre, (433, 308)) #Determino las cordenadas donde se empieza a escirbir el nombre
        
        ventana.blit(icono, (210, 350)) #Icono corona
        
        pygame.display.flip() #Muestra los cambios en  la pantalla
  
    return nombre_ingresado  #retorna el nombre ingresado

#===================================================================================================

def guardar_nombre_puntaje(nombre, puntaje):
    """
    Guarda en un archivo json el nombre y puntaje obtenidos de mayor a menor.\n
    primero abre el json en modo lectura, luego agrega los nombre y puntos y los ordena con sort\n
    por ultimo escribe lo nuevos "datos" en el json y los guarda.\n
    \n
    parametros =\n
    `nombre` : nombre que se ingreso en el juego\n
    `puntaje` : puntaje obtenido en el juego  
    """
    
    nombre_json = "puntajes.json"  # Nombre del archivo JSON

    # Leo el archivo JSON existente
    with open(nombre_json, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    # Añado a datos el diccionario con el nombre y puntaje
    datos.append({"nombre": nombre, "puntaje": puntaje})
    
    # Ordeno los datos por el puntaje de mayor a menor
    datos.sort(key=lambda x: x["puntaje"], reverse=True)
    
    # Guardo los datos actualizados en el archivo JSON
    with open(nombre_json, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)

#===================================================================================================

def cargar_puntajs(nombre_archivo):
    """
    Carga los datos de un archivo json\n
    \n
    parametros =\n
    `nombre_archivo` ( str ): Nombre del JSON a cargar
    
    """
    with open(nombre_archivo, 'r') as archivo:
        datos = json.load(archivo)
    return datos

#===================================================================================================

def mostrar_puntajes(fuente_titulos, datos, ventana):
    """
    Muestra los 3 mejores puntajes uno debajo del otro de mayor a menor. itera los datos de un archivo json y va agarrando\n
    los valores de las llaves nombre y puntaje, luego se los renderiza y dibuja en la ventana.\n
    \n
    parametros =\n
    `fuente_titulos` : Fuente con la que se escribiran lo textos.\n
    `datos` : Datos donde se guardaron los nombres y puntajes\n
    `ventana` : Ventana donde se muestran los puntajes.
    """
    y = 230  # Posición inicial en Y para el primer nombre
    for jugador in datos[:3]:  # Itera solo los 3 primeros 
        nombre = jugador["nombre"]
        puntaje = jugador["puntaje"]
        
        texto_nombre = fuente_titulos.render(nombre, True, (255, 255, 255))  # Color blanco
        texto_puntaje = fuente_titulos.render(str(puntaje), True, (255, 255, 255))  # Color blanco
        
        # Dibuja el nombre y el puntaje en la ventana
        ventana.blit(texto_nombre, (270, y))
        ventana.blit(texto_puntaje, (760, y))
        
        y += 100  # Incrementa la posición Y para el siguiente nombre

    pygame.display.flip()  # Actualiza la pantalla completa






#==========================================================================================================================================================================


























































































































































































preguntas = obtener_preguntas(lista)