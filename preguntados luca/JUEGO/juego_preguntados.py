import pygame
pygame.init()  # Inicializa pygame
pygame.mixer.init() #Inicializa la mezcla de sonido

#================================= IMPORTAR FUNCIONES Y LOS DATOS ============================================================================================================================================================================
from preguntados_biblioteca import obtener_preguntas, mostrar_pregunta, pedir_nombre, guardar_nombre_puntaje, mostrar_puntajes, cargar_puntajs
from data import lista
#============================================================================================================================================================================

#==LLAMO A LA FUNCION PARA GUARDAR LOS DATOS EN LA VARIABLE==
preguntas = obtener_preguntas(lista)
#print(preguntas[0])

#============================= RECTANGULOS MENU ============================================================================================================================================================================
#                          x, y, ancho, largo
menu_jugar = pygame.Rect(428, 150, 290, 70)
menu_puntajes = pygame.Rect(428, 250, 290, 70)
menu_salir = pygame.Rect(428, 350, 290, 70)
activar_musica = pygame.Rect(5, 5, 30, 20)
desactivar_musica = pygame.Rect(40, 5, 30, 20)

#============================= RECTANGULOS PUNTAJES ============================================================================================================================================================================

boton_puntaje_volver = pygame.Rect(435, 580, 290, 70)
cuadro_puntaje = pygame.Rect(179, 120, 800, 400) 

#============================= RECTANGULOS JUGANDO ============================================================================================================================================================================

boton_pregunta = pygame.Rect(430, 32, 290, 70)
boton_reiniciar = pygame.Rect(428, 580, 290, 70)
cuadro_preguntas = pygame.Rect(0, 210, 1150, 70)
cuadro_opcion_a = pygame.Rect(37, 400, 350, 70)
cuadro_opcion_b = pygame.Rect(410, 400, 350, 70)
cuadro_opcion_c = pygame.Rect(780, 400, 350, 70)

#============================= RECTANGULOS GAME-OVER ============================================================================================================================================================================

pantalla_game_over = pygame.Rect(0, 0, 1150, 690)
boton_volver_menu = pygame.Rect(420, 300, 290, 70)

#================================ FUENTES ============================================================================================================================================================================
#                                          tamaño
fuente = pygame.font.SysFont("Arial Narrow", 50)
fuente_titulos = pygame.font.SysFont("Arial Narrow", 90)

#================================== TEXTOS MENU ============================================================================================================================================================================
#                         fuente, texto, antialias, color
texto_jugar = fuente.render("Jugar", True, (255, 255, 255))
texto_salir = fuente.render("Salir", True, (255, 255, 255))
texto_puntajes = fuente.render("Puntajes", True, (255, 255, 255)) 

#================================== TEXTOS JUGANDO ============================================================================================================================================================================

texto_pregunta = fuente.render("Pregunta", True, (255, 255, 255))
texto_reiniciar = fuente.render("Reiniciar", True, (255, 255, 255))

#=================================== TEXTOS PUNTAJES ============================================================================================================================================================================

puntaje_volver_menu = fuente.render("VOLVER", True, (255, 255, 255))
titulo = fuente_titulos.render("PUNTAJES", True, (0, 0, 0)) 
titulo_nombres = fuente_titulos.render("NOMBRES", True, (255, 255, 255))
titulo_puntajes = fuente_titulos.render("PUNTOS", True, (255, 255, 255))

#================================== TEXTOS GAME-OVER ============================================================================================================================================================================

texto_game_over = fuente.render("GAME OVER", True, (255, 0, 0))
texto_volver_menu = fuente.render("MENU", True, (255, 255, 255))

#==================================== VENTANA ============================================================================================================================================================================

resolucion = (1150, 690)
ventana = pygame.display.set_mode(resolucion) # (x,y) = resolucion
nombre_ventana = pygame.display.set_caption("Preguntados Luca") #Nombre de la ventana

#================================== IMPORTAR IMAGENES ============================================================================================================================================================================

imagen_fondo = pygame.image.load("C://CLASE PROGRAMACION//preguntados luca//imagenes//imagen_inicio.png")
imagen_fondo = pygame.transform.scale(imagen_fondo, (resolucion))

