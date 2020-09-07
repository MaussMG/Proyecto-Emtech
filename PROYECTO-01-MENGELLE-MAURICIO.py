# -*- coding: utf-8 -*-
"""
@author: Mauricio Mengelle
"""


#from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches

import lifestore_file as lifestore
lifestore_products=lifestore.lifestore_products

##Substraemos por categorias    
categorias_existentes=[]

for producto in lifestore_products:
       if producto[3] not in categorias_existentes:
           categorias_existentes.append(producto[3])
           
           
#Ahora si podemos ver cuantas y cuales categorias existen:

#print("Estas son las CATEGORIAS: ",categorias_existentes)
#print("\nEste es el NUMERO DE CATEGROIAS: ", len(categorias_existentes))



#Se hace una copia de la lista de productos de la tienda
productos_tienda=[]
productos_tienda=lifestore_products[:].copy()


#productos_tienda = [id_producto, nombre, precio, categoria, stock,numero_ventas,numero_devoluciones]

for producto in productos_tienda:
    numero_ventas=0
    numero_devoluciones=0
    id_producto=producto[0]
    for venta in lifestore_sales:
        if id_producto==venta[1]:
           if venta[4]==0:
            numero_ventas+=1
           else:
            numero_devoluciones+=1
    producto.append(numero_ventas)
    producto.append(numero_devoluciones)

#productos_tienda = [id_producto, nombre, precio, categoria, stock,numero_ventas,numero_devoluciones,
#                    num_busquedas]
    
for producto in productos_tienda:
    numero_busquedas=0
    id_producto=producto[0]
    for busqueda in lifestore_searches:
        if id_producto==busqueda[1]:
            numero_busquedas+=1
    producto.append(numero_busquedas)
    
 
#Creamos una lista de listas de la forma
# [id_producto,nombre,numero de reseñas, promedio,num_devoluciones]    
productos_reseña=[]
for producto in productos_tienda:
    reseña=0
    id_producto=producto[0]
    num_reseñas=0
    num_devoluciones=0
    for ventas in lifestore_sales:
        if id_producto==ventas[1]:
            reseña += ventas[2]
            num_reseñas += 1
            if ventas[4]==1:
                num_devoluciones+=1
    if num_reseñas>0:        
        promedio_reseña=reseña/num_reseñas        
        productos_reseña.append([id_producto,producto[1],num_reseñas,promedio_reseña,num_devoluciones])   
    else:
        productos_reseña.append([id_producto,producto[1],0,0,num_devoluciones]) 
            

promedio_reseña=[]    
for producto in productos_reseña:
    if(producto[3]>0):
        promedio_reseña.append(producto[3])
    
promedio_reseña.sort(reverse=True)

productos_ordenados_reseña=[]

for num in promedio_reseña:
    for producto in productos_reseña:
        if producto[3]==num:
            if producto not in productos_ordenados_reseña:
                productos_ordenados_reseña.append(producto)



#Ahora tenemos que disgregar los productos por categorias
productos_procesador=[]
productos_t_video=[]
productos_t_madre=[]
productos_disco_duro=[]
productos_usb=[]
productos_pantalla=[]
productos_bocina=[]
productos_audifono=[]


#Para los procesadores
for producto in productos_tienda:
    if producto[3] == categorias_existentes[0]:
        productos_procesador.append(producto)

#Para las tarejtas de video
for producto in productos_tienda:
    if producto[3] == categorias_existentes[1]:
        productos_t_video.append(producto)

#Para las tarjetas madre
for producto in productos_tienda:
    if producto[3] == categorias_existentes[2]:
        productos_t_madre.append(producto)

#Para discos duros
for producto in productos_tienda:
    if producto[3] == categorias_existentes[3]:
        productos_disco_duro.append(producto)

#Para Usb
for producto in productos_tienda:
    if producto[3] == categorias_existentes[4]:
        productos_usb.append(producto)

#Para Pantallas
for producto in productos_tienda:
    if producto[3] == categorias_existentes[5]:
        productos_pantalla.append(producto)
        
