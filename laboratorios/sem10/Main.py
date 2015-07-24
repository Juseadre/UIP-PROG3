import os,Lector,Autor,Libro
lista_lectores = []
lista_autores = []
lista_libros = []
opcion=""
while opcion != "6":
	print("1. Ingresar un lector: ")
	print("2. Ingresar un autor: ")
	print("3. Ingresar un libro: ")
	print("4. Hacer peticion: ")
	print("5. Hacer devolucion: ")
	print("6. Salir")
	opcion=input("Ingrese una opcion")
	if opcion=="1":
		ID = input("Ingrese su identificacion por favor, y disculpe la molestia: ")
		nombre = input("Ahora escriba su nombre: ")
		lector = Lector.Lector(ID,nombre)
		lista_lectores.append(lector)
		os.system("cls")
		
	if opcion=="2":
		nombre2=input("Escriba aqui en este sensual espacio yo se que te gusta aceptalo el nombre del autor: ")
		nacionalidad=input("Ahora ingrese su nacionalidad no el tuyo ok si no el del autor: ")
		autor = Autor.Autor(nombre2,nacionalidad)
		lista_autores.append(autor)
		os.system("cls")
		
	if opcion=="3":
		titulo = input("Escriba el titulo: ")
		tipo = input("Escriba el tipo: ")
		editorial = input("Escriba el nombre de la editorial: ")
		libro = Libro.Libro(titulo,tipo,editorial)
		lista_libros.append(libro)
		contador = 10
		os.system("cls")
		
	if opcion=="4":
		contador-=1
		if contador<0:
			print("Que va friend no hay mas libros.")
		else:
			print("Ayala vida se acaban de llevar un libro un libro.")

	if opcion=="5":
		contador+=1
		if contador>10:
			print("Hey! no hay ningun libros que devolver asi que rueda.")
			contador-=1
		else:
			print("Hey llego un lape aqui y trajo este libro.")