imagen_juego = pygame.image.load("C://CLASE PROGRAMACION//preguntados luca//imagenes//imagen_juego.png")
imagen_juego = pygame.transform.scale(imagen_juego, (resolucion))

imagen_ingresar_nombre = pygame.image.load("C://CLASE PROGRAMACION//preguntados luca//imagenes//imagen_ingresar_nombre.png")
imagen_ingresar_nombre = pygame.transform.scale(imagen_ingresar_nombre, (resolucion))

imagen_apagar_volumen = pygame.image.load("C://CLASE PROGRAMACION//preguntados luca//imagenes//desactivar_volumen.png")
imagen_apagar_volumen = icono = pygame.transform.scale(imagen_apagar_volumen, (20, 20))

imagen_activar_volumen = pygame.image.load("C://CLASE PROGRAMACION//preguntados luca//imagenes//activar_volumen.png")
imagen_activar_volumen = icono = pygame.transform.scale(imagen_activar_volumen, (20, 20))

icono = pygame.image.load("C://CLASE PROGRAMACION//preguntados luca//imagenes//icono2.png")
icono = pygame.transform.scale(icono, (222, 222))

#=================================== SONIDOS ============================================================================================================================================================================
#EXPORTAR MUSICA FONDO
musica_fondo = pygame.mixer.music.load("C://CLASE PROGRAMACION//preguntados luca//sonidos//musica_fondo.mp3")
musica_fondo = pygame.mixer.music.play(-1) #LOOP

#EXPORTAR SONIDO RESPUESTA CORRECTA
sonido_correcto = pygame.mixer.Sound("C://CLASE PROGRAMACION//preguntados luca//sonidos//efecto_acierto.mp3")

#EXPORTAR SONIDO RESPUESTA INCORRECTA
sonido_error = pygame.mixer.Sound("C://CLASE PROGRAMACION//preguntados luca//sonidos//efecto_error.mp3") 

#VOLUMEN DE SONIDOS
pygame.mixer.music.set_volume(0.3)
sonido_correcto.set_volume(0.3)
sonido_error.set_volume(0.3)

#===BANDERAS/INICIALIZACIONES===============================================================================================================================================================================
running = True
estado = "menu_principal" #inicializo la variable de estados
puntaje = 0 #inicializo el puntaje
respuestas_incorrectas = [] #creo lista donde se guardaran las opciones incorrectas
pregunta_indice_actual = 0 #inicializo el indice 
vidas = 2 #inicializo las vidas
nombre = "" #inicializo la variable que almacenara el nombre

#============================================================================================================================================================================
while running:  # Bucle principal del juego
    
    # =MANEJO DE EVENTOS=
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Termina el bucle principal si se cierra la ventana
        
        if event.type == pygame.MOUSEBUTTONDOWN: #detecta si se hace click
            
#============================================================================================================================================================================            
        #MENU PRINCIPAL
            if estado == "menu_principal":
                                
            #APAGAR MUSICA    
                if desactivar_musica.collidepoint(event.pos): #Si se apreta 
                    musica_fondo = pygame.mixer.music.stop() #Se apaga la musica
                                  
            #INICIAR MUSICA  
                if activar_musica.collidepoint(event.pos): #Si se apreta
                    musica_fondo = pygame.mixer.music.play(-1) #Se vuelve a escuchar la musica en bucle
                     
            #EMPEZAR A JUGAR        
                if menu_jugar.collidepoint(event.pos):
                    estado = "esperando"
                    vidas = 2  #Reinicio las vidas al empear
                    respuestas_incorrectas = [] #Reinicio la lsista de respuestas incorrectas    
            
            #PUNTAJES
                if menu_puntajes.collidepoint(event.pos):
                    estado = "puntajes" 
            
            #SALIR
                if menu_salir.collidepoint(event.pos):
                    running = False               
                    