#Para bocinas
for producto in productos_tienda:
    if producto[3] == categorias_existentes[6]:
        productos_bocina.append(producto)

#Para audifonos
for producto in productos_tienda:
    if producto[3] == categorias_existentes[7]:
        productos_audifono.append(producto)

########################################################################

#Tenemos que ordenar los productos por categoria
        
#PROCESADORES
numero_ventas=[]    
for producto in productos_procesador:
    numero_ventas.append(producto[5])
    
numero_ventas.sort(reverse=True)

x_procesador_ordenado_ventas=[]

for num in numero_ventas:
    for producto in productos_procesador:
        if producto[5]==num:
            if producto not in x_procesador_ordenado_ventas:
                x_procesador_ordenado_ventas.append(producto)
                
############                
numero_busquedas=[]    

for producto in productos_procesador:
    numero_busquedas.append(producto[7])
    
numero_busquedas.sort(reverse=True)

busq_procesador_ordenado=[]

for num in numero_busquedas:
    for producto in productos_procesador:
        if producto[7]==num:
            if producto not in busq_procesador_ordenado:
                busq_procesador_ordenado.append(producto)
                
#TARJETA DE VIDEO
numero_ventas=[]    
for producto in productos_t_video:
    numero_ventas.append(producto[5])
    
numero_ventas.sort(reverse=True)

x_t_video_ordenado_ventas=[]

for num in numero_ventas:
    for producto in productos_t_video:
        if producto[5]==num:
            if producto not in x_t_video_ordenado_ventas:
                x_t_video_ordenado_ventas.append(producto)
                
############                
numero_busquedas=[]    

for producto in productos_t_video:
    numero_busquedas.append(producto[7])
    
numero_busquedas.sort(reverse=True)

busq_t_video_ordenado=[]

for num in numero_busquedas:
    for producto in productos_t_video:
        if producto[7]==num:
            if producto not in busq_t_video_ordenado:
                busq_t_video_ordenado.append(producto)                


#TARJETA MADRE
numero_ventas=[]    
for producto in productos_t_madre:
    numero_ventas.append(producto[5])
    
numero_ventas.sort(reverse=True)

x_t_madre_ordenado_ventas=[]

for num in numero_ventas:
    for producto in productos_t_madre:
        if producto[5]==num:
            if producto not in x_t_madre_ordenado_ventas:
                x_t_madre_ordenado_ventas.append(producto)
                
############                
numero_busquedas=[]    

for producto in productos_t_madre:
    numero_busquedas.append(producto[7])
    
numero_busquedas.sort(reverse=True)

busq_t_madre_ordenado=[]

for num in numero_busquedas:
    for producto in productos_t_madre:
        if producto[7]==num:
            if producto not in busq_t_madre_ordenado:
                busq_t_madre_ordenado.append(producto)    
          
#Discos DUROS
numero_ventas=[]    
for producto in productos_disco_duro:
    numero_ventas.append(producto[5])
    
numero_ventas.sort(reverse=True)

x_disco_duro_ordenado_ventas=[]

for num in numero_ventas:
    for producto in productos_disco_duro:
        if producto[5]==num:
            if producto not in x_disco_duro_ordenado_ventas:
                x_disco_duro_ordenado_ventas.append(producto)
            
############                
numero_busquedas=[]    

for producto in productos_disco_duro:
    numero_busquedas.append(producto[7])
    
numero_busquedas.sort(reverse=True)

busq_disco_duro_ordenado=[]

for num in numero_busquedas:
    for producto in productos_disco_duro:
        if producto[7]==num:
            if producto not in busq_disco_duro_ordenado:
                busq_disco_duro_ordenado.append(producto)  

#Memorias usb
numero_ventas=[]    
for producto in productos_usb:
    numero_ventas.append(producto[5])
    
numero_ventas.sort(reverse=True)

x_usb_ordenado_ventas=[]

