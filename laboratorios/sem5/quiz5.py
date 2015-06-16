import os
print("Welcome Back Stranger ABC!")
lista= []
opcion=0;
contador = -1
while opcion != "4":
 print("1: Que quieres agregar")
 print("2. Que quieres eliminar")
 print("3. Deseas saber que tienes en tu lista ?")
 print("4. Salir")
 
 opcion=input("Elija la opcion que deseas tomar: ")
 
 if opcion == "1":
  objeto=input("Que quieres agregar? ")
  contador = contador + 1
  objeto = (str(contador) + "." + str(objeto))
  lista.append(objeto)
 if opcion == "2":
  print(lista)
  eliminar = int(input("Que quieres eliminar de la lista? "))
  print("Creo que ya se a eliminado : " + lista[eliminar])
  del lista[eliminar]
 if opcion == "3":
  print(lista)
 
 print("toca enter para continuar")
 input()
 os.system("cls")