#============================================================================================================================================================================
        #JUGANDO (SIN MOSTRAR LAS PREGUNTAS)
            if estado == "esperando":
            #SALIR    
                if event.type == pygame.QUIT:
                    running = False  # Termina el bucle principal si se cierra la venta
            
            #MOSTRAR PREGUNTAS    
                if boton_pregunta.collidepoint(event.pos): #Si se apreto el boton pregunta
                    pregunta_indice_actual += 1 #Sumo 1 al indice y empiezo a mostrar las preguntas
                    respuestas_incorrectas = [] #Vacio la lista para que se vuelva a mostrar la opcion
                    estado = "jugando" #Se muestran las preguntas
            
            #REINICIAR
                if boton_reiniciar.collidepoint(event.pos): #Si se apreta reiniciar
                    pregunta_indice_actual = 0 #Se vuelve a la primera pregunta
                    puntaje = 0 #Reinicio el puntaje
                    vidas = 2 #Reinicio las vidas
                    respuestas_incorrectas = [] #Reinicio la lista de respuestas incorrectas                            

#============================================================================================================================================================================                    
        #JUGANDO (MOSTRANDO LAS PREGUNTAS)
            if estado == "jugando":
            #SALIR    
                if event.type == pygame.QUIT:
                    running = False  # Termina el bucle principal si se cierra la venta
                
            #OPCION A    
                if cuadro_opcion_a.collidepoint(event.pos):          
                    if "a" == preguntas[pregunta_indice_actual][2]: #Si se responde correctamente
                        sonido_correcto.play() #Sonido Respuesta correcta
                        vidas = 2  #Se Reinician vidas para la siguiente pregunta
                        puntaje += 10 #El puntaje suma 10                    
                        estado = "esperando"  #Deja de mostrar la pregunta y opciones    
                #SI SE RESPONDE MAL                       
                    else: 
                        vidas -= 1 #Se resta una vida
                        sonido_error.play() #Sonido respuesta incorrecta
                        respuestas_incorrectas.append("a") #Se agrega la opcion elegida a la lista (se deja de mostrar) con append
                    #SI SE PIERDE    
                        if vidas == 0:
                            nombre = pedir_nombre(fuente, ventana, imagen_ingresar_nombre, icono) #Si se pierde se pide el nombre
                            guardar_nombre_puntaje(nombre, puntaje) #Se guarda el nombre pedido
                            estado = "game_over" #Muestra la pantalla de game-over           
            #OPCION B
                elif cuadro_opcion_b.collidepoint(event.pos):            
                    if "b" == preguntas[pregunta_indice_actual][2]:
                        sonido_correcto.play() #Sonido Respuesta correcta
                        vidas = 2  #Se Reinician vidas para la siguiente pregunta
                        puntaje += 10 #El puntaje suma 10 
                        estado = "esperando" #Deja de mostrar la pregunta y opciones
                #SI SE RESPONDE MAL       
                    else: 
                        vidas -= 1 #Se resta una vida
                        sonido_error.play() #Sonido respuesta incorrecta
                        respuestas_incorrectas.append("b") #Se agrega la opcion elegida a la lista (se deja de mostrar) con append
                    #SI SE PIERDE    
                        if vidas == 0: #Si vidas llega a 0
                            nombre = pedir_nombre(fuente, ventana, imagen_ingresar_nombre, icono)
                            guardar_nombre_puntaje(nombre, puntaje) #Se guarda el nombre pedido
                            estado = "game_over" #Muestra la pantalla de game-over           
            #OPCION C
                elif cuadro_opcion_c.collidepoint(event.pos):
                    if "c" == preguntas[pregunta_indice_actual][2]:
                        sonido_correcto.play() #Sonido Respuesta correcta
                        vidas = 2  #Se Reinician vidas para la siguiente pregunta
                        puntaje += 10#El puntaje suma 10
                        estado = "esperando" #Deja de mostrar la pregunta y opciones
                #SI SE RESPONDE MAL        
                    else: 
                        vidas -= 1 #Se resta una vida
                        sonido_error.play() #Sonido respuesta incorrecta
                        respuestas_incorrectas.append("c") #Se agrega la opcion elegida a la lista (se deja de mostrar) con append
                    #SI SE PIERDE    
                        if vidas == 0: #Si vidas llega a 0
                            nombre = pedir_nombre(fuente, ventana, imagen_ingresar_nombre, icono) #Si se pierde se pide el nombre
                            guardar_nombre_puntaje(nombre, puntaje) #Se guarda el nombre pedido
                            estado = "game_over" #Muestra la pantalla de game-over 
                            
            #SI SE GANA SE PIDE EL NOMBRE Y MUESTRA LA PANTALLA GAME-OVER
                if puntaje >= 170: #Si puntaje es 170
                    nombre = pedir_nombre(fuente, ventana, imagen_ingresar_nombre, icono) #Muestro la pantalla pedir nombre
                    guardar_nombre_puntaje(nombre, puntaje) #Guardo el nombre
                    estado = "game_over" #Muestro la pantalla game over                  
            
            #REINICIAR
                if boton_reiniciar.collidepoint(event.pos): #Si se apreta reiniciar
                    pregunta_indice_actual = 1 #Se vuelve a la primera pregunta
                    puntaje = 0 #Reinicio el puntaje
                    vidas = 2 #Reinicio las vidas
                    respuestas_incorrectas = [] #Reinicio la lista de respuestas incorrectas