for num in numero_ventas:
    for producto in productos_usb:
        if producto[5]==num:
            if producto not in x_usb_ordenado_ventas:
                x_usb_ordenado_ventas.append(producto)
         
############                
numero_busquedas=[]    

for producto in productos_usb:
    numero_busquedas.append(producto[7])
    
numero_busquedas.sort(reverse=True)

busq_usb_ordenado=[]

for num in numero_busquedas:
    for producto in productos_usb:
        if producto[7]==num:
            if producto not in busq_usb_ordenado:
                busq_usb_ordenado.append(producto)          
        
#Pantallas
numero_ventas=[]    
for producto in productos_pantalla:
    numero_ventas.append(producto[5])
    
numero_ventas.sort(reverse=True)

x_pantalla_ordenado_ventas=[]

for num in numero_ventas:
    for producto in productos_pantalla:
        if producto[5]==num:
            if producto not in x_pantalla_ordenado_ventas:
                x_pantalla_ordenado_ventas.append(producto)

############                
numero_busquedas=[]    

for producto in productos_pantalla:
    numero_busquedas.append(producto[7])
    
numero_busquedas.sort(reverse=True)

busq_pantalla_ordenado=[]

for num in numero_busquedas:
    for producto in productos_pantalla:
        if producto[7]==num:
            if producto not in busq_pantalla_ordenado:
                busq_pantalla_ordenado.append(producto)          
        
#Bocinas
numero_ventas=[]    
for producto in productos_bocina:
    numero_ventas.append(producto[5])
    
numero_ventas.sort(reverse=True)

x_bocina_ordenado_ventas=[]

for num in numero_ventas:
    for producto in productos_bocina:
        if producto[5]==num:
            if producto not in x_bocina_ordenado_ventas:
                x_bocina_ordenado_ventas.append(producto)
        
############                
numero_busquedas=[]    

for producto in productos_bocina:
    numero_busquedas.append(producto[7])
    
numero_busquedas.sort(reverse=True)

busq_bocina_ordenado=[]

for num in numero_busquedas:
    for producto in productos_bocina:
        if producto[7]==num:
            if producto not in busq_bocina_ordenado:
                busq_bocina_ordenado.append(producto)  

#Audifonos
numero_ventas=[]    
for producto in productos_audifono:
    numero_ventas.append(producto[5])
    
numero_ventas.sort(reverse=True)

x_audifono_ordenado_ventas=[]

for num in numero_ventas:
    for producto in productos_audifono:
        if producto[5]==num:
            if producto not in x_audifono_ordenado_ventas:
                x_audifono_ordenado_ventas.append(producto)

############                
numero_busquedas=[]    

for producto in productos_audifono:
    numero_busquedas.append(producto[7])
    
numero_busquedas.sort(reverse=True)

busq_audifono_ordenado=[]

for num in numero_busquedas:
    for producto in productos_audifono:
        if producto[7]==num:
            if producto not in busq_audifono_ordenado:
                busq_audifono_ordenado.append(producto) 

#Incluyendo a TODOS los productos por venta
numero_ventas=[]    
for producto in productos_tienda:
    numero_ventas.append(producto[5])
    
numero_ventas.sort(reverse=True)
              
x_todos_ordenado_ventas=[]

for num in numero_ventas:
    for producto in productos_tienda:
        if producto[5]==num:
            if producto not in x_todos_ordenado_ventas:
                x_todos_ordenado_ventas.append(producto)
              
#Incluyendo a TODOS por busqueda
numero_busquedas=[]    
for producto in productos_tienda:
    numero_busquedas.append(producto[7])
    
numero_busquedas.sort(reverse=True)
              
busq_todos_ordenado=[]

for num in numero_busquedas:
    for producto in productos_tienda:
        if producto[7]==num:
            if producto not in busq_todos_ordenado:
                busq_todos_ordenado.append(producto)

#####################
            

################################# Aquí esta el código de inicio de sesión:

# ["Usuario", contrasenia""]
lista_usuarios =  [["Admin","el_pro"],["usuario1","python"]]

print("\n Es un EXCELENTE día para iniciar sesión")

