import os 
print("WELCOME BACK STRANGER!") 
opcion=0; 
agenda={} 
while opcion != "5": 
	print("1: IMPRIMIR NUMERO DE TELEFONO") 
	print("2. AGREGAR NUMERO DE TELEFONO") 
	print("3. ELIMINAR NUMERO DE TELEFONO") 
	print("4. BUSCAR NUMERO DE TELEFONO") 
	print("5. SALIR") 
	 
	opcion=input("POR FAVOR ELIJA UN NUMERO: ") 
	 
	if opcion == "2": 
		nombre=str(input("INTRODUZCA UN NOMBRE: ")) 

		numero=int(input("INTRODUZCA UN NUMERO: ")) 

		agenda[nombre] = numero  
	if opcion == "3": 
	
		print(agenda) 
		eliminar=input("INTRODUZCA EL NOMBRE QUE DESEAS ELIMINAR DE LA AGENDA: ") 
		if eliminar in agenda: 
			del agenda[eliminar] 
			print("CREO QUE SE ELIMINO "+ str(eliminar) + "...UMMM O TAL VEZ NO") 
		else: 
			print("HEY HEY HEY YO NO VEO ESO") 
	if opcion == "1": 
		print(agenda) 
	if opcion == "4": 
		buscar=str(input("A QUIEN QUIERES BUSCAR? ")) 
		if buscar in agenda: 
			print("Numero: " + str(agenda[buscar])) 
		else: 
			print("HEY HEY HEY ESO NO ESTA AQUI") 
	print("HEY DALE AL BOTON ESE GORDO QUE SE LLAMA ENTER PARA CONTINUAR") 

 
	input() 
	os.system("cls") 