#============================================================================================================================================================================        
        #GAME-OVER    
            if estado == "game_over":
            #SALIR    
                if event.type == pygame.QUIT:
                    running = False  # Termina el bucle principal si se cierra la venta
                    
                if boton_volver_menu.collidepoint(event.pos): #SI se apreta volver
                    estado = "menu_principal" #Se regresa al menu    
                      
#============================================================================================================================================================================
        #PUNTAJES
            if estado == "puntajes":       
            #SALIR    
                if event.type == pygame.QUIT:
                    running = False  # Termina el bucle principal si se cierra la venta
                        
                if boton_puntaje_volver.collidepoint(event.pos): #SI se apreta volver
                    estado = "menu_principal" #Se regresa al menu
                    
#============================================================================================================================================================================
#MENU PRINCIPAL
    if estado == "menu_principal":
            
        ventana.blit(imagen_fondo, (0, 0))  #Dibuja la imagen de fondo             
        pygame.draw.rect(ventana, (50, 49, 77), activar_musica, border_radius=15)  #Dibuja el rectángulo de activar musica
        pygame.draw.rect(ventana, (50, 49, 77), desactivar_musica, border_radius=15)  # Dibuja el rectángulo de desactivar musica
        pygame.draw.rect(ventana, (50, 49, 77), menu_jugar, border_radius=15)  # Dibuja el rectángulo de Jugar
        pygame.draw.rect(ventana, (50, 49, 77), menu_puntajes, border_radius=15)  # Dibuja el rectángulo de puntajes
        pygame.draw.rect(ventana, (50, 49, 77), menu_salir, border_radius=15)  # Dibuja el rectángulo de Salir
        
        ventana.blit(texto_jugar, (525, 170))  # Dibuja el texto de Jugar              
        ventana.blit(texto_salir, (535, 370))  # Dibuja el texto de Salir          
        ventana.blit(texto_puntajes, (508, 270))  # Dibuja el texto puntajes
        ventana.blit(imagen_activar_volumen, (8, 5)) #Dibja la imagen activar volumen      
        ventana.blit(imagen_apagar_volumen, (38, 5)) #Dibuja la imagen desactivar volumen
        
#============================================================================================================================================================================
#ESPERANDO
    if estado == "esperando":
        
        ventana.blit(imagen_juego, (0, 0)) #Dibuja la imagen de fondo      
        pygame.draw.rect(ventana, (7, 13, 55), boton_pregunta, border_radius=15) #Dibuja el rectangulo del boton pregunta
        pygame.draw.rect(ventana, (7, 13, 55), cuadro_preguntas, border_radius=15) #Se dibuja el rectangulo donde se veran las preguntas
        pygame.draw.rect(ventana, (7, 13, 55), cuadro_opcion_a, border_radius=15) #Se dibuja el cuadro donde se vera la opcion A
        pygame.draw.rect(ventana, (7, 13, 55), cuadro_opcion_b, border_radius=15) #Se dibuja el cuadro donde se vera la opcion B
        pygame.draw.rect(ventana, (7, 13, 55), cuadro_opcion_c, border_radius=15) #Se dibuja el cuadro donde se vera la opcion C
        pygame.draw.rect(ventana, (7, 13, 55), boton_reiniciar, border_radius=15) #Dibuja el rectangulo reiniciar
        
        ventana.blit(texto_pregunta, (505, 50)) #Dibuja el texto de pregunta      
        ventana.blit(texto_reiniciar, (500, 600)) #Dibuja el texto de reiniciar   
        