ingreso=False
intentos=0

while ingreso==False:
    
    print("******************** BIENVENIDO a LIFESTORE MÉXICO *********************")
    print("\n********************* INICIO DE SESION *********************")
    input_usuario= input("Por favor escriba a continuación el nombre de USUSARIO: ")
    input_contrasenia= input("Ahora escriba gentilmente la CONTRASEÑA: ")
    
    for usuario in lista_usuarios:
        if usuario[0]==input_usuario and usuario[1]==input_contrasenia:
            ingreso= True
            break
    if ingreso==True:
        print("\nEs INCREIBLE que este por aquí "+input_usuario)
    else:
        intentos+=1
        print("\n       ¡Oh oh! Parece que hubo un error al ingresar sus credenciales")
        print("\n       ¿Desea poder crear un NUEVO usuario?")
        crear=input("Escriba 'si' en caso de querer crear un nuevo usuario, en caso contrario escriba cualquier otra cosa o de enter : ").lower()
        
        if crear=="si":
            
            creado_exitoso=False
            
            while creado_exitoso==False:
                print("\n********************* CREACION DE USUARIO NUEVO *********************")
                nuevo_usuario=input("Ingrese su FABULOSO nombre de usuario:")
                
                bandera= True
                for usuario in lista_usuarios:
                    if usuario[0]==nuevo_usuario:
                        print("\nLo sentimos, ese ususario ya existe, debe escribir uno DIFERENTE, por favor")
                        bandera=False
                
                if bandera==True:     
                    nueva_contrasenia=input("Ingrese su secreta contraseña:")
                    lista_usuarios.append([nuevo_usuario,nueva_contrasenia])
                    print("\nUsuario creado EXITOSAMENTE")
                    print("Momento de escribir sus credenciales recien creadas.")
                    creado_exitoso=True
                    break
        else:
            print("\nOkey, intentelo otra vez")
            
print("\n********************* SESION ACTIVA *********************")

salir=False