#   ARMO EL PUNTAJE ---> casteo la variable puntaje a str (para poder mostrarlo) y con el metodo zfill agrego ceros a la izquierda 

#                                                             cuantos 0,  antialias, color                    
        texto_puntaje = fuente.render(f"Puntaje: {str(puntaje).zfill(3)}", True, (255, 255, 255))       
        ventana.blit(texto_puntaje, (850, 50)) #Se dibuja el puntaje
        
#============================================================================================================================================================================        
#JUGANDO
    if estado == "jugando":
        
        ventana.blit(imagen_juego, (0, 0)) #Dibuja la imagen de fondo      
        pygame.draw.rect(ventana, (7, 13, 55), boton_pregunta, border_radius=15) #Dibuja el rectangulo del boton pregunta
        pygame.draw.rect(ventana, (7, 13, 55), cuadro_preguntas, border_radius=15) #Se dibuja el rectangulo donde se veran las preguntas
        pygame.draw.rect(ventana, (7, 13, 55), cuadro_opcion_a, border_radius=15) #Se dibuja el cuadro donde se vera la opcion A
        pygame.draw.rect(ventana, (7, 13, 55), cuadro_opcion_b, border_radius=15) #Se dibuja el cuadro donde se vera la opcion B
        pygame.draw.rect(ventana, (7, 13, 55), cuadro_opcion_c, border_radius=15) #Se dibuja el cuadro donde se vera la opcion C
        pygame.draw.rect(ventana, (7, 13, 55), boton_reiniciar, border_radius=15) #Dibuja el rectangulo reiniciar
        
        ventana.blit(texto_pregunta, (505, 50)) #Dibuja el texto de pregunta      
        ventana.blit(texto_reiniciar, (500, 600)) #Dibuja el texto de reiniciar   
        
#   ARMO EL PUNTAJE ---> casteo la variable puntaje a str (para poder mostrarlo) y con el metodo zfill agrego ceros a la izquierda 

#                                                             cuantos 0,  antialias, color                    
        texto_puntaje = fuente.render(f"Puntaje: {str(puntaje).zfill(3)}", True, (255, 255, 255))       
        ventana.blit(texto_puntaje, (850, 50)) #Se dibuja el puntaje
        
        #LLAMO A LA FUNCION Y EMPIEZO A MOSTAR LAS PREGUNTAS SEGUN EL INDICE   
        mostrar_pregunta(pregunta_indice_actual, fuente, ventana, respuestas_incorrectas)    

#============================================================================================================================================================================   
#GAME-OVER        
    if estado == "game_over":
        ventana.fill((13, 114, 105)) #Se pinta la ventana      
        pygame.draw.rect(ventana, (50, 49, 77), boton_volver_menu, border_radius=15) # Dibuja el botón Volver al Menú
        
        ventana.blit(texto_game_over, (460, 250)) # Muestra el texto de Game Over      
        ventana.blit(texto_volver_menu, (515, 320)) # Muestra el texto del botón        

#============================================================================================================================================================================        
#PUNTAJES
    if estado == "puntajes":
        ventana.fill((255, 255, 255))  #pinta la ventana       
        pygame.draw.rect(ventana, (50, 49, 77), boton_puntaje_volver, border_radius=15) # Dibuja el botón Volver al Menú
        pygame.draw.rect(ventana, (7, 13, 55), cuadro_puntaje, border_radius=15) #Rectangulo fondo     
           
        ventana.blit(puntaje_volver_menu, (515, 600)) # Muestra el texto del botón volver
        ventana.blit(titulo, (420, 20)) # Muestra el texto de Game Over
        ventana.blit(titulo_nombres, (200, 140)) # Muestra el texto de Game Over
        ventana.blit(titulo_puntajes, (660, 140)) # Muestra el texto de Game Over    
        
        mostrar_puntajes(fuente_titulos, cargar_puntajs("puntajes.json"), ventana)   #Se llama la funcion y muestro los puntajes       
        
#============================================================================================================================================================================
    
    pygame.display.flip()  # Actualiza los cambios en la pantalla 

pygame.quit()  # Fin

#============================================================================================================================================================================                      