while salir==False:
    if input_usuario=="Admin":
        print("\n¿Que es lo que desea hacer "+input_usuario+" ?\n")
        print("1. Ver datos importantes por categoria de los productos")
        print("2. Ver el top productos de MAYOR ventas sin importar categoria")
        print("3. Ver el top productos de MAYOR busquedas sin importar categoria")
        print("4. Ver el top 20 productos con MEJOR reseñas")
        print("5. Ver el top 20 productos de PEOR reseña")
        print("6. Salir")
        respuesta= input("Ingrese el numero de su interes: ")

        if respuesta=='1':
            salir_1=False
            while  salir_1==False:
            
                  print("\n¿Que es lo que desea ver por categoria?\n")
                  print("1. Ver top mayores productos VENDIDOS por categoria")
                  print("2. Ver top menores productos VENDIDOS por categoria")
                  print("3. Ver top mayores productos BUSCADOS por categoria")
                  print("4. Ver top menores productos BUSCADOS por categoria")
                  print("5. Salir de esta seccion")
                  n_respuesta=input("Ingrese el numero que le interesa: ")
                      
                  if n_respuesta=='1':
                          print("\nLas categorias son:")
                          n=1
                          for cat in categorias_existentes:
                                  print(n," ", cat)
                                  n+=1
                          cual_categoria= input("\n¿De cual GRANDIOSA categoria quiere ver el top MAYOR ventas?: ")
                          
                          flag=False
                          
                          if cual_categoria=='1':
                                  
                                  print("\nExisten ",len(x_procesador_ordenado_ventas), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=1
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de ventas, Nombre_producto")
                                  print("\nProcesadores: ")
                                  for producto in x_procesador_ordenado_ventas[0:(top_n)]:
                                          print(n,", ",producto[5],", ",producto[1])
                                          n=n+1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                          
                          elif cual_categoria=='2':        
                                  
                                  print("\nExisten ",len(x_t_video_ordenado_ventas), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=1
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de ventas, Nombre_producto")
                                  print("\nTarjetas de video: ")
                                  for producto in x_t_video_ordenado_ventas[0:(top_n)]:
                                          print(n,", ",producto[5],", ",producto[1])
                                          n=n+1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='3':        
                                  
                                  print("\nExisten ",len(x_t_madre_ordenado_ventas), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=1
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de ventas, Nombre_producto")
                                  print("\nTarjetas madre: ")
                                  for producto in x_t_madre_ordenado_ventas[0:(top_n)]:
                                          print(n,", ",producto[5],", ",producto[1])
                                          n=n+1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='4':        
                               
                                  print("\nExisten ",len(x_disco_duro_ordenado_ventas), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=1
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de ventas, Nombre_producto")
                                  print("\nDiscos duro: ")
                                  for producto in x_disco_duro_ordenado_ventas[0:(top_n)]:
                                          print(n,", ",producto[5],", ",producto[1])
                                          n=n+1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='5':        
                              
                                  print("\nExisten ",len(x_usb_ordenado_ventas), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=1
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de ventas, Nombre_producto")
                                  print("\nUSB: ")
                                  for producto in x_usb_ordenado_ventas[0:(top_n)]:
                                          print(n,", ",producto[5],", ",producto[1])
                                          n=n+1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='6':        
                              
                                  print("\nExisten ",len(x_pantalla_ordenado_ventas), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=1
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de ventas, Nombre_producto")
                                  print("\nPantallas: ")
                                  for producto in x_pantalla_ordenado_ventas[0:(top_n)]:
                                          print(n,", ",producto[5],", ",producto[1])
                                          n=n+1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='7':        
                              
                                  print("\nExisten ",len(x_bocina_ordenado_ventas), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=1
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de ventas, Nombre_producto")
                                  print("\nBocinas: ")
                                  for producto in x_bocina_ordenado_ventas[0:(top_n)]:
                                          print(n,", ",producto[5],", ",producto[1])
                                          n=n+1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='8':        
                              
                                  print("\nExisten ",len(x_audifono_ordenado_ventas), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=1
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de ventas, Nombre_producto")
                                  print("\Audifonos: ")
                                  for producto in x_audifono_ordenado_ventas[0:(top_n)]:
                                          print(n,", ",producto[5],", ",producto[1])
                                          n=n+1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          else:
                              print("Ingrese una opcion valida por favor")
                          
                  elif n_respuesta=='2':
                          print("\nLas categorias son:")
                          n=1
                          for cat in categorias_existentes:
                                  print(n," ", cat)
                                  n+=1
                          cual_categoria= input("\n¿De cual GRANDIOSA categoria quiere ver el top MENOS ventas?: ")
                          
                          flag=False
                          
                          if cual_categoria=='1':
                                  
                                  print("\nExisten ",len(x_procesador_ordenado_ventas), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=top_n
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de ventas, Nombre_producto")
                                  print("\nProcesadores: ")
                                  for producto in x_procesador_ordenado_ventas[-(top_n):]:
                                          print(n,", ",producto[5],", ",producto[1])
                                          n=n-1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                          
                          elif cual_categoria=='2':        
                                  
                                  print("\nExisten ",len(x_t_video_ordenado_ventas), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=top_n
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de ventas, Nombre_producto")
                                  print("\nTarjetas de video: ")
                                  for producto in x_t_video_ordenado_ventas[-(top_n):]:
                                          print(n,", ",producto[5],", ",producto[1])
                                          n=n-1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='3':        
                                  
                                  print("\nExisten ",len(x_t_madre_ordenado_ventas), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=top_n
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de ventas, Nombre_producto")
                                  print("\nTarjetas madre: ")
                                  for producto in x_t_madre_ordenado_ventas[-(top_n):]:
                                          print(n,", ",producto[5],", ",producto[1])
                                          n=n-1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='4':        
                               
                                  print("\nExisten ",len(x_disco_duro_ordenado_ventas), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=top_n
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de ventas, Nombre_producto")
                                  print("\nDiscos duro: ")
                                  for producto in x_disco_duro_ordenado_ventas[-(top_n):]:
                                          print(n,", ",producto[5],", ",producto[1])
                                          n=n-1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='5':        
                              
                                  print("\nExisten ",len(x_usb_ordenado_ventas), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=top_n
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de ventas, Nombre_producto")
                                  print("\nUSB: ")
                                  for producto in x_usb_ordenado_ventas[-(top_n):]:
                                          print(n,", ",producto[5],", ",producto[1])
                                          n=n-1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='6':        
                              
                                  print("\nExisten ",len(x_pantalla_ordenado_ventas), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=top_n
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de ventas, Nombre_producto")
                                  print("\nPantallas: ")
                                  for producto in x_pantalla_ordenado_ventas[-(top_n):]:
                                          print(n,", ",producto[5],", ",producto[1])
                                          n=n-1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='7':        
                              
                                  print("\nExisten ",len(x_bocina_ordenado_ventas), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=top_n
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de ventas, Nombre_producto")
                                  print("\nBocinas: ")
                                  for producto in x_bocina_ordenado_ventas[-(top_n):]:
                                          print(n,", ",producto[5],", ",producto[1])
                                          n=n-1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='8':        
                              
                                  print("\nExisten ",len(x_audifono_ordenado_ventas), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=top_n
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de ventas, Nombre_producto")
                                  print("\Audifonos: ")
                                  for producto in x_audifono_ordenado_ventas[-(top_n):]:
                                          print(n,", ",producto[5],", ",producto[1])
                                          n=n-1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          else:
                              print("Ingrese una opcion valida por favor")
                  
                  elif n_respuesta=='3':
                          print("\nLas categorias son:")
                          n=1
                          for cat in categorias_existentes:
                                  print(n," ", cat)
                                  n+=1
                          cual_categoria= input("\n¿De cual GRANDIOSA categoria quiere ver el top MAYOR BUSQUEDAS?: ")
                          
                          flag=False
                          
                          if cual_categoria=='1':
                                  
                                  print("\nExisten ",len(busq_procesador_ordenado), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=1
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de busquedas, Nombre_producto")
                                  print("\nProcesadores: ")
                                  for producto in busq_procesador_ordenado[0:(top_n)]:
                                          print(n,", ",producto[7],", ",producto[1])
                                          n=n+1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                          
                          elif cual_categoria=='2':        
                                  
                                  print("\nExisten ",len(busq_t_video_ordenado), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=1
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de busquedas, Nombre_producto")
                                  print("\nProcesadores: ")
                                  for producto in busq_t_video_ordenado[0:(top_n)]:
                                          print(n,", ",producto[7],", ",producto[1])
                                          n=n+1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='3':        
                                  
                                  print("\nExisten ",len(busq_t_madre_ordenado), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=1
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de busquedas, Nombre_producto")
                                  print("\nProcesadores: ")
                                  for producto in busq_t_madre_ordenado[0:(top_n)]:
                                          print(n,", ",producto[7],", ",producto[1])
                                          n=n+1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='4':        
                               
                                  print("\nExisten ",len(busq_disco_duro_ordenado), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=1
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de busquedas, Nombre_producto")
                                  print("\nProcesadores: ")
                                  for producto in busq_disco_duro_ordenado[0:(top_n)]:
                                          print(n,", ",producto[7],", ",producto[1])
                                          n=n+1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='5':        
                              
                                  print("\nExisten ",len(busq_usb_ordenado), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=1
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de busquedas, Nombre_producto")
                                  print("\nProcesadores: ")
                                  for producto in busq_usb_ordenado[0:(top_n)]:
                                          print(n,", ",producto[7],", ",producto[1])
                                          n=n+1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='6':        
                              
                                  print("\nExisten ",len(busq_pantalla_ordenado), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=1
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de busquedas, Nombre_producto")
                                  print("\nProcesadores: ")
                                  for producto in busq_pantalla_ordenado[0:(top_n)]:
                                          print(n,", ",producto[7],", ",producto[1])
                                          n=n+1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='7':        
                              
                                  print("\nExisten ",len(busq_bocina_ordenado), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=1
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de busquedas, Nombre_producto")
                                  print("\nProcesadores: ")
                                  for producto in busq_bocina_ordenado[0:(top_n)]:
                                          print(n,", ",producto[7],", ",producto[1])
                                          n=n+1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='8':        
                              
                                  print("\nExisten ",len(busq_audifono_ordenado), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=1
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de busquedas, Nombre_producto")
                                  print("\nProcesadores: ")
                                  for producto in busq_audifono_ordenado[0:(top_n)]:
                                          print(n,", ",producto[7],", ",producto[1])
                                          n=n+1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          else:
                              print("Ingrese una opcion valida por favor")     
                              
                  elif n_respuesta=='4':
                          print("\nLas categorias son:")
                          n=1
                          for cat in categorias_existentes:
                                  print(n," ", cat)
                                  n+=1
                          cual_categoria= input("\n¿De cual GRANDIOSA categoria quiere ver el top MENOS BUSQUEDAS?: ")
                          
                          flag=False
                          
                          if cual_categoria=='1':
                                  
                                  print("\nExisten ",len(busq_procesador_ordenado), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=top_n
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de busquedas, Nombre_producto")
                                  print("\nProcesadores: ")
                                  for producto in busq_procesador_ordenado[-(top_n):]:
                                          print(n,", ",producto[7],", ",producto[1])
                                          n=n-1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                          
                          elif cual_categoria=='2':        
                                  
                                  print("\nExisten ",len(busq_t_video_ordenado), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=top_n
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de busquedas, Nombre_producto")
                                  print("\nProcesadores: ")
                                  for producto in busq_t_video_ordenado[-(top_n):]:
                                          print(n,", ",producto[7],", ",producto[1])
                                          n=n-1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='3':        
                                  
                                  print("\nExisten ",len(busq_t_madre_ordenado), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=top_n
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de busquedas, Nombre_producto")
                                  print("\nProcesadores: ")
                                  for producto in busq_t_madre_ordenado[-(top_n):]:
                                          print(n,", ",producto[7],", ",producto[1])
                                          n=n-1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='4':        
                               
                                  print("\nExisten ",len(busq_disco_duro_ordenado), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=top_n
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de busquedas, Nombre_producto")
                                  print("\nProcesadores: ")
                                  for producto in busq_disco_duro_ordenado[-(top_n):]:
                                          print(n,", ",producto[7],", ",producto[1])
                                          n=n-1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='5':        
                              
                                  print("\nExisten ",len(busq_usb_ordenado), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=top_n
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de busquedas, Nombre_producto")
                                  print("\nProcesadores: ")
                                  for producto in busq_usb_ordenado[-(top_n):]:
                                          print(n,", ",producto[7],", ",producto[1])
                                          n=n-1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='6':        
                              
                                  print("\nExisten ",len(busq_pantalla_ordenado), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=top_n
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de busquedas, Nombre_producto")
                                  print("\nProcesadores: ")
                                  for producto in busq_pantalla_ordenado[-(top_n):]:
                                          print(n,", ",producto[7],", ",producto[1])
                                          n=n-1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='7':        
                              
                                  print("\nExisten ",len(busq_bocina_ordenado), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=top_n
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de busquedas, Nombre_producto")
                                  print("\nProcesadores: ")
                                  for producto in busq_bocina_ordenado[-(top_n):]:
                                          print(n,", ",producto[7],", ",producto[1])
                                          n=n-1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          elif cual_categoria=='8':        
                              
                                  print("\nExisten ",len(busq_audifono_ordenado), "productos en esta categoria")
                                  while flag==False:
                                      top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 3): ")
                                      try:
                                          top_n=int(top_n)
                                          flag=True
                                      except:
                                          print("Escribalo con numero por favor")
                                  n=top_n
                                  print("-----------------------------------------------")
                                  print("Posicion, Numero de busquedas, Nombre_producto")
                                  print("\nProcesadores: ")
                                  for producto in busq_audifono_ordenado[-(top_n):]:
                                          print(n,", ",producto[7],", ",producto[1])
                                          n=n-1
                                  print("-----------------------------------------------") 
                                  input("De enter o cualquier otra letra para continuar")
                                  flag=False
                                  
                          else:
                              print("Ingrese una opcion valida por favor")                      
                      
                  elif n_respuesta=='5':
                      salir_1=True
                      break
                  else:
                      print("Intente de nuevo, por favor")
        
        elif respuesta=='2':
            
            flag=False
            print("\nExisten ",len(x_todos_ordenado_ventas), "productos en TOTAL")
            while flag==False:
                 top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 10): ")
                 try:
                     top_n=int(top_n)
                     flag=True
                 except:
                     print("Escribalo con numero por favor")
                                              
            n=1
            print("\n-----------------------------------------------")
            print("Posicion, Numero de ventas, Nombre_producto, Categoria")
            print("\nTop ",top_n, "Sin importar categoria:\n")
            for producto in x_todos_ordenado_ventas[0:(top_n)]:
                print(n,", ",producto[5],", ",producto[1],", ",producto[3])
                n=n+1
            print("-----------------------------------------------") 
            input("De enter o cualquier otra letra para continuar")

        elif respuesta=='3':
            
            flag=False
            print("\nExisten ",len(busq_todos_ordenado), "productos en TOTAL")
            while flag==False:
                 top_n=input("Ingrese el top 'n' que quiere ver (por ejemplo, escriba 10): ")
                 try:
                     top_n=int(top_n)
                     flag=True
                 except:
                     print("Escribalo con numero por favor")
                                              
            n=1
            print("\n-----------------------------------------------")
            print("Posicion, Numero de busquedas, Nombre_producto, Categoria")
            print("\nTop ",top_n, "Sin importar categoria:\n")
            for producto in busq_todos_ordenado[0:(top_n)]:
                print(n,", ",producto[7],", ",producto[1],", ",producto[3])
                n=n+1
            print("-----------------------------------------------") 
            input("De enter o cualquier otra letra para continuar")            
        
        elif respuesta=='4':
            n=1
            top_n=20
            print("\n-----------------TOP 20 MEJORES reseñas------------------------------")
            print("Posicion, Promedio reseña, Nombre_producto, numero de reseñas")
            print("\nTop ",top_n, "Sin importar categoria:\n")
            for producto in productos_ordenados_reseña[0:(top_n)]:
                print(n,", ",producto[3],", ",producto[1],", ",producto[2])
                n=n+1
            print("-----------------------------------------------") 
            input("De enter o cualquier otra letra para continuar")  
            
        elif respuesta=='5':
            top_n=20
            n=1
            print("\n-----------------TOP 20 PEORES reseñas------------------------------")
            print("Posicion, Promedio reseña, Nombre_producto, numero de reseñas, num_devoluciones")
            print("\nTop ",top_n, "Sin importar categoria:\n")
            for producto in reversed(productos_ordenados_reseña[-(top_n):]):
                print(n,", ",producto[3],", ",producto[1],", ",producto[2],", ",producto[4])
                n=n+1
            print("-----------------------------------------------") 
            input("De enter o cualquier otra letra para continuar")    
            
        elif respuesta=='6':
                print("\nEl negocio estara seguro en nuestras manos, ¡hasta pronto "+ input_usuario+"!")
                salir=True
                break
            
        else:
                print("Intente de nuevo una opcion")
                
                
    else:
        
        while salir==False:
            print("\n¿Que es lo que desea hacer "+input_usuario+" ?")
            print("1. Muestrame tus productos estrella")
            print("2. Muestrame los productos que tengas en descuento")
            print("3. Muestrame todos tus productos")
            print("4. Salir")
            accion= input("Escribe el numero de lo que deseas hacer: ")
            
            if accion=='4':
                salir=True
                print("Gracias por visitarnos, LIFESTORE a su servicio")
                break
        
        
    
    
    
    